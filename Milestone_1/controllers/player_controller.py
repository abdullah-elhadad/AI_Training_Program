"""Player controller component for the football application.

"""

from models.player import Player


class PlayerController:
    """Coordinates behavior and data transformation for player entities."""

    def create_player(
        self,
        name: str,
        club: str,
        national_team: str
    ) -> dict[str, str]:
        """Creates a player instance and returns their structured data.

        Args:
            name: The full name of the football player.
            club: The current club the player represents.
            national_team: The country the player represents internationally.

        Returns:
            A dictionary containing the freshly created player's profile data.
        """
        player = Player(name, club, national_team)
        return player.get_info()
    
    