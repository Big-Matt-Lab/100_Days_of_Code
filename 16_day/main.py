from prettytable import PrettyTable

my_dict = {"Pokemon": ('Pikachu', 'Squirtle', 'Charmander'), "Type": ('Electric', 'Water', 'Fire')}

table = PrettyTable()
for col, rows in my_dict.items():
    table.add_column(col, rows)
table.align = "l"

print(table)
