# Math IA
## Overview
This is the probability calculation code for my internal assessment in International Baccalaureate Mathematics: Analysis and Approaches (Standard Level). My project is centered around probability: I'm making a heavily dealer-weighted gambling game. See [The Game](#the-game) for a detailed explanation of the rules and mechanics.

## The Game
The player bets B$. The player then rolls a d20 down a dice tower which leads into a box with a layout as shown in figure 1. The number shown on the d20 is multiplied by the factor indicated by the sector in the box. The product is the number of cards drawn from a deck of cards. The winnings are calculated by this formula: `1.5B * # of jokers + B * # of aces + 0.5B * # of kings + 0.25B * # of queens`

Figure 1

![Figure 1](/images/Figure%201.png)


## TODO
- Get better picture for figure 1
- Model and 3D print dice tower and board
    - Test probabilities of each option on board
- Finish in-file TODO lists
- Factor in all probabilities to a single program. Output:
    - Probability of a specific permutation
    - Probability of a specific return
    - Expected percentage return on a bet
    - Expected numerical return on a bet
    - Spreadsheet with all permutations, their probabilities
- Finalize winnings table, box factors, etc.