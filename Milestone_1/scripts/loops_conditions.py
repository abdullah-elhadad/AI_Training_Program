"""Milestone 1 - Script 2: Loops and Conditions.

This script demonstrates control flow mechanisms in Python, specifically 
for loops, while loops, and conditional statements (if/elif/else), 
adhering to the Google Python Style Guide.

Author: football
Style: Google Python Style Guide
"""

# ==============================================================================
# 1. For Loops
# ==============================================================================

players: list[str] = ["Ronaldo", "Salah", "Bellingham"]

for player in players:
    print(player)

# ==============================================================================
# 2. Conditional Statements (If / Elif / Else)
# ==============================================================================
ronaldo_goals: int = 40


if ronaldo_goals > 30:
    print("Top scorer")
elif ronaldo_goals == 30:
    print("Good season")
else:
    print("Needs improvement")

# ==============================================================================
# 3. While Loops
# ==============================================================================
remaining_matches: int = 3

while remaining_matches > 0:
    print(f"Match day remaining: {remaining_matches}")
    remaining_matches -= 1  # Decrementing the counter to avoid an infinite loop