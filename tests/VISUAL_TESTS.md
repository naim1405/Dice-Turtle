# Visual Tests

Visual tests allow you to see the actual turtle graphics window and verify the visual appearance of components.

## Available Visual Tests

### 1. Action Module
```bash
python tests/visual_test_action.py
```
Shows the action display ("Roll Dice" / "Move Piece") and cycles through player colors.

### 2. Dice Module
```bash
python tests/visual_test_dice.py
```
Shows the dice rolling animation and displays the dice values. Rolls 10 times with pauses between each roll.

### 3. Player Module
```bash
python tests/visual_test_player.py
```
Shows the player display cycling through all 4 players (Green → Yellow → Blue → Red).

## How to Use

1. Run any visual test from the project root directory
2. The turtle window will open
3. Follow the prompts in the terminal
4. Press Enter to proceed through each step
5. Press Enter at the end to close the window

## Note

These tests are for **visual inspection only** and are not part of the automated test suite. They're useful for:
- Debugging visual issues
- Verifying colors and positioning
- Checking animations and transitions
- Manual acceptance testing

The automated unit tests in `tests/unit/` mock the turtle graphics to run without opening windows.
