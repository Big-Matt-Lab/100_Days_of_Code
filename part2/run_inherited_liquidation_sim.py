import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
import shutil

# Enable seaborn theme
sns.set_theme(style="whitegrid", palette="colorblind", font="DejaVu Sans")

RMD_DIVISORS = {
    73: 26.5,
    74: 25.5,
    75: 24.6,
    76: 23.7,
    77: 22.9,
    78: 22.0,
    79: 21.1,
    80: 20.2,
    81: 19.4,
    82: 18.5,
    83: 17.7,
    84: 16.8,
    85: 16.0,
    86: 15.2,
    87: 14.4,
    88: 13.7,
    89: 12.9,
    90: 12.2,
    91: 11.5,
    92: 10.8,
}


class Account:
    def __init__(self, name, balance, growth_rate, tax_drag=0.0):
        self.name = name
        self.balance = balance
        self.growth_rate = growth_rate
        self.tax_drag = tax_drag

    def grow(self, net_contribution=0.0):
        effective_rate = self.growth_rate - self.tax_drag
        self.balance = (self.balance + net_contribution) * (1 + effective_rate)
        self.balance = max(0.0, self.balance)


def get_federal_tax(taxable_income, is_matt_65, is_eileen_65, itemized_deduction=0.0):
    brackets = [
        (23200, 0.10),
        (94300, 0.12),
        (201050, 0.22),
        (383900, 0.24),
        (float("inf"), 0.32),
    ]
    standard_deduction = 29200
    if is_matt_65:
        standard_deduction += 1550
    if is_eileen_65:
        standard_deduction += 1550

    deduction = max(standard_deduction, itemized_deduction)
    fed_taxable = max(0.0, taxable_income - deduction)

    fed_tax = 0.0
    previous_limit = 0.0
    remaining_income = fed_taxable

    for limit, rate in brackets:
        bracket_width = limit - previous_limit
        taxable_in_bracket = min(remaining_income, bracket_width)
        fed_tax += taxable_in_bracket * rate
        remaining_income -= taxable_in_bracket
        if remaining_income <= 0:
            break
        previous_limit = limit

    return fed_tax


def get_south_carolina_tax(taxable_income, is_matt_65, is_eileen_65):
    sc_subtraction = 0.0
    sc_subtraction += 15000 if is_matt_65 else 3000
    sc_subtraction += 15000 if is_eileen_65 else 3000
    sc_taxable = max(0.0, taxable_income - sc_subtraction)
    return sc_taxable * 0.0427


def get_irmaa_surcharge(magi):
    if magi <= 218000:
        return 0.0
    elif magi <= 274000:
        return 2297.0
    elif magi <= 342000:
        return 5770.0
    else:
        return 9240.0


def run_sim_correct(inherited_mode, target_magi=218000):
    ira = Account("Rollover IRA", 1225203.98, growth_rate=0.070)

    # 2.0% fee drag on Inherited IRA if kept open
    inherited_growth = 0.05 if inherited_mode != "Roth_Liquidate_2027" else 0.07
    inherited_ira = Account("Inherited IRA", 26181.12, growth_rate=inherited_growth)

    traditional_brokerage = Account(
        "Traditional Brokerage", 269188.33 + 24908.52, growth_rate=0.070, tax_drag=0.004
    )
    trust_brokerage = Account(
        "Trust Brokerage", 191310.70, growth_rate=0.070, tax_drag=0.004
    )
    roth_ira = Account("Roth IRA", 0.0, growth_rate=0.070)

    base_pension_2027 = 46748.64 + 9240.00
    base_ss_2027 = 35100.00 + 16872.00
    cola_rate = 0.026

    base_non_tax_expenses_2027 = 136234.70

    records = []

    for year_idx, year in enumerate(range(2027, 2054)):
        age_matt = 65 + year_idx
        age_eileen = 64 + year_idx

        is_matt_65 = age_matt >= 65
        is_eileen_65 = age_eileen >= 65

        pension = base_pension_2027 * ((1 + cola_rate) ** year_idx)
        ss = base_ss_2027 * ((1 + cola_rate) ** year_idx)
        non_tax_expenses = base_non_tax_expenses_2027 * ((1 + cola_rate) ** year_idx)

        itemized_deduction = 30000.0 * ((1 + 0.02) ** year_idx)

        inherited_withdrawal = 0.0
        lifestyle_withdrawal = 72000.0 * ((1 + cola_rate) ** year_idx)

        if inherited_mode == "Current_Plan" or inherited_mode == "Roth_Standard":
            if year <= 2033:
                inherited_withdrawal = inherited_ira.balance / (7.0 - year_idx)
            else:
                inherited_withdrawal = 0.0
        elif inherited_mode == "Roth_Liquidate_2027":
            if year == 2027:
                inherited_withdrawal = inherited_ira.balance
            else:
                inherited_withdrawal = 0.0

        # Handle lifestyle withdrawal
        if year == 2027 and inherited_mode == "Roth_Liquidate_2027":
            lifestyle_withdrawal = 48000.0

        rmd = 0.0
        rollover_lifestyle = lifestyle_withdrawal
        if age_matt >= 73:
            divisor = RMD_DIVISORS[age_matt]
            rmd = ira.balance / divisor
            rollover_lifestyle = max(lifestyle_withdrawal, rmd)

        # Roth Conversion Headroom
        roth_conversion = 0.0
        if inherited_mode != "Current_Plan" and year <= 2033:
            fixed_magi_components = (
                pension + ss + inherited_withdrawal + rollover_lifestyle
            )
            max_allowed_conversion = max(0.0, target_magi - fixed_magi_components)
            roth_conversion = min(max_allowed_conversion, ira.balance)

        magi = (
            pension + ss + inherited_withdrawal + rollover_lifestyle + roth_conversion
        )
        gross_taxable_income = (
            pension
            + ss * 0.85
            + inherited_withdrawal
            + rollover_lifestyle
            + roth_conversion
        )
        fed_tax = get_federal_tax(
            gross_taxable_income,
            is_matt_65,
            is_eileen_65,
            itemized_deduction=itemized_deduction,
        )
        sc_tax = get_south_carolina_tax(gross_taxable_income, is_matt_65, is_eileen_65)
        total_income_tax = fed_tax + sc_tax
        irmaa_surcharge = get_irmaa_surcharge(magi)
        total_tax_due = total_income_tax + irmaa_surcharge

        # Checking cash flow
        checking_cash_inflow = pension + ss + inherited_withdrawal + rollover_lifestyle
        baseline_net_surplus = max(
            0.0, checking_cash_inflow - non_tax_expenses - total_tax_due
        )
        frivolous_spent = 0.25 * baseline_net_surplus
        net_checking_flow = (
            checking_cash_inflow - non_tax_expenses - total_tax_due - frivolous_spent
        )

        # Initialize year-end flows for accounts
        ira_flow = -rollover_lifestyle - roth_conversion
        roth_flow = roth_conversion
        tb_flow = 0.0
        trad_flow = 0.0
        inherited_flow = 0.0

        if inherited_mode == "Current_Plan":
            if net_checking_flow >= 0.0:
                trad_flow = net_checking_flow
                tb_flow = 0.0
            else:
                shortfall = -net_checking_flow
                if trust_brokerage.balance >= shortfall:
                    tb_flow = -shortfall
                    trad_flow = 0.0
                else:
                    rem = shortfall - trust_brokerage.balance
                    tb_flow = -trust_brokerage.balance
                    trad_flow = -rem
            if year <= 2033:
                inherited_flow = -inherited_withdrawal
        else:
            # Roth Scenarios (Taxes Paid from Trust Brokerage)
            checking_shortfall_before_tax = (
                checking_cash_inflow - non_tax_expenses - frivolous_spent
            )

            if checking_shortfall_before_tax >= 0.0:
                trad_flow = checking_shortfall_before_tax
                if trust_brokerage.balance >= total_tax_due:
                    tb_flow = -total_tax_due
                else:
                    rem = total_tax_due - trust_brokerage.balance
                    tb_flow = -trust_brokerage.balance
                    trad_flow += -rem
            else:
                total_draw = total_tax_due - checking_shortfall_before_tax
                if trust_brokerage.balance >= total_draw:
                    tb_flow = -total_draw
                    trad_flow = 0.0
                else:
                    rem = total_draw - trust_brokerage.balance
                    tb_flow = -trust_brokerage.balance
                    trad_flow = -rem

            if inherited_mode == "Roth_Standard" and year <= 2033:
                inherited_flow = -inherited_withdrawal
            elif inherited_mode == "Roth_Liquidate_2027" and year == 2027:
                inherited_flow = -inherited_withdrawal

        # Grow accounts with accumulated flows exactly ONCE
        ira.grow(ira_flow)
        roth_ira.grow(roth_flow)
        trust_brokerage.grow(tb_flow)
        traditional_brokerage.grow(trad_flow)
        if inherited_mode != "Roth_Liquidate_2027":
            inherited_ira.grow(inherited_flow)
        else:
            if year == 2027:
                inherited_ira.grow(inherited_flow)  # Will hit 0
            else:
                inherited_ira.balance = 0.0

        total_portfolio_value = (
            ira.balance
            + roth_ira.balance
            + traditional_brokerage.balance
            + trust_brokerage.balance
            + inherited_ira.balance
        )

        latent_tax_rate = 0.22
        after_tax_portfolio_value = (
            (ira.balance + inherited_ira.balance) * (1 - latent_tax_rate)
            + roth_ira.balance
            + traditional_brokerage.balance
            + trust_brokerage.balance
        )

        records.append(
            {
                "Year": year,
                "Age": age_matt,
                "Total Value": total_portfolio_value,
                "After-Tax Value": after_tax_portfolio_value,
            }
        )

    return pd.DataFrame(records)


# Generate dataframes
df_none = run_sim_correct("Current_Plan")
df_std = run_sim_correct("Roth_Standard")
df_liq = run_sim_correct("Roth_Liquidate_2027")

# Create a beautiful plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot lines
plt.plot(
    df_none["Year"],
    df_none["After-Tax Value"] / 1e6,
    label="Current Plan (No Conversions)",
    color="#1f77b4",
    linewidth=2.5,
)
plt.plot(
    df_std["Year"],
    df_std["After-Tax Value"] / 1e6,
    label="Roth Conversion (7-Yr Inherited Depletion)",
    color="#ff7f0e",
    linestyle="--",
    linewidth=2.0,
)
plt.plot(
    df_liq["Year"],
    df_liq["After-Tax Value"] / 1e6,
    label="Roth Conversion (Jan 2027 Inherited Liquidation)",
    color="#2ca02c",
    linewidth=2.5,
)

# Highlight title as a takeaway
ax.set_title(
    "Jan 2027 Inherited IRA Liquidation Boosts Family Wealth by $44,040",
    fontsize=13,
    fontweight="bold",
    pad=15,
)
ax.set_xlabel("Calendar Year\n(Age Matt / Age Eileen)", fontsize=11, labelpad=10)
ax.set_ylabel("After-Tax Net Worth ($ Millions)", fontsize=11)

# Generate x-ticks
years = df_none["Year"].values
ages_matt = df_none["Age"].values
ages_eileen = ages_matt - 1
xticks_indices = np.arange(0, len(years), 4)
plt.xticks(
    years[xticks_indices],
    [
        f"{int(y)}\n({int(am)}/{int(ae)})"
        for y, am, ae in zip(
            years[xticks_indices],
            ages_matt[xticks_indices],
            ages_eileen[xticks_indices],
        )
    ],
    fontsize=9,
)

plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(
    loc="upper left", fontsize=10, frameon=True, facecolor="white", edgecolor="none"
)

# Highlights text box
liq_diff = df_liq.iloc[-1]["After-Tax Value"] - df_std.iloc[-1]["After-Tax Value"]
total_diff = df_liq.iloc[-1]["After-Tax Value"] - df_none.iloc[-1]["After-Tax Value"]
box_text = (
    f"At Horizon (2053):\n"
    f"• Combined Roth Strategy Gain: +${total_diff:,.0f} vs Baseline\n"
    f"• Jan 2027 Liquidation Advantage: +${liq_diff:,.0f} vs Standard Roth\n"
    f"  (Eliminated 2.0% advisor fee drag on the Inherited IRA)"
)
props = dict(
    boxstyle="round,pad=0.5", facecolor="#faf7f3", edgecolor="#d3d3d3", alpha=0.9
)
plt.text(2028, 3.4, box_text, fontsize=10, verticalalignment="top", bbox=props)

plt.tight_layout()

# Save first to scratch
os.makedirs("/workspace/scratch/inherited_liquidation", exist_ok=True)
plt.savefig(
    "/workspace/scratch/inherited_liquidation/inherited_liquidation_wealth.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close()

# Copy to out
shutil.copy(
    "/workspace/scratch/inherited_liquidation/inherited_liquidation_wealth.png",
    "/workspace/out/inherited_liquidation_wealth.png",
)
shutil.copy(__file__, "/workspace/out/run_inherited_liquidation_sim.py")

print("SUCCESS: Chart generated and copied to out")
