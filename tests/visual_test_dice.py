"""
Visual test for Dice module - displays the turtle window for visual inspection.

Run this with: python tests/visual_test_dice.py
Press Enter in the terminal to continue rolling dice.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from turtle import Screen
from dice import Dice


def test_dice_visual():
    """Visual test for Dice module with pause."""
    
    # Setup screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Dice Module Visual Test")
    
    # Load dice images
    for i in range(1, 7):
        try:
            screen.addshape(f"./resources/dice_{i}.gif")
        except:
            print(f"Warning: Could not load dice_{i}.gif")
    
    try:
        screen.addshape("./resources/dice_blank.gif")
    except:
        print("Warning: Could not load dice_blank.gif")
    
    # Create dice instance
    dice = Dice()
    
    print("\n=== Dice Module Visual Test ===")
    print("Dice starting position: (8, 335)")
    
    input("\nPress Enter to roll the dice...")
    
    # Roll multiple times
    for i in range(10):
        dice.roll()
        print(f"Roll {i+1}: {Dice.current_value}")
        print(f"Consecutive sixes: {Dice.consecutive_six}")
        
        if Dice.consecutive_six == 3:
            print("⚠️  Three consecutive sixes! Re-rolling...")
        
        if i < 9:
            input("Press Enter to roll again...")
        
    print("\n=== Test Complete ===")
    print(f"Final value: {Dice.current_value}")
    print(f"Previous value: {Dice.prev_value}")
    input("\nPress Enter to close the window...")
    screen.bye()


if __name__ == "__main__":
    test_dice_visual()
