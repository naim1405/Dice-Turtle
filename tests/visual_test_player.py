"""
Visual test for Player module - displays the turtle window for visual inspection.

Run this with: python tests/visual_test_player.py
Press Enter in the terminal to cycle through players.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from turtle import Screen
from player import Player


def test_player_visual():
    """Visual test for Player module with pause."""
    
    # Setup screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Player Module Visual Test")
    
    # Create player instance
    player = Player()
    
    print("\n=== Player Module Visual Test ===")
    print(f"Starting player: {Player.player_color[Player.current_player]}")
    print("Player display position: (-300, 320)")
    
    input("\nPress Enter to cycle through all players...")
    
    # Cycle through all players twice
    for cycle in range(2):
        print(f"\n--- Cycle {cycle + 1} ---")
        for i in range(4):
            player.handle_player_change()
            current = Player.player_color[Player.current_player]
            print(f"Player {Player.current_player}: {current}")
            
            if i < 3 or cycle < 1:
                input("Press Enter to change to next player...")
    
    print("\n=== Test Complete ===")
    print("Notice how the player cycles: Green → Yellow → Blue → Red → Green...")
    input("\nPress Enter to close the window...")
    screen.bye()


if __name__ == "__main__":
    test_player_visual()
