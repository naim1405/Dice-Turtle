"""
Unit tests for the Dice module.

Tests cover dice initialization, rolling mechanics, consecutive six handling,
and state management.
"""

import pytest
from unittest.mock import MagicMock, patch
import sys


@patch('dice.Turtle.__init__', return_value=None)
@patch('dice.Turtle.penup')
@patch('dice.Turtle.hideturtle')
@patch('dice.Turtle.goto')
@patch('dice.Turtle.showturtle')
@patch('dice.Turtle.shape')
class TestDiceInitialization:
    """Test suite for Dice initialization."""
    
    def test_dice_inherits_from_turtle(self, mock_shape, mock_show, mock_goto, 
                                       mock_hide, mock_penup, mock_init):
        """Test that Dice properly inherits from Turtle."""
        from dice import Dice
        dice = Dice()
        mock_init.assert_called_once()
        
    def test_initial_position(self, mock_shape, mock_show, mock_goto, 
                             mock_hide, mock_penup, mock_init):
        """Test dice is positioned at (8, 335)."""
        from dice import Dice
        dice = Dice()
        mock_goto.assert_called_once_with(8, 335)
        
    def test_initial_values(self, mock_shape, mock_show, mock_goto, 
                           mock_hide, mock_penup, mock_init, reset_class_variables):
        """Test initial class variables are set correctly."""
        from dice import Dice
        assert Dice.prev_value == 0
        assert Dice.current_value == 0
        assert Dice.consecutive_six == 0
        assert Dice.allow_rolling == True
        
    def test_penup_called(self, mock_shape, mock_show, mock_goto, 
                         mock_hide, mock_penup, mock_init):
        """Test penup is called during initialization."""
        from dice import Dice
        dice = Dice()
        mock_penup.assert_called_once()
        
    def test_turtle_hidden_then_shown(self, mock_shape, mock_show, mock_goto, 
                                      mock_hide, mock_penup, mock_init):
        """Test turtle is hidden then shown during initialization."""
        from dice import Dice
        dice = Dice()
        mock_hide.assert_called_once()
        mock_show.assert_called_once()


@patch('dice.Turtle.__init__', return_value=None)
@patch('dice.Turtle.penup')
@patch('dice.Turtle.hideturtle')
@patch('dice.Turtle.goto')
@patch('dice.Turtle.showturtle')
@patch('dice.Turtle.shape')
class TestDiceRolling:
    """Test suite for dice rolling mechanics."""
    
    def test_roll_generates_value_in_range(self, mock_shape, mock_show, mock_goto, 
                                          mock_hide, mock_penup, mock_init, 
                                          reset_class_variables):
        """Test roll generates a value between 1 and 6."""
        from dice import Dice
        dice = Dice()
        
        # Roll multiple times to test randomness
        for _ in range(20):
            dice.roll()
            assert 1 <= Dice.current_value <= 6
            
    def test_roll_updates_current_value(self, mock_shape, mock_show, mock_goto, 
                                        mock_hide, mock_penup, mock_init, 
                                        mock_dice_roll, reset_class_variables):
        """Test that rolling updates current_value."""
        from dice import Dice
        dice = Dice()
        mock_dice_roll(4)
        dice.roll()
        assert Dice.current_value == 4
        
    def test_roll_stores_previous_value(self, mock_shape, mock_show, mock_goto, 
                                        mock_hide, mock_penup, mock_init, 
                                        mock_dice_roll, reset_class_variables):
        """Test that prev_value stores the previous roll."""
        from dice import Dice
        dice = Dice()
        mock_dice_roll(3)
        dice.roll()
        assert Dice.current_value == 3
        
        mock_dice_roll(5)
        dice.roll()
        assert Dice.prev_value == 3
        assert Dice.current_value == 5
        
    def test_consecutive_six_increments(self, mock_shape, mock_show, mock_goto, 
                                       mock_hide, mock_penup, mock_init, 
                                       mock_dice_roll, reset_class_variables):
        """Test consecutive six counter increments when rolling 6."""
        from dice import Dice
        dice = Dice()
        mock_dice_roll(6)
        
        dice.roll()
        assert Dice.consecutive_six == 1
        
        dice.roll()
        assert Dice.consecutive_six == 2
        
    def test_consecutive_six_resets_on_non_six(self, mock_shape, mock_show, mock_goto, 
                                               mock_hide, mock_penup, mock_init, 
                                               mock_dice_roll, reset_class_variables):
        """Test consecutive six counter resets when rolling non-6."""
        from dice import Dice
        dice = Dice()
        mock_dice_roll(6)
        dice.roll()
        assert Dice.consecutive_six == 1
        
        mock_dice_roll(3)
        dice.roll()
        assert Dice.consecutive_six == 0
        
    def test_three_consecutive_sixes_triggers_reroll(self, mock_shape, mock_show, 
                                                     mock_goto, mock_hide, mock_penup, 
                                                     mock_init, reset_class_variables):
        """Test that three consecutive 6s triggers a re-roll."""
        from dice import Dice
        dice = Dice()
        
        with patch('dice.secrets.randbelow') as mock_random:
            # First three rolls return 6, fourth returns 4
            mock_random.side_effect = [5, 5, 5, 3]  # randbelow returns 0-5, so 5 = dice 6
            
            dice.roll()
            dice.roll()
            dice.roll()  # This should trigger re-roll
            
            # Should have rolled 4 times (3 sixes + 1 reroll)
            assert mock_random.call_count == 4
            # After rerolling a non-6, consecutive_six resets to 0
            assert Dice.consecutive_six == 0
            
    def test_shape_changes_after_roll(self, mock_shape, mock_show, mock_goto, 
                                     mock_hide, mock_penup, mock_init, 
                                     mock_dice_roll, reset_class_variables):
        """Test that dice shape updates to match rolled value."""
        from dice import Dice
        dice = Dice()
        mock_dice_roll(4)
        dice.roll()
        
        # Check that shape was called with correct dice image
        calls = [call for call in mock_shape.call_args_list 
                if 'dice_4.gif' in str(call)]
        assert len(calls) > 0


@patch('dice.Turtle.__init__', return_value=None)
@patch('dice.Turtle.penup')
@patch('dice.Turtle.hideturtle')
@patch('dice.Turtle.goto')
@patch('dice.Turtle.showturtle')
@patch('dice.Turtle.shape')
class TestDiceClassVariables:
    """Test suite for Dice class-level state management."""
    
    def test_class_variables_shared_across_instances(self, mock_shape, mock_show, 
                                                     mock_goto, mock_hide, mock_penup, 
                                                     mock_init, mock_dice_roll, 
                                                     reset_class_variables):
        """Test that class variables are shared between Dice instances."""
        from dice import Dice
        dice1 = Dice()
        dice2 = Dice()
        
        mock_dice_roll(6)
        dice1.roll()
        
        # Both instances should see the same current_value
        assert dice1.current_value == 6
        assert dice2.current_value == 6
        assert Dice.current_value == 6
        
    def test_allow_rolling_flag(self, mock_shape, mock_show, mock_goto, 
                                mock_hide, mock_penup, mock_init, 
                                reset_class_variables):
        """Test allow_rolling flag is accessible."""
        from dice import Dice
        dice = Dice()
        assert hasattr(Dice, 'allow_rolling')
        assert Dice.allow_rolling == True
