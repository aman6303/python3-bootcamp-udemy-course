# Card War Game

A classic card game implementation in Python using Object-Oriented Programming principles and modular design.

## Description

War is a simple card game typically played by two players. Each player starts with half of a standard 52-card deck. Players simultaneously reveal their top cards, and the player with the higher card wins both cards. When cards are equal, a "war" occurs where players place additional cards face-down and reveal another card to determine the winner.

## Features

- Classic War card game rules
- Two-player gameplay
- Automatic war scenario handling
- Game statistics tracking
- Customizable player names
- Configurable round limits
- Modular code structure

## How to Play

1. Run the program
2. Enter names for Player 1 and Player 2 (or press Enter for defaults)
3. Set the maximum number of rounds (or press Enter for default 1000)
4. Watch the game play automatically
5. View final statistics when the game ends

## Game Rules

- Each player starts with 26 cards
- Players play one card at a time
- Higher card wins both cards
- When cards are equal, WAR occurs:
  - Each player places 3 cards face-down
  - Then plays 1 card face-up
  - Higher card wins all cards in the pot
  - If still equal, another war occurs

## Example Output

```
==================================================
WAR CARD GAME
==================================================

Player 1: 26 cards
Player 2: 26 cards

Let the game begin!

Round 1: Player 1: 7♥ vs Player 2: 3♠
Player 1 wins this round

Round 2: Player 1: K♦ vs Player 2: K♣

WAR!
Player 1: 5♥ vs Player 2: 9♠
Player 2 wins the war! (+10 cards)
```
