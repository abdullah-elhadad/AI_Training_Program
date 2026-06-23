"""
Player model module.
This module defines the Player class.
"""

class Player:
    """
    Represents a football player.
    """

    def __init__(
        self,
        name: str,
        club: str,
        national_team: str
    ) -> None:
        """
        Initialize player information.

        Args:
            name: Player name.
            club: Player club.
            national_team: Player national team.
        """
        self.name = name
        self.club = club
        self.national_team = national_team

    def get_info(self) -> dict[str, str]:
        """
        Return player information.

        Returns:
            Dictionary containing player data.
        """
        return {
            "name": self.name,
            "club": self.club,
            "national_team": self.national_team
        }