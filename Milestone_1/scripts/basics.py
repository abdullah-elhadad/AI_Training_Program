"""Milestone 1 - Script 1: Python Basics.

This script covers the fundamentals of Python, including variables, 
data types, lists, and dictionaries, strictly following the Google 
Python Style Guide with proper type hints and docstrings.

Author: football
Style: Google Python Style Guide
"""

# ==============================================================================
# 1. Variables & Type Hints
# ==============================================================================

player_name: str = "Cristiano Ronaldo"
club_name: str = "Real Madrid"
national_team: str = "Egypt"

print(player_name)
print(club_name)
print(national_team)

# ==============================================================================
# 2. Data Types
# ==============================================================================
goals = 938
age = 41
market_value = 12000000.50
is_legend = True

print(type(goals))
print(type(age))
print(type(market_value))
print(type(is_legend))

# ==============================================================================
# 3. Lists
# ==============================================================================

# Explicitly defining the list elements type as strings
favorite_players: list[str] = ["Cristiano Ronaldo", "Salah", "Benzema"]
print(favorite_players)

# Appending an item
favorite_players.append("Vinicius")
print(favorite_players)

# ==============================================================================
# 4. Dictionaries
# ==============================================================================

# Dictionary example
ronaldo_stats = {
    "goals": 938,
    "assists": 257,
    "club": "Al Nassr"
}

print(ronaldo_stats)