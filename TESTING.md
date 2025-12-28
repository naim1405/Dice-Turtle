# Testing Documentation for Dice-Turtle

This document provides comprehensive information about the test suite for the Dice-Turtle board game project.

## Table of Contents

1. [Overview](#overview)
2. [Test Structure](#test-structure)
3. [Running Tests](#running-tests)
4. [Test Coverage](#test-coverage)
5. [Test Modules](#test-modules)
6. [Writing New Tests](#writing-new-tests)
7. [Common Patterns](#common-patterns)

---

## Overview

The Dice-Turtle test suite uses **pytest** as the testing framework. All tests are located in the `tests/` directory and organized into three categories:

- **Unit Tests** (`tests/unit/`) - Test individual components in isolation
- **Integration Tests** (`tests/integration/`) - Test interactions between components
- **System Tests** (`tests/system/`) - Test the complete application flow

---

## Test Structure

```
tests/
├── conftest.py              # Shared fixtures and configuration
├── unit/
│   ├── test_dice.py         # Dice rolling and state tests
│   ├── test_player.py       # Player turn management tests
│   ├── test_action.py       # Action display tests
│   ├── test_piece_path.py   # Path data validation tests
│   ├── test_piece.py        # Piece movement and logic tests
│   └── test_board.py        # Board rendering tests
├── integration/
│   └── (integration tests go here)
└── system/
    └── (system tests go here)
```

---

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/unit/test_dice.py
```

### Run Specific Test Class

```bash
pytest tests/unit/test_dice.py::TestDiceRolling
```

### Run Specific Test Method

```bash
pytest tests/unit/test_dice.py::TestDiceRolling::test_roll_generates_value_in_range
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run Tests with Coverage Report

```bash
pytest --cov=. --cov-report=html
```

### Run Tests and Stop on First Failure

```bash
pytest -x
```

---

## Test Coverage

The test suite covers the following areas:

### **1. Dice Module (`test_dice.py`)**

**Tests: 11** covering:
- Initialization and turtle inheritance
- Random dice rolling (1-6 range)
- State management (prev_value, current_value)
- Consecutive six detection and handling
- Automatic re-roll on three consecutive sixes
- Shape updates to match dice value
- Class variable sharing across instances

### **2. Player Module (`test_player.py`)**

**Tests: 13** covering:
- Player initialization
- Turn cycling through 4 players (0 → 1 → 2 → 3 → 0)
- Player color assignments (Green, Yellow, Blue, Red)
- Display position updates
- Screen clearing between turns
- Player label and name rendering
- Class variable state management

### **3. Action Module (`test_action.py`)**

**Tests: 13** covering:
- Action display initialization
- Position setting at (120, 320)
- "Roll Dice" action display (action = 0)
- "Move Piece" action display (action = 1)
- Action toggling
- Screen clearing before updates
- Color matching with current player
- Global instance creation

### **4. Piece Path Module (`test_piece_path.py`)**

**Tests: 21** covering:
- Path length validation (57 positions per path)
- Coordinate format validation [x, y]
- Unique starting positions for each player
- Board boundary validation
- Inactive position arrays (4 per player)
- Active position arrays (4 per player)
- Corner positioning for inactive zones
- Path-to-position alignment
- Data export verification

### **5. Piece Module (`test_piece.py`)**

**Tests: 21** covering:
- Piece initialization with player assignment
- Color assignment per player
- Position management (inactive → active → path)
- Movement mechanics and validation
- Turn-based movement restrictions
- Path length boundaries (0-56)
- Piece activation with dice value 6
- `set_inactive()` method
- Overlap detection setup
- Status tracking (available/active pieces)
- Click handler registration

### **6. Board Module (`test_board.py`)**

**Tests: 16** covering:
- Board initialization
- Turtle positioning at (-300, 300)
- Board dimensions (15x15, 41px boxes)
- Box drawing in both directions
- Inactive zone creation with player colors
- Path creation (left, right, top, bottom)
- 3x6 and 6x3 grid layouts
- Main board square rendering
- Data structure initialization
- Turtle hiding after completion

---

## Test Modules

### `conftest.py` - Shared Test Fixtures

Provides reusable fixtures for all tests:

#### **`mock_turtle`**
Mocks the turtle.Turtle class to prevent GUI windows from opening during tests.

```python
def test_something(mock_turtle):
    # Turtle is mocked, no GUI will appear
    from dice import Dice
    dice = Dice()
```

#### **`mock_screen`**
Mocks the turtle.Screen class for screen-related operations.

#### **`reset_class_variables`**
Resets class-level state between tests to ensure test isolation.

```python
def test_something(reset_class_variables):
    # Class variables are reset before and after this test
    from dice import Dice
    assert Dice.current_value == 0
```

#### **`mock_dice_roll`**
Controls dice roll outcomes for deterministic testing.

```python
def test_roll_six(mock_dice_roll):
    mock_dice_roll(6)  # Next roll will be 6
    dice.roll()
    assert Dice.current_value == 6
```

#### **Sample Data Fixtures**
- `sample_path` - Example path for testing
- `sample_inactive_pos` - Example inactive positions
- `sample_active_pos` - Example active positions

---

## Writing New Tests

### Test Structure Template

```python
import pytest
from unittest.mock import patch, MagicMock


class TestYourFeature:
    """Test suite description."""
    
    def test_something_specific(self, mock_turtle):
        """Test description in plain English."""
        # Arrange - Set up test data and mocks
        from your_module import YourClass
        instance = YourClass()
        
        # Act - Perform the action being tested
        result = instance.method()
        
        # Assert - Verify the result
        assert result == expected_value
```

### Best Practices

1. **One assertion per test** - Keep tests focused
2. **Descriptive names** - Use `test_verb_expected_behavior` format
3. **Use fixtures** - Leverage conftest.py fixtures for common setup
4. **Mock external dependencies** - Especially turtle graphics
5. **Test edge cases** - Boundary values, empty inputs, etc.
6. **Document test purpose** - Add docstrings explaining what's tested

### Example: Adding a New Test

```python
@patch('piece.Turtle.__init__', return_value=None)
@patch('piece.Turtle.goto')
class TestNewFeature:
    """Test suite for new feature."""
    
    def test_new_behavior(self, mock_goto, mock_init):
        """Test that new behavior works as expected."""
        from piece import Piece
        piece = Piece(0, path, inactive_pos, active_pos)
        
        piece.new_method()
        
        assert piece.new_attribute == expected_value
```

---

## Common Patterns

### Pattern 1: Testing Class Initialization

```python
def test_initialization(self, mock_turtle):
    """Test that class initializes correctly."""
    from module import ClassName
    instance = ClassName()
    
    assert instance.attribute == expected_value
    assert hasattr(instance, 'required_attribute')
```

### Pattern 2: Testing State Changes

```python
def test_state_change(self, reset_class_variables):
    """Test that state changes correctly."""
    from module import ClassName
    ClassName.class_var = initial_value
    
    instance = ClassName()
    instance.change_state()
    
    assert ClassName.class_var == new_value
```

### Pattern 3: Testing with Mocked Dependencies

```python
@patch('module.Dependency')
def test_with_dependency(self, mock_dependency):
    """Test interaction with dependency."""
    mock_dependency.return_value = expected_return
    
    from module import ClassName
    instance = ClassName()
    result = instance.use_dependency()
    
    assert result == expected_result
    mock_dependency.assert_called_once()
```

### Pattern 4: Testing Exceptions

```python
def test_raises_exception(self):
    """Test that exception is raised on invalid input."""
    from module import ClassName
    instance = ClassName()
    
    with pytest.raises(ValueError):
        instance.method_that_should_fail()
```

### Pattern 5: Parameterized Tests

```python
@pytest.mark.parametrize("input_value,expected", [
    (1, "one"),
    (2, "two"),
    (3, "three"),
])
def test_multiple_inputs(self, input_value, expected):
    """Test with multiple input values."""
    result = function_under_test(input_value)
    assert result == expected
```

---

## Debugging Tests

### View Detailed Output

```bash
pytest -vv
```

### Show Print Statements

```bash
pytest -s
```

### Run Tests in Debug Mode

```bash
pytest --pdb  # Drop into debugger on failure
```

### Show Locals on Failure

```bash
pytest -l
```

---

## Continuous Integration

Tests should be run automatically on every commit. Add to your CI pipeline:

```yaml
# Example GitHub Actions workflow
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.13'
      - run: pip install -r requirements.txt
      - run: pytest -v
```

---

## Test Dependencies

Required packages (add to `requirements.txt`):

```
pytest>=9.0.0
pytest-cov>=4.0.0
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Troubleshooting

### Issue: "ImportError: cannot import name X"

**Solution**: Make sure the module path is correct and the module exists in your workspace.

### Issue: "fixture 'X' not found"

**Solution**: Check that `conftest.py` is in the tests directory and contains the fixture.

### Issue: "TclError: no display name"

**Solution**: Tests should mock turtle graphics to avoid GUI. Ensure proper mocking is in place.

### Issue: "Class variables not resetting between tests"

**Solution**: Use the `reset_class_variables` fixture to reset state between tests.

---

## Future Enhancements

### Integration Tests to Add

1. **Full turn sequence** - Roll dice → move piece → change player
2. **Multi-piece interactions** - Multiple pieces on board simultaneously
3. **Overlap handling** - Piece capturing opponent pieces
4. **Winning condition** - All 4 pieces reaching home

### System Tests to Add

1. **Complete game playthrough** - From start to finish
2. **Performance tests** - Board rendering speed
3. **UI responsiveness** - Click handling and animation
4. **Edge case scenarios** - All pieces blocked, etc.

---

## Contributing

When adding new features to Dice-Turtle:

1. **Write tests first** (TDD approach recommended)
2. **Maintain >80% coverage** for new code
3. **Run full test suite** before committing
4. **Update this documentation** if adding new test patterns

---

## Contact & Support

For questions about the test suite:
- Review existing tests in `tests/unit/` for examples
- Check `conftest.py` for available fixtures
- Refer to [pytest documentation](https://docs.pytest.org/)

---

**Last Updated**: December 28, 2025
