"""
Pytest configuration and shared fixtures for Dice-Turtle tests.

This module provides mock turtle graphics environment and common
fixtures used across all test modules.
"""

import pytest
from unittest.mock import MagicMock, patch
import sys
from pathlib import Path

# Add project root to Python path so tests can import modules
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def mock_turtle():
    """
    Fixture that mocks the turtle graphics module.
    Prevents actual GUI from launching during tests.
    """
    with patch('turtle.Turtle') as mock_t:
        mock_instance = MagicMock()
        mock_t.return_value = mock_instance
        yield mock_instance


@pytest.fixture
def mock_screen():
    """
    Fixture that mocks the turtle Screen.
    """
    with patch('turtle.Screen') as mock_s:
        mock_instance = MagicMock()
        mock_s.return_value = mock_instance
        yield mock_instance


@pytest.fixture
def reset_class_variables():
    """
    Fixture to reset class variables between tests.
    Use this when testing modules that use class-level state.
    """
    yield
    # Reset after test
    try:
        from dice import Dice
        Dice.prev_value = 0
        Dice.current_value = 0
        Dice.consecutive_six = 0
        Dice.allow_rolling = True
    except ImportError:
        pass
    
    try:
        from player import Player
        Player.current_player = -1
    except ImportError:
        pass
    
    try:
        from piece import Piece
        Piece.allow_moving = False
        Piece.piece_status = {
            0: {"available": 4, "active": 0},
            1: {"available": 4, "active": 0},
            2: {"available": 4, "active": 0},
            3: {"available": 4, "active": 0},
        }
        Piece.next_player = True
    except ImportError:
        pass


@pytest.fixture
def mock_dice_roll(monkeypatch):
    """
    Fixture to control dice roll results for deterministic testing.
    
    Usage:
        def test_something(mock_dice_roll):
            mock_dice_roll(6)  # Next roll will be 6
    """
    def set_roll_value(value):
        import secrets
        monkeypatch.setattr(secrets, 'randbelow', lambda x: value - 1)
    return set_roll_value


@pytest.fixture
def sample_path():
    """
    Fixture providing a sample path for testing.
    """
    return [[0, 0], [41, 0], [82, 0], [123, 0], [164, 0]]


@pytest.fixture
def sample_inactive_pos():
    """
    Fixture providing sample inactive positions.
    """
    return [[-279, 239], [-279, 197], [-279, 156], [-279, 115]]


@pytest.fixture
def sample_active_pos():
    """
    Fixture providing sample active positions.
    """
    return [[-197, 196], [-156, 196], [-156, 155], [-197, 155]]
