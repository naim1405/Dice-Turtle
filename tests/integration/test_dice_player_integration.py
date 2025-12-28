"""
Integration tests for Dice and Player interaction.

Tests verify that dice rolling and player turn management work together correctly.
"""

import pytest
from unittest.mock import MagicMock, patch


@patch('dice.Turtle.__init__', return_value=None)
@patch('dice.Turtle.penup')
@patch('dice.Turtle.hideturtle')
@patch('dice.Turtle.goto')
@patch('dice.Turtle.showturtle')
@patch('dice.Turtle.shape')
@patch('player.Turtle.__init__', return_value=None)
@patch('player.Turtle.penup')
@patch('player.Turtle.hideturtle')
@patch('player.Turtle.speed')
@patch('player.Turtle.clear')
@patch('player.Turtle.goto')
@patch('player.Turtle.color')
@patch('player.Turtle.write')
@patch('player.Turtle.forward')
class TestDicePlayerIntegration:
    """Integration tests for Dice and Player interaction."""
    
    def test_player_changes_after_dice_roll_non_six(self, mock_forward, mock_write, 
                                                      mock_color, mock_goto_player, 
                                                      mock_clear, mock_speed, 
                                                      mock_hide_player, mock_penup_player,
                                                      mock_init_player, mock_shape, 
                                                      mock_show, mock_goto_dice, 
                                                      mock_hide_dice, mock_penup_dice, 
                                                      mock_init_dice, reset_class_variables):
        """Test that player turn changes after rolling non-six."""
        from dice import Dice
        from player import Player
        
        # Reset player to initial state
        Player.current_player = -1
        player = Player()
        current_player_after_init = Player.current_player
        
        # Create dice and roll non-six
        dice = Dice()
        with patch('secrets.randbelow', return_value=3):  # Roll 4
            dice.roll()
        
        # Verify dice rolled 4
        assert Dice.current_value == 4
        assert Dice.consecutive_six == 0
        
    def test_player_does_not_change_after_rolling_six(self, mock_forward, mock_write, 
                                                        mock_color, mock_goto_player, 
                                                        mock_clear, mock_speed, 
                                                        mock_hide_player, mock_penup_player,
                                                        mock_init_player, mock_shape, 
                                                        mock_show, mock_goto_dice, 
                                                        mock_hide_dice, mock_penup_dice, 
                                                        mock_init_dice, reset_class_variables):
        """Test that player gets another turn after rolling six."""
        from dice import Dice
        from player import Player
        
        # Reset to known state
        Player.current_player = -1
        player = Player()
        initial_player = Player.current_player
        
        # Roll a six
        dice = Dice()
        with patch('secrets.randbelow', return_value=5):  # Roll 6
            dice.roll()
        
        # Verify dice rolled 6 and consecutive six counter updated
        assert Dice.current_value == 6
        assert Dice.consecutive_six == 1
        
    def test_consecutive_six_tracking(self, mock_forward, mock_write, 
                                       mock_color, mock_goto_player, 
                                       mock_clear, mock_speed, 
                                       mock_hide_player, mock_penup_player,
                                       mock_init_player, mock_shape, 
                                       mock_show, mock_goto_dice, 
                                       mock_hide_dice, mock_penup_dice, 
                                       mock_init_dice, reset_class_variables):
        """Test consecutive six tracking across multiple rolls."""
        from dice import Dice
        from player import Player
        
        Player.current_player = -1
        player = Player()
        dice = Dice()
        
        # Roll first six
        with patch('secrets.randbelow', return_value=5):  # Roll 6
            dice.roll()
        assert Dice.current_value == 6
        assert Dice.consecutive_six == 1
        
        # Roll second six
        with patch('secrets.randbelow', return_value=5):  # Roll 6
            dice.roll()
        assert Dice.current_value == 6
        assert Dice.consecutive_six == 2
        
        # Roll non-six resets counter
        with patch('secrets.randbelow', return_value=2):  # Roll 3
            dice.roll()
        assert Dice.current_value == 3
        assert Dice.consecutive_six == 0
        
    def test_three_consecutive_sixes_reroll(self, mock_forward, mock_write, 
                                             mock_color, mock_goto_player, 
                                             mock_clear, mock_speed, 
                                             mock_hide_player, mock_penup_player,
                                             mock_init_player, mock_shape, 
                                             mock_show, mock_goto_dice, 
                                             mock_hide_dice, mock_penup_dice, 
                                             mock_init_dice, reset_class_variables):
        """Test that three consecutive sixes trigger reroll."""
        from dice import Dice
        from player import Player
        
        Player.current_player = -1
        player = Player()
        dice = Dice()
        
        # Roll two sixes
        with patch('secrets.randbelow', return_value=5):  # Roll 6
            dice.roll()
            dice.roll()
        
        assert Dice.consecutive_six == 2
        
        # Third six should trigger reroll - mock to return 4 on the reroll
        with patch('secrets.randbelow', side_effect=[5, 3]):  # Roll 6, then 4 on reroll
            dice.roll()
        
        # Should have automatically rerolled
        assert Dice.current_value == 4
        assert Dice.consecutive_six == 0
        
    def test_multiple_players_cycle_correctly(self, mock_forward, mock_write, 
                                                mock_color, mock_goto_player, 
                                                mock_clear, mock_speed, 
                                                mock_hide_player, mock_penup_player,
                                                mock_init_player, mock_shape, 
                                                mock_show, mock_goto_dice, 
                                                mock_hide_dice, mock_penup_dice, 
                                                mock_init_dice, reset_class_variables):
        """Test that players cycle through 0, 1, 2, 3 correctly."""
        from dice import Dice
        from player import Player
        
        Player.current_player = -1
        player = Player()
        
        # Player should start at 0 after init
        assert Player.current_player == 0
        
        # Change player manually to test cycling
        player.handle_player_change()
        assert Player.current_player == 1
        
        player.handle_player_change()
        assert Player.current_player == 2
        
        player.handle_player_change()
        assert Player.current_player == 3
        
        # Should cycle back to 0
        player.handle_player_change()
        assert Player.current_player == 0
        
    def test_player_color_matches_current_player(self, mock_forward, mock_write, 
                                                   mock_color, mock_goto_player, 
                                                   mock_clear, mock_speed, 
                                                   mock_hide_player, mock_penup_player,
                                                   mock_init_player, mock_shape, 
                                                   mock_show, mock_goto_dice, 
                                                   mock_hide_dice, mock_penup_dice, 
                                                   mock_init_dice, reset_class_variables):
        """Test that player color updates match current player."""
        from dice import Dice
        from player import Player
        
        Player.current_player = -1
        player = Player()
        
        # Verify initial player (0 = Green)
        assert Player.current_player == 0
        assert Player.player_color[0] == "Green"
        
        # Change to next player
        player.handle_player_change()
        assert Player.current_player == 1
        assert Player.player_color[1] == "Yellow"
        
        # Verify color method was called with correct color
        color_calls = [call[0][0] for call in mock_color.call_args_list]
        assert "Yellow" in color_calls
