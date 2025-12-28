"""
Integration tests for Player and Action interaction.

Tests verify that action display correctly tracks player turns and game state.
"""

import pytest
from unittest.mock import MagicMock, patch


class TestPlayerActionIntegration:
    """Integration tests for Player and Action interaction."""
    
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_action_initial_state(self, mock_action_turtle, mock_player_turtle, reset_class_variables):
        """Test that action starts with 'Roll Dice' state."""
        from player import Player
        from action import Action
        
        # Mock turtles
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        mock_action_instance = MagicMock()
        mock_action_turtle.return_value = mock_action_instance
        
        # Reset player
        Player.current_player = -1
        player = Player()
        action = Action()
        
        # Initial action should be 0 (Roll Dice)
        assert action.current_action == 0
        
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_action_updates_to_move_piece(self, mock_action_turtle, mock_player_turtle, reset_class_variables):
        """Test that action updates to 'Move Piece' after dice roll."""
        from player import Player
        from action import Action
        
        # Mock turtles
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        mock_action_instance = MagicMock()
        mock_action_turtle.return_value = mock_action_instance
        
        Player.current_player = -1
        player = Player()
        action = Action()
        
        # Update action to move piece (simulating dice roll)
        action.update_action(1)
        
        # Action should now be 1 (Move Piece)
        assert action.current_action == 1
        
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_action_resets_to_roll_dice(self, mock_action_turtle, mock_player_turtle, reset_class_variables):
        """Test that action resets to 'Roll Dice' after piece moves."""
        from player import Player
        from action import Action
        
        # Mock turtles
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        mock_action_instance = MagicMock()
        mock_action_turtle.return_value = mock_action_instance
        
        Player.current_player = -1
        player = Player()
        action = Action()
        
        # Simulate full turn
        action.update_action(1)  # Move Piece
        assert action.current_action == 1
        
        action.update_action(0)  # Roll Dice
        assert action.current_action == 0
        
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_player_action_synchronized_cycle(self, mock_action_turtle, mock_player_turtle, reset_class_variables):
        """Test that player and action stay synchronized through player cycling."""
        from player import Player
        from action import Action
        
        # Mock turtles
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        mock_action_instance = MagicMock()
        mock_action_turtle.return_value = mock_action_instance
        
        Player.current_player = -1
        player = Player()
        action = Action()
        
        # Initial state
        assert Player.current_player == 0
        assert action.current_action == 0
        
        # Simulate turn for player 0
        action.update_action(1)  # Dice rolled, move piece
        assert action.current_action == 1
        
        # Change player
        player.handle_player_change()
        action.update_action(0)  # Reset to roll dice
        
        # Player 1's turn
        assert Player.current_player == 1
        assert action.current_action == 0
        
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_action_toggles_correctly(self, mock_action_turtle, mock_player_turtle, reset_class_variables):
        """Test action correctly toggles between Roll Dice (0) and Move Piece (1)."""
        from player import Player
        from action import Action
        
        # Mock turtles
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        mock_action_instance = MagicMock()
        mock_action_turtle.return_value = mock_action_instance
        
        Player.current_player = -1
        player = Player()
        action = Action()
        
        # Start with Roll Dice
        assert action.current_action == 0
        
        # Toggle multiple times
        action.update_action(1)
        assert action.current_action == 1
        
        action.update_action(0)
        assert action.current_action == 0
        
        action.update_action(1)
        assert action.current_action == 1
        
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_player_and_action_through_full_game_cycle(self, mock_action_turtle, mock_player_turtle, reset_class_variables):
        """Test player and action synchronization through a full 4-player cycle."""
        from player import Player
        from action import Action
        
        # Mock turtles
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        mock_action_instance = MagicMock()
        mock_action_turtle.return_value = mock_action_instance
        
        Player.current_player = -1
        player = Player()
        action = Action()
        
        # Simulate full cycle for all 4 players
        for i in range(4):
            assert Player.current_player == i
            assert action.current_action == 0  # Roll Dice
            
            # Dice rolled
            action.update_action(1)
            assert action.current_action == 1  # Move Piece
            
            # Piece moved, change player
            player.handle_player_change()
            action.update_action(0)
        
        # Should be back at player 0
        assert Player.current_player == 0
        assert action.current_action == 0
        
    @patch('player.Turtle')
    @patch('action.Turtle')
    def test_player_color_consistency(self, mock_action_turtle, mock_player_turtle, reset_class_variables):
        """Test that player colors are correctly mapped."""
        from player import Player
        from action import Action
        
        # Mock turtles
        mock_player_instance = MagicMock()
        mock_player_turtle.return_value = mock_player_instance
        
        Player.current_player = -1
        player = Player()
        
        # Verify color mapping
        expected_colors = {
            -1: "White",
            0: "Green",
            1: "Yellow",
            2: "Blue",
            3: "Red"
        }
        
        for player_num, expected_color in expected_colors.items():
            assert Player.player_color[player_num] == expected_color
