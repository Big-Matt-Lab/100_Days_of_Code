"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Blackjack Game ***
A simplified, text-based game of Blackjack against a computer dealer.

Python concepts highlighted:
- `random` module for card dealing
- `os` module for clearing the console
- Function definition for modularity (`deal_card`, `calculate_score`, etc.)
- List data structures to represent hands of cards
- `while` loops for game flow (player's turn, replay option)
- `if/elif/else` for game logic and determining outcomes
- F-strings for dynamic and readable output
- Input handling and sanitization (`input()`, `lower()`)
"""

import random
import os

def clear_console():
    """Clears the console screen for a cleaner game display."""
    # Python concept: Using os.system to run a shell command. 'nt' is for Windows.
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from the deck."""
    # Python concept: A list representing card values. Ace is 11, face cards are 10.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Python concept: `random.choice` selects a single item from a sequence.
    return random.choice(cards)

def calculate_score(cards):
    """
    Calculates the score of a given hand, handling Aces and Blackjack.
    Blackjack (an Ace + a 10-value card on the initial deal) is returned as 0.
    """
    # Python concept: `sum()` to total list items, `len()` to get list length.
    # A score of 0 represents a Blackjack, giving it a special status.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Python concept: `in` operator and `count()` method for list inspection.
    # Handle Aces: If score > 21, change an Ace's value from 11 to 1.
    score = sum(cards)
    num_aces = cards.count(11)
    # Python concept: `while` loop to adjust for one or more Aces.
    while score > 21 and num_aces > 0:
        score -= 10  # Effectively changes an 11 to a 1
        num_aces -= 1
    return score

def compare(player_score, dealer_score):
    """Compares player and dealer scores to determine the winner."""
    # Python concept: `if/elif/else` chain for complex conditional logic.
    if player_score == dealer_score:
        return "It's a draw."
    elif dealer_score == 0:
        return "You lose, dealer has Blackjack!"
    elif player_score == 0:
        return "You win with a Blackjack!"
    elif player_score > 21:
        return "You went over. You lose."
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    """Runs a single round of Blackjack."""
    print("--- Welcome to Blackjack ---")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Player's turn
    while True:
        player_score = calculate_score(player_hand)
        print(f"  Your cards: {player_hand}, current score: {player_score}")
        print(f"  Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or player_score > 21:
            break

        hit_or_stand = input("Type 'h' to Hit, or 's' to Stand: ").lower()
        if hit_or_stand == 'h':
            player_hand.append(deal_card())
        else:
            break

    # Dealer's turn
    dealer_score = calculate_score(dealer_hand)
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print("\n--- Final Results ---")
    print(f"  Your final hand: {player_hand}, final score: {calculate_score(player_hand)}")
    print(f"  Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(calculate_score(player_hand), dealer_score))
    print("---------------------\n")

if __name__ == "__main__":
    while input("Do you want to play a hand of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        clear_console()
        play_game()
