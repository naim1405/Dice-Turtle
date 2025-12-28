"""
Visual test for Action module - displays the turtle window for visual inspection.

Run this with: python tests/visual_test_action.py
Press Enter in the terminal to close the window.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from turtle import Screen
from action import Action
from player import Player


def test_action_visual():
    """Visual test for Action module with pause."""
    
    # Setup screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Action Module Visual Test")
    
    # Create action instance
    print("\n=== Action Module Visual Test ===")
    print("Current player:", Player.player_color[Player.current_player])
    print("Action displayed: Roll Dice (action=0)")
    
    # The action is already displayed by __init__
    
    # Pause to view
    input("\nPress Enter to update action to 'Move Piece'...")
    
    # Update to action 1
    from action import action_writer
    action_writer.update_action(1)
    print("Action updated to: Move Piece (action=1)")
    
    input("\nPress Enter to cycle through players...")
    
    # Cycle through players
    from player import p
    for i in range(4):
        p.handle_player_change()
        action_writer.write_action()  # Redraw with new player color
        print(f"Player changed to: {Player.player_color[Player.current_player]}")
        input(f"Press Enter to continue to next player...")
    
    print("\n=== Test Complete ===")
    input("Press Enter to close the window...")
    screen.bye()


if __name__ == "__main__":
    test_action_visual()
