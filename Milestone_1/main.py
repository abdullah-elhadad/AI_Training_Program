"""Main execution entry point for the football application.

This script wires up the MVC components (Model, View, Controller) and 
demonstrates the full flow by initializing and updating a player profile.

Author: football
Style: Google Python Style Guide
"""

from controllers.player_controller import PlayerController
from views.player_view import PlayerView


def main() -> None:
    """The main function to initialize and run the MVC application workflow."""
    controller: PlayerController = PlayerController()
    view: PlayerView = PlayerView()

    player_data: dict[str, str] = controller.create_player(
        "Cristiano Ronaldo",
        "Al Nassr",
        "Portugal"
    )

    view.show_player(player_data)


if __name__ == "__main__":
    main()