"""Milestone 1 - Script 3: Python Functions.

This script demonstrates the usage of functions in Python, showcasing 
proper type hinting, structural spacing, and detailed Google-style docstrings.

"""


def total_goals(league_goals: int, champions_goals: int) -> int:
    """Calculates the total number of goals scored in a season.

    Args:
        league_goals: Number of goals scored in the domestic league.
        champions_goals: Number of goals scored in the champions league.

    Returns:
        The sum of league goals and champions league goals.
    """
    return league_goals + champions_goals


def player_information(name: str, club: str) -> None:
    """Prints formatted information about a football player.

    Args:
        name: The full name of the player.
        club: The current club the player plays for.
    """
    print(f"Player: {name}")
    print(f"Club: {club}")


# ==============================================================================
# Execution
# ==============================================================================

# Google style requires spaces around the assignment operator (=)
ronaldo_total: int = total_goals(35, 8)
print(ronaldo_total)

player_information("Cristiano Ronaldo", "Al Nassr")