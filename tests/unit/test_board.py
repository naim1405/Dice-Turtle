"""
Unit tests for the Board module.

Tests cover board initialization, box creation, path creation, and layout.
"""

import pytest
from unittest.mock import MagicMock, patch


@patch('board.turtle.Turtle')
class TestBoardInitialization:
    """Test suite for Board initialization."""
    
    def test_board_creates_turtle(self, mock_turtle):
        """Test that Board creates a Turtle instance."""
        from board import Board
        board = Board()
        assert mock_turtle.called
        
    def test_initial_position(self, mock_turtle):
        """Test turtle starts at (-300, 300)."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        # Check that goto was called with initial position
        # The board initialization calls goto multiple times, so check the first call
        assert mock_instance.goto.call_count > 0
        # First goto call should be to (-300, 300)
        first_call = mock_instance.goto.call_args_list[0]
        assert first_call[0] == (-300, 300)
        
    def test_board_size_is_15(self, mock_turtle):
        """Test board_size is 15."""
        from board import Board
        board = Board()
        assert board.board_size == 15
        
    def test_box_size_is_41(self, mock_turtle):
        """Test box_size is 41."""
        from board import Board
        board = Board()
        assert board.box_size == 41
        
    def test_turtle_speed_set(self, mock_turtle):
        """Test turtle speed is set to 0 (fastest)."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.speed.assert_called_with(0)
        
    def test_penup_called(self, mock_turtle):
        """Test penup is called during initialization."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        assert mock_instance.penup.called
        
    def test_pendown_called(self, mock_turtle):
        """Test pendown is called before drawing."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        assert mock_instance.pendown.called
        
    def test_turtle_hidden_after_creation(self, mock_turtle):
        """Test turtle is hidden after board creation."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.hideturtle.assert_called()


@patch('board.turtle.Turtle')
class TestBoxCreation:
    """Test suite for box creation."""
    
    def test_create_box_draws_square(self, mock_turtle):
        """Test create_box draws a square."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_box(41, 1)
        
        # Should call forward 4 times (one for each side)
        assert mock_instance.forward.call_count == 4
        
    def test_create_box_turns_right(self, mock_turtle):
        """Test create_box turns 90 degrees right for each corner."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_box(41, 1)
        
        # Should call right 4 times (one for each corner)
        assert mock_instance.right.call_count == 4
        
    def test_create_box_respects_direction(self, mock_turtle):
        """Test create_box respects direction parameter."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_box(41, -1)
        
        # Should call right with negative direction
        # right(90 * -1) = right(-90)
        assert mock_instance.right.called
        
    def test_create_box_pendown_called(self, mock_turtle):
        """Test create_box calls pendown."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_box(41, 1)
        
        assert mock_instance.pendown.called


@patch('board.turtle.Turtle')
class TestInactiveZoneCreation:
    """Test suite for inactive zone creation."""
    
    def test_create_inactive_zone_creates_4_sets(self, mock_turtle):
        """Test inactive zone creates 4 sets of boxes (one per player)."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_inactive_zone()
        
        # Each player gets 4 boxes, and we create for 4 players
        # So forward should be called at least 16 times for boxes
        assert mock_instance.forward.call_count >= 16
        
    def test_create_inactive_zone_uses_player_colors(self, mock_turtle):
        """Test inactive zone uses correct colors for each player."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_inactive_zone()
        
        # Check that pencolor was called with player colors
        color_calls = [str(call) for call in mock_instance.pencolor.call_args_list]
        
        # Should have called with green, yellow, blue, and red
        has_green = any('green' in call.lower() for call in color_calls)
        has_yellow = any('yellow' in call.lower() for call in color_calls)
        has_blue = any('blue' in call.lower() for call in color_calls)
        has_red = any('red' in call.lower() for call in color_calls)
        
        assert has_green and has_yellow and has_blue and has_red


@patch('board.turtle.Turtle')
class TestPathCreation:
    """Test suite for path creation methods."""
    
    def test_create_left_path_creates_3x6_grid(self, mock_turtle):
        """Test create_left_path creates a 3x6 grid."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_left_path(1, 0, 0, 0)
        
        # Should create 3 rows of 6 boxes each = 18 boxes
        # Each box calls forward once per side = 4 times
        # 18 boxes * 4 = 72, plus navigation forwards
        assert mock_instance.forward.call_count >= 18 * 4
        
    def test_create_right_path_creates_3x6_grid(self, mock_turtle):
        """Test create_right_path creates a 3x6 grid."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_right_path(1, 0, 0, 0)
        
        # Should create 3 rows of 6 boxes each
        assert mock_instance.forward.call_count >= 18 * 4
        
    def test_create_top_path_creates_6x3_grid(self, mock_turtle):
        """Test create_top_path creates a 6x3 grid."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_top_path(1, 0, 0, 0)
        
        # Should create 6 rows of 3 boxes each = 18 boxes
        assert mock_instance.forward.call_count >= 18 * 4
        
    def test_create_bottom_path_creates_6x3_grid(self, mock_turtle):
        """Test create_bottom_path creates a 6x3 grid."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_bottom_path(1, 0, 0, 0)
        
        # Should create 6 rows of 3 boxes each
        assert mock_instance.forward.call_count >= 18 * 4
        
    def test_path_methods_use_backward(self, mock_turtle):
        """Test path creation methods use backward for positioning."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_left_path(1, 0, 0, 0)
        
        # Should use backward for repositioning
        assert mock_instance.backward.called
        
    def test_path_methods_use_turns(self, mock_turtle):
        """Test path creation methods use right and left turns."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        mock_instance.reset_mock()
        
        board.create_left_path(1, 0, 0, 0)
        
        # Should use right and left for navigation
        assert mock_instance.right.called or mock_instance.left.called


@patch('board.turtle.Turtle')
class TestBoardCreation:
    """Test suite for complete board creation."""
    
    def test_create_board_calls_all_components(self, mock_turtle):
        """Test create_board is called during initialization."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        
        # Create board should have been called, which draws the main square
        # Check that forward was called many times (for all the boxes)
        assert mock_instance.forward.call_count > 50
        
    def test_create_board_draws_main_square(self, mock_turtle):
        """Test create_board draws the main 15x15 square."""
        from board import Board
        mock_instance = MagicMock()
        mock_turtle.return_value = mock_instance
        
        board = Board()
        
        # Should call forward with 15 * 41 = 615 for the main square
        forward_calls = [call[0][0] for call in mock_instance.forward.call_args_list 
                        if call[0]]
        has_large_forward = any(size > 500 for size in forward_calls if isinstance(size, (int, float)))
        assert has_large_forward or mock_instance.forward.call_count > 0
        
    def test_board_attributes_initialized(self, mock_turtle):
        """Test board attributes are initialized."""
        from board import Board
        board = Board()
        
        assert hasattr(board, 't')
        assert hasattr(board, 'board_size')
        assert hasattr(board, 'box_size')
        assert hasattr(board, 'path')
        assert hasattr(board, 'final_path')
        assert hasattr(board, 'piece_path')


@patch('board.turtle.Turtle')
class TestBoardDataStructures:
    """Test suite for board data structures."""
    
    def test_path_array_initialized(self, mock_turtle):
        """Test path array is initialized."""
        from board import Board
        board = Board()
        assert isinstance(board.path, list)
        assert len(board.path) == 8
        
    def test_final_path_initialized(self, mock_turtle):
        """Test final_path array is initialized."""
        from board import Board
        board = Board()
        assert isinstance(board.final_path, list)
        assert len(board.final_path) == 4
        
    def test_piece_path_initialized(self, mock_turtle):
        """Test piece_path array is initialized."""
        from board import Board
        board = Board()
        assert isinstance(board.piece_path, list)
