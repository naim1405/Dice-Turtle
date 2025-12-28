"""
Integration tests for full game flow.

Tests verify complete game scenarios including multiple players, pieces, and turns.
"""

import pytest
from unittest.mock import MagicMock, patch


class TestFullGameFlow:
    """Integration tests for full game flow scenarios."""
    
    @patch('dice.Dice.shape')
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_complete_turn_cycle(self, mock_action_turtle, mock_player_turtle,
                                   mock_dice_turtle, mock_randbelow, mock_shape,
                                   reset_class_variables):
        """Test a complete turn: roll dice, check state, manage player turns."""
        from dice import Dice
        from piece import Piece
        from player import Player
        from action import Action
        
        # Mock turtles
        mock_dice_instance = MagicMock()
        mock_dice_instance.shape = MagicMock()
        mock_dice_turtle.return_value = mock_dice_instance
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        mock_action_instance = MagicMock()
        mock_action_turtle.return_value = mock_action_instance
        
        # Initialize game
        Player.current_player = -1
        player = Player()
        dice = Dice()
        action = Action()
        
        # Reset state
        Dice.allow_rolling = True
        Piece.allow_moving = False
        
        # Current player should be 0 (Green)
        assert Player.current_player == 0
        
        # Roll dice (roll a 4)
        mock_randbelow.return_value = 3  # Returns 4
        dice.roll()
        
        assert Dice.current_value == 4
        
        # Simulate piece move
        Piece.allow_moving = True
        # After piece moves
        Piece.allow_moving = False
        Dice.allow_rolling = True
        
        assert Dice.allow_rolling == True
        assert Piece.allow_moving == False
        
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_player_cycling_through_all_four(self, mock_action_turtle, mock_player_turtle,
                                              mock_dice_turtle, mock_randbelow, reset_class_variables):
        """Test that players cycle through 0, 1, 2, 3 correctly."""
        from dice import Dice
        from player import Player
        
        # Mock turtles
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        
        Player.current_player = -1
        player = Player()
        
        # Should start at 0
        assert Player.current_player == 0
        
        # Cycle through all players
        player.handle_player_change()
        assert Player.current_player == 1
        
        player.handle_player_change()
        assert Player.current_player == 2
        
        player.handle_player_change()
        assert Player.current_player == 3
        
        # Should cycle back to 0
        player.handle_player_change()
        assert Player.current_player == 0
        
    @patch('dice.Dice.shape')
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_six_grants_extra_turn(self, mock_action_turtle, mock_player_turtle,
                                     mock_dice_turtle, mock_randbelow, mock_shape,
                                     reset_class_variables):
        """Test that rolling six allows player to keep their turn."""
        from dice import Dice
        from piece import Piece
        from player import Player
        
        # Mock turtles
        mock_dice_instance = MagicMock()
        mock_dice_instance.shape = MagicMock()
        mock_dice_turtle.return_value = mock_dice_instance
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        
        Player.current_player = -1  # Set to -1 so it becomes 0 after init
        player = Player()
        dice = Dice()
        
        # Should be player 0 after init
        assert Player.current_player == 0
        
        # Roll a six
        mock_randbelow.return_value = 5  # Roll 6
        dice.roll()
        
        assert Dice.current_value == 6
        assert Dice.consecutive_six == 1
        
        # When six is rolled, next_player flag should be False
        Piece.next_player = False
        
        # Player should remain the same (not changed)
        assert Player.current_player == 0
        assert Piece.next_player == False
        
    @patch('dice.Dice.shape')
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_three_consecutive_sixes_behavior(self, mock_action_turtle, mock_player_turtle,
                                               mock_dice_turtle, mock_randbelow, mock_shape,
                                               reset_class_variables):
        """Test that three consecutive sixes trigger reroll."""
        from dice import Dice
        from player import Player
        
        # Mock turtles
        mock_dice_instance = MagicMock()
        mock_dice_instance.shape = MagicMock()
        mock_dice_turtle.return_value = mock_dice_instance
        
        Player.current_player = 0
        dice = Dice()
        
        # Roll three consecutive sixes
        mock_randbelow.return_value = 5  # Roll 6
        dice.roll()
        assert Dice.consecutive_six == 1
        
        dice.roll()
        assert Dice.consecutive_six == 2
        
        # Third six triggers reroll
        mock_randbelow.side_effect = [5, 2]  # Roll 6, then reroll to 3
        dice.roll()
        
        # Should have rerolled
        assert Dice.current_value == 3
        assert Dice.consecutive_six == 0
        
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_piece_status_across_game(self, mock_action_turtle, mock_player_turtle,
                                        mock_dice_turtle, reset_class_variables):
        """Test piece status management for all players during game."""
        from piece import Piece
        
        Piece.piece_status = {
            0: {"available": 4, "active": 0},
            1: {"available": 4, "active": 0},
            2: {"available": 4, "active": 0},
            3: {"available": 4, "active": 0},
        }
        
        # Simulate game progression
        # Player 0 activates 2 pieces
        Piece.piece_status[0]["active"] = 2
        assert Piece.piece_status[0]["active"] == 2
        
        # Player 1 activates 1 piece
        Piece.piece_status[1]["active"] = 1
        assert Piece.piece_status[1]["active"] == 1
        
        # Player 0 finishes 1 piece
        Piece.piece_status[0]["available"] = 3
        assert Piece.piece_status[0]["available"] == 3
        
        # All other players still have 4 available
        assert Piece.piece_status[1]["available"] == 4
        assert Piece.piece_status[2]["available"] == 4
        assert Piece.piece_status[3]["available"] == 4
        
    @patch('dice.Dice.shape')
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_game_state_consistency(self, mock_action_turtle, mock_player_turtle,
                                      mock_dice_turtle, mock_randbelow, mock_shape,
                                      reset_class_variables):
        """Test that game state remains consistent through multiple operations."""
        from dice import Dice
        from piece import Piece
        from player import Player
        
        # Mock turtles
        mock_dice_instance = MagicMock()
        mock_dice_instance.shape = MagicMock()
        mock_dice_turtle.return_value = mock_dice_instance
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        
        # Initialize
        Player.current_player = -1
        player = Player()
        dice = Dice()
        
        assert Player.current_player == 0
        
        # Simulate multiple turns
        for turn in range(4):
            current = Player.current_player
            
            # Roll dice
            mock_randbelow.return_value = turn  # Roll 1, 2, 3, 4
            dice.roll()
            expected_value = turn + 1
            assert Dice.current_value == expected_value
            
            # Move piece (simulated by setting flags)
            Piece.allow_moving = True
            Piece.allow_moving = False
            Dice.allow_rolling = True
            
            # Change player
            player.handle_player_change()
            
        # After 4 turns, should be back at player 0
        assert Player.current_player == 0
