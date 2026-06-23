"""
Player view module.
Handles displaying player information.
"""


class PlayerView:
    """
    Displays player information.
    """

    def show_player(
        self,
        player_data: dict[str, str]
    ) -> None:
        """
        Display player information.

        Args:
            player_data: Dictionary containing player data.
        """
        print("=" * 40)
        print("Player Information")
        print("=" * 40)

        print(f"Name          : {player_data['name']}")
        print(f"Club          : {player_data['club']}")
        print(f"National Team : {player_data['national_team']}")