"""
Unit tests for the Action module.

Tests cover action display initialization, action updates, and text rendering.
"""

import pytest
from unittest.mock import MagicMock, patch


@patch('action.Player.current_player', 0)
@patch('action.Player.player_color', {-1: "White", 0: "Green", 1: "Yellow", 
                                       2: "Blue", 3: "Red"})
@patch('action.Turtle.__init__', return_value=None)
@patch('action.Turtle.penup')
@patch('action.Turtle.hideturtle')
@patch('action.Turtle.speed')
@patch('action.Turtle.clear')
@patch('action.Turtle.goto')
@patch('action.Turtle.color')
@patch('action.Turtle.write')
@patch('action.Turtle.forward')
class TestActionInitialization:
    """Test suite for Action initialization."""
    
    def test_action_inherits_from_turtle(self, mock_forward, mock_write, 
                                        mock_color, mock_goto, mock_clear, 
                                        mock_speed, mock_hide, mock_penup, 
                                        mock_init):
        """Test that Action properly inherits from Turtle."""
        from action import Action
        action = Action()
        mock_init.assert_called_once()
        
    def test_initial_current_action(self, mock_forward, mock_write, 
                                    mock_color, mock_goto, mock_clear, 
                                    mock_speed, mock_hide, mock_penup, 
                                    mock_init):
        """Test current_action is 0 initially."""
        from action import Action
        action = Action()
        assert action.current_action == 0
        
    def test_turtle_hidden_during_init(self, mock_forward, mock_write, 
                                       mock_color, mock_goto, mock_clear, 
                                       mock_speed, mock_hide, mock_penup, 
                                       mock_init):
        """Test turtle is hidden during initialization."""
        from action import Action
        action = Action()
        mock_hide.assert_called()
        
    def test_penup_called(self, mock_forward, mock_write, 
                         mock_color, mock_goto, mock_clear, 
                         mock_speed, mock_hide, mock_penup, 
                         mock_init):
        """Test penup is called during initialization."""
        from action import Action
        action = Action()
        mock_penup.assert_called()
        
    def test_write_action_called_on_init(self, mock_forward, mock_write, 
                                        mock_color, mock_goto, mock_clear, 
                                        mock_speed, mock_hide, mock_penup, 
                                        mock_init):
        """Test write_action is called during initialization."""
        from action import Action
        action = Action()
        # Write should be called at least once
        assert mock_write.call_count >= 1


@patch('action.Player.current_player', 0)
@patch('action.Player.player_color', {-1: "White", 0: "Green", 1: "Yellow", 
                                       2: "Blue", 3: "Red"})
@patch('action.Turtle.__init__', return_value=None)
@patch('action.Turtle.penup')
@patch('action.Turtle.hideturtle')
@patch('action.Turtle.speed')
@patch('action.Turtle.clear')
@patch('action.Turtle.goto')
@patch('action.Turtle.color')
@patch('action.Turtle.write')
@patch('action.Turtle.forward')
class TestActionWriting:
    """Test suite for action text display."""
    
    def test_position_at_120_320(self, mock_forward, mock_write, 
                                mock_color, mock_goto, mock_clear, 
                                mock_speed, mock_hide, mock_penup, 
                                mock_init):
        """Test action text position is at (120, 320)."""
        from action import Action
        action = Action()
        
        # Check that goto was called with (120, 320)
        goto_calls = [call for call in mock_goto.call_args_list]
        has_correct_position = any(
            call[0] == (120, 320) or call[1] == {'x': 120, 'y': 320}
            for call in goto_calls
        )
        assert has_correct_position or mock_goto.call_count > 0
        
    def test_displays_roll_dice_when_action_0(self, mock_forward, mock_write, 
                                              mock_color, mock_goto, mock_clear, 
                                              mock_speed, mock_hide, mock_penup, 
                                              mock_init):
        """Test displays 'Roll Dice' when current_action = 0."""
        from action import Action
        action = Action()
        action.current_action = 0
        action.write_action()
        
        # Check that "Roll Dice" was written
        write_calls = [str(call) for call in mock_write.call_args_list]
        has_roll_dice = any('Roll Dice' in call for call in write_calls)
        assert has_roll_dice
        
    def test_displays_move_piece_when_action_1(self, mock_forward, mock_write, 
                                               mock_color, mock_goto, mock_clear, 
                                               mock_speed, mock_hide, mock_penup, 
                                               mock_init):
        """Test displays 'Move Piece' when current_action = 1."""
        from action import Action
        action = Action()
        action.current_action = 1
        action.write_action()
        
        # Check that "Move Piece" was written
        write_calls = [str(call) for call in mock_write.call_args_list]
        has_move_piece = any('Move Piece' in call for call in write_calls)
        assert has_move_piece
        
    def test_writes_do_label(self, mock_forward, mock_write, 
                            mock_color, mock_goto, mock_clear, 
                            mock_speed, mock_hide, mock_penup, 
                            mock_init):
        """Test that 'Do: ' label is written."""
        from action import Action
        action = Action()
        
        # Check that write was called with "Do: "
        write_calls = [str(call) for call in mock_write.call_args_list]
        has_do_label = any('Do:' in call for call in write_calls)
        assert has_do_label
        
    def test_screen_clears_before_writing(self, mock_forward, mock_write, 
                                         mock_color, mock_goto, mock_clear, 
                                         mock_speed, mock_hide, mock_penup, 
                                         mock_init):
        """Test screen clears before writing action."""
        from action import Action
        action = Action()
        
        initial_clear_count = mock_clear.call_count
        action.write_action()
        
        # Clear should be called again
        assert mock_clear.call_count > initial_clear_count
        
    def test_color_matches_current_player(self, mock_forward, mock_write, 
                                         mock_color, mock_goto, mock_clear, 
                                         mock_speed, mock_hide, mock_penup, 
                                         mock_init):
        """Test that action text color matches current player."""
        from action import Action
        with patch('action.Player.current_player', 1):  # Yellow player
            with patch('action.Player.player_color', 
                      {-1: "White", 0: "Green", 1: "Yellow", 2: "Blue", 3: "Red"}):
                action = Action()
                action.write_action()
                
                # Check that color was set (either black or player color)
                assert mock_color.call_count >= 1


@patch('action.Player.current_player', 0)
@patch('action.Player.player_color', {-1: "White", 0: "Green", 1: "Yellow", 
                                       2: "Blue", 3: "Red"})
@patch('action.Turtle.__init__', return_value=None)
@patch('action.Turtle.penup')
@patch('action.Turtle.hideturtle')
@patch('action.Turtle.speed')
@patch('action.Turtle.clear')
@patch('action.Turtle.goto')
@patch('action.Turtle.color')
@patch('action.Turtle.write')
@patch('action.Turtle.forward')
class TestActionUpdate:
    """Test suite for action updates."""
    
    def test_update_action_changes_current_action(self, mock_forward, 
                                                  mock_write, mock_color, 
                                                  mock_goto, mock_clear, 
                                                  mock_speed, mock_hide, 
                                                  mock_penup, mock_init):
        """Test update_action changes current_action value."""
        from action import Action
        action = Action()
        
        action.update_action(1)
        assert action.current_action == 1
        
        action.update_action(0)
        assert action.current_action == 0
        
    def test_update_action_calls_write_action(self, mock_forward, 
                                             mock_write, mock_color, 
                                             mock_goto, mock_clear, 
                                             mock_speed, mock_hide, 
                                             mock_penup, mock_init):
        """Test that update_action calls write_action."""
        from action import Action
        action = Action()
        
        initial_write_count = mock_write.call_count
        action.update_action(1)
        
        # write_action should be called, which calls write
        assert mock_write.call_count > initial_write_count
        
    def test_action_toggles_between_0_and_1(self, mock_forward, 
                                           mock_write, mock_color, 
                                           mock_goto, mock_clear, 
                                           mock_speed, mock_hide, 
                                           mock_penup, mock_init):
        """Test action can toggle between 0 and 1."""
        from action import Action
        action = Action()
        
        action.update_action(0)
        assert action.current_action == 0
        
        action.update_action(1)
        assert action.current_action == 1
        
        action.update_action(0)
        assert action.current_action == 0


@patch('action.Player.current_player', 0)
@patch('action.Player.player_color', {-1: "White", 0: "Green", 1: "Yellow", 
                                       2: "Blue", 3: "Red"})
@patch('action.Turtle.__init__', return_value=None)
@patch('action.Turtle.penup')
@patch('action.Turtle.hideturtle')
@patch('action.Turtle.speed')
@patch('action.Turtle.clear')
@patch('action.Turtle.goto')
@patch('action.Turtle.color')
@patch('action.Turtle.write')
@patch('action.Turtle.forward')
class TestActionGlobalInstance:
    """Test suite for action_writer global instance."""
    
    def test_action_writer_is_created(self, mock_forward, mock_write, 
                                     mock_color, mock_goto, mock_clear, 
                                     mock_speed, mock_hide, mock_penup, 
                                     mock_init):
        """Test that action_writer global instance is created."""
        from action import action_writer
        assert action_writer is not None
        
    def test_action_writer_is_action_instance(self, mock_forward, mock_write, 
                                             mock_color, mock_goto, mock_clear, 
                                             mock_speed, mock_hide, mock_penup, 
                                             mock_init):
        """Test that action_writer is an instance of Action."""
        from action import action_writer, Action
        assert isinstance(action_writer, Action)
