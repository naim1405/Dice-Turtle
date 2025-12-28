"""
Unit tests for the Player module.

Tests cover player initialization, turn management, and player cycling.
"""

import pytest
from unittest.mock import MagicMock, patch, call


@patch('player.Turtle.__init__', return_value=None)
@patch('player.Turtle.penup')
@patch('player.Turtle.hideturtle')
@patch('player.Turtle.speed')
@patch('player.Turtle.clear')
@patch('player.Turtle.goto')
@patch('player.Turtle.color')
@patch('player.Turtle.write')
@patch('player.Turtle.forward')
class TestPlayerInitialization:
    """Test suite for Player initialization."""
    
    def test_player_inherits_from_turtle(self, mock_forward, mock_write, mock_color, 
                                        mock_goto, mock_clear, mock_speed, 
                                        mock_hide, mock_penup, mock_init, 
                                        reset_class_variables):
        """Test that Player properly inherits from Turtle."""
        from player import Player
        player = Player()
        mock_init.assert_called_once()
        
    def test_initial_current_player(self, mock_forward, mock_write, mock_color, 
                                    mock_goto, mock_clear, mock_speed, 
                                    mock_hide, mock_penup, mock_init, 
                                    reset_class_variables):
        """Test initial current_player is -1."""
        from player import Player
        # Reset before creating instance
        Player.current_player = -1
        player = Player()
        # After initialization, current_player should be 0 (handle_player_change is called)
        assert Player.current_player == 0
        
    def test_player_color_dictionary(self, mock_forward, mock_write, mock_color, 
                                     mock_goto, mock_clear, mock_speed, 
                                     mock_hide, mock_penup, mock_init, 
                                     reset_class_variables):
        """Test player_color dictionary has correct mappings."""
        from player import Player
        expected_colors = {
            -1: "White",
            0: "Green",
            1: "Yellow",
            2: "Blue",
            3: "Red",
        }
        assert Player.player_color == expected_colors
        
    def test_turtle_hidden_during_init(self, mock_forward, mock_write, mock_color, 
                                       mock_goto, mock_clear, mock_speed, 
                                       mock_hide, mock_penup, mock_init, 
                                       reset_class_variables):
        """Test turtle is hidden during initialization."""
        from player import Player
        player = Player()
        mock_hide.assert_called()
        
    def test_penup_called(self, mock_forward, mock_write, mock_color, 
                         mock_goto, mock_clear, mock_speed, 
                         mock_hide, mock_penup, mock_init, 
                         reset_class_variables):
        """Test penup is called during initialization."""
        from player import Player
        player = Player()
        mock_penup.assert_called()


@patch('player.Turtle.__init__', return_value=None)
@patch('player.Turtle.penup')
@patch('player.Turtle.hideturtle')
@patch('player.Turtle.speed')
@patch('player.Turtle.clear')
@patch('player.Turtle.goto')
@patch('player.Turtle.color')
@patch('player.Turtle.write')
@patch('player.Turtle.forward')
class TestPlayerChange:
    """Test suite for player turn management."""
    
    def test_handle_player_change_cycles_through_players(self, mock_forward, 
                                                         mock_write, mock_color, 
                                                         mock_goto, mock_clear, 
                                                         mock_speed, mock_hide, 
                                                         mock_penup, mock_init, 
                                                         reset_class_variables):
        """Test that players cycle through 0 -> 1 -> 2 -> 3 -> 0."""
        from player import Player
        Player.current_player = -1
        player = Player()
        
        # Should be player 0 after init
        assert Player.current_player == 0
        
        player.handle_player_change()
        assert Player.current_player == 1
        
        player.handle_player_change()
        assert Player.current_player == 2
        
        player.handle_player_change()
        assert Player.current_player == 3
        
        player.handle_player_change()
        assert Player.current_player == 0  # Should wrap around
        
    def test_modulo_wrapping(self, mock_forward, mock_write, mock_color, 
                            mock_goto, mock_clear, mock_speed, 
                            mock_hide, mock_penup, mock_init, 
                            reset_class_variables):
        """Test that player wraps from 3 back to 0."""
        from player import Player
        Player.current_player = 2  # Set to 2, so __init__ will make it 3
        player = Player()  # This calls handle_player_change, making it 3
        
        player.handle_player_change()  # This should wrap to 0
        assert Player.current_player == 0
        
    def test_position_updates_on_change(self, mock_forward, mock_write, mock_color, 
                                       mock_goto, mock_clear, mock_speed, 
                                       mock_hide, mock_penup, mock_init, 
                                       reset_class_variables):
        """Test turtle position updates to (-300, 320)."""
        from player import Player
        Player.current_player = -1
        player = Player()
        
        # Check that goto was called with correct position
        goto_calls = [call(-300, 320) for call in mock_goto.call_args_list 
                     if call == ((-300, 320),)]
        assert len(goto_calls) > 0
        
    def test_screen_clears_on_change(self, mock_forward, mock_write, mock_color, 
                                    mock_goto, mock_clear, mock_speed, 
                                    mock_hide, mock_penup, mock_init, 
                                    reset_class_variables):
        """Test screen clears before writing new player."""
        from player import Player
        Player.current_player = -1
        player = Player()
        
        initial_clear_count = mock_clear.call_count
        player.handle_player_change()
        
        # Clear should be called again
        assert mock_clear.call_count > initial_clear_count
        
    def test_color_matches_player(self, mock_forward, mock_write, mock_color, 
                                  mock_goto, mock_clear, mock_speed, 
                                  mock_hide, mock_penup, mock_init, 
                                  reset_class_variables):
        """Test that color is set to match current player."""
        from player import Player
        Player.current_player = 1  # Yellow player
        player = Player()
        
        player.handle_player_change()  # Should change to player 2 (Blue)
        
        # Check that color was set to Blue
        color_calls = [str(call) for call in mock_color.call_args_list]
        has_blue = any('Blue' in call for call in color_calls)
        assert has_blue
        
    def test_writes_player_label(self, mock_forward, mock_write, mock_color, 
                                mock_goto, mock_clear, mock_speed, 
                                mock_hide, mock_penup, mock_init, 
                                reset_class_variables):
        """Test that 'Player :' label is written."""
        from player import Player
        Player.current_player = -1
        player = Player()
        
        # Check that write was called with "Player : "
        write_calls = [str(call) for call in mock_write.call_args_list]
        has_player_label = any('Player :' in call for call in write_calls)
        assert has_player_label
        
    def test_writes_color_name(self, mock_forward, mock_write, mock_color, 
                              mock_goto, mock_clear, mock_speed, 
                              mock_hide, mock_penup, mock_init, 
                              reset_class_variables):
        """Test that player color name is written."""
        from player import Player
        Player.current_player = -1
        player = Player()
        
        # After init, should write "Green"
        write_calls = [str(call) for call in mock_write.call_args_list]
        has_green = any('Green' in call for call in write_calls)
        assert has_green


@patch('player.Turtle.__init__', return_value=None)
@patch('player.Turtle.penup')
@patch('player.Turtle.hideturtle')
@patch('player.Turtle.speed')
@patch('player.Turtle.clear')
@patch('player.Turtle.goto')
@patch('player.Turtle.color')
@patch('player.Turtle.write')
@patch('player.Turtle.forward')
class TestPlayerClassVariables:
    """Test suite for Player class-level state management."""
    
    def test_class_variables_shared_across_instances(self, mock_forward, 
                                                     mock_write, mock_color, 
                                                     mock_goto, mock_clear, 
                                                     mock_speed, mock_hide, 
                                                     mock_penup, mock_init, 
                                                     reset_class_variables):
        """Test that current_player is shared between Player instances."""
        from player import Player
        Player.current_player = -1
        player1 = Player()
        player2 = Player()
        
        # Both instances should see the same current_player
        assert player1.current_player == player2.current_player
        assert Player.current_player == 1  # Both inits called handle_player_change
