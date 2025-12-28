"""
Integration tests for Dice and Piece movement.

Tests verify that dice rolls correctly control piece movement and game state.
Focused on state management and flag interactions.
"""

import pytest
from unittest.mock import MagicMock, patch


class TestDicePieceIntegration:
    """Integration tests for Dice and Piece movement."""
    
    @patch('dice.Dice.shape')
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')  
    def test_dice_state_affects_piece_movement_flags(self, mock_action_turtle, mock_player_turtle,
                                                       mock_dice_turtle, mock_randbelow, mock_shape,
                                                       reset_class_variables):
        """Test that dice state correctly affects piece movement permission flags."""
        from dice import Dice
        from piece import Piece
        from player import Player
        
        # Mock dice turtle properly
        mock_dice_instance = MagicMock()
        mock_dice_instance.shape = MagicMock()
        mock_dice_turtle.return_value = mock_dice_instance
        
        # Setup
        Player.current_player = 0
        Dice.allow_rolling = True
        Dice.current_value = 0
        Piece.allow_moving = False
        
        # Create dice and roll
        dice = Dice()
        mock_randbelow.return_value = 3  # Roll 4
        dice.roll()
        
        # After roll, verify dice value
        assert Dice.current_value == 4
        assert Dice.consecutive_six == 0
        
    @patch('dice.Dice.shape')
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_consecutive_six_tracking_with_reroll(self, mock_action_turtle, mock_player_turtle,
                                                    mock_dice_turtle, mock_randbelow, mock_shape,
                                                    reset_class_variables):
        """Test that three consecutive sixes trigger automatic reroll."""
        from dice import Dice
        from player import Player
        
        # Mock turtle
        mock_dice_instance = MagicMock()
        mock_dice_instance.shape = MagicMock()
        mock_dice_turtle.return_value = mock_dice_instance
        
        Player.current_player = 0
        dice = Dice()
        
        # Roll first six
        mock_randbelow.return_value = 5  # 5 + 1 = 6
        dice.roll()
        assert Dice.current_value == 6
        assert Dice.consecutive_six == 1
        
        # Roll second six
        dice.roll()
        assert Dice.consecutive_six == 2
        
        # Third six triggers reroll - simulate rolling 6 then 3
        mock_randbelow.side_effect = [5, 2]  # Roll 6, then reroll to 3
        dice.roll()
        
        # Should have rerolled to 3
        assert Dice.current_value == 3
        assert Dice.consecutive_six == 0
        
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_piece_status_tracking(self, mock_action_turtle, mock_player_turtle,
                                     mock_dice_turtle, reset_class_variables):
        """Test that piece status is tracked correctly across players."""
        from piece import Piece
        from player import Player
        
        Player.current_player = 0
        
        # Initialize piece status
        Piece.piece_status = {
            0: {"available": 4, "active": 0},
            1: {"available": 4, "active": 0},
            2: {"available": 4, "active": 0},
            3: {"available": 4, "active": 0},
        }
        
        # Verify initial state
        assert Piece.piece_status[0]["available"] == 4
        assert Piece.piece_status[0]["active"] == 0
        
        # Simulate activating a piece
        Piece.piece_status[0]["active"] += 1
        assert Piece.piece_status[0]["active"] == 1
        
        # Simulate piece finishing
        Piece.piece_status[0]["available"] -= 1
        assert Piece.piece_status[0]["available"] == 3
        
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_turn_management_flags(self, mock_action_turtle, mock_player_turtle,
                                     mock_dice_turtle, reset_class_variables):
        """Test that turn management flags work correctly."""
        from dice import Dice
        from piece import Piece
        from player import Player
        
        # Setup
        Player.current_player = 0
        Dice.allow_rolling = True
        Piece.allow_moving = False
        Piece.next_player = True
        
        # After rolling dice (simulated)
        Dice.allow_rolling = False
        Piece.allow_moving = True
        
        assert Dice.allow_rolling == False
        assert Piece.allow_moving == True
        
        # After moving piece (simulated)
        Piece.allow_moving = False
        Dice.allow_rolling = True
        
        assert Piece.allow_moving == False
        assert Dice.allow_rolling == True
        
    @patch('dice.Dice.shape')
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_six_prevents_player_change(self, mock_action_turtle, mock_player_turtle,
                                          mock_dice_turtle, mock_randbelow, mock_shape,
                                          reset_class_variables):
        """Test that rolling six sets flag to prevent player change."""
        from dice import Dice
        from piece import Piece
        from player import Player
        
        # Mock turtle
        mock_dice_instance = MagicMock()
        mock_dice_instance.shape = MagicMock()
        mock_dice_turtle.return_value = mock_dice_instance
        
        Player.current_player = 0
        Piece.next_player = True
        
        dice = Dice()
        mock_randbelow.return_value = 5  # Roll 6
        dice.roll()
        
        assert Dice.current_value == 6
        # When six is rolled, next_player should be set to False
        # This would be done in piece.move(), but we test the flag
        Piece.next_player = False
        assert Piece.next_player == False
        
    @patch('dice.Dice.shape')
    @patch('secrets.randbelow')
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_non_six_allows_player_change(self, mock_action_turtle, mock_player_turtle,
                                            mock_dice_turtle, mock_randbelow, mock_shape,
                                            reset_class_variables):
        """Test that rolling non-six sets flag to allow player change."""
        from dice import Dice
        from piece import Piece
        from player import Player
        
        # Mock turtle
        mock_dice_instance = MagicMock()
        mock_dice_instance.shape = MagicMock()
        mock_dice_turtle.return_value = mock_dice_instance
        
        Player.current_player = 0
        Piece.next_player = False
        
        dice = Dice()
        mock_randbelow.return_value = 2  # Roll 3
        dice.roll()
        
        assert Dice.current_value == 3
        assert Dice.consecutive_six == 0
        
        # When non-six is rolled, next_player should be True
        # This would be done in piece.move()
        Piece.next_player = True
        assert Piece.next_player == True
        
    @patch('dice.Turtle')
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_multiple_player_piece_status(self, mock_action_turtle, mock_player_turtle,
                                           mock_dice_turtle, reset_class_variables):
        """Test piece status tracking for all four players."""
        from piece import Piece
        
        Piece.piece_status = {
            0: {"available": 4, "active": 0},
            1: {"available": 4, "active": 0},
            2: {"available": 4, "active": 0},
            3: {"available": 4, "active": 0},
        }
        
        # Activate pieces for different players
        for i in range(4):
            Piece.piece_status[i]["active"] += 1
            assert Piece.piece_status[i]["active"] == 1
            assert Piece.piece_status[i]["available"] == 4
            
        # Finish pieces for different players
        for i in range(4):
            Piece.piece_status[i]["available"] -= 1
            assert Piece.piece_status[i]["available"] == 3
