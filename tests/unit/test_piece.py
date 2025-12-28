"""
Unit tests for the Piece module.

Tests cover piece initialization, movement, activation, and game logic.
"""

import pytest
from unittest.mock import MagicMock, patch, Mock


@patch('piece.Turtle.__init__', return_value=None)
@patch('piece.Turtle.shape')
@patch('piece.Turtle.pensize')
@patch('piece.Turtle.pencolor')
@patch('piece.Turtle.speed')
@patch('piece.Turtle.penup')
@patch('piece.Turtle.fillcolor')
@patch('piece.Turtle.goto')
@patch('piece.Turtle.onclick')
class TestPieceInitialization:
    """Test suite for Piece initialization."""
    
    def test_piece_inherits_from_turtle(self, mock_onclick, mock_goto, 
                                       mock_fillcolor, mock_penup, mock_speed, 
                                       mock_pencolor, mock_pensize, mock_shape, 
                                       mock_init, sample_path, sample_inactive_pos, 
                                       sample_active_pos):
        """Test that Piece properly inherits from Turtle."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        mock_init.assert_called_once()
        
    def test_player_assignment(self, mock_onclick, mock_goto, 
                              mock_fillcolor, mock_penup, mock_speed, 
                              mock_pencolor, mock_pensize, mock_shape, 
                              mock_init, sample_path, sample_inactive_pos, 
                              sample_active_pos):
        """Test that player is correctly assigned."""
        from piece import Piece
        piece = Piece(2, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        assert piece.player == 2
        
    def test_color_assignment_green(self, mock_onclick, mock_goto, 
                                   mock_fillcolor, mock_penup, mock_speed, 
                                   mock_pencolor, mock_pensize, mock_shape, 
                                   mock_init, sample_path, sample_inactive_pos, 
                                   sample_active_pos):
        """Test player 0 gets green color."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        mock_fillcolor.assert_called_with("green")
        
    def test_color_assignment_yellow(self, mock_onclick, mock_goto, 
                                    mock_fillcolor, mock_penup, mock_speed, 
                                    mock_pencolor, mock_pensize, mock_shape, 
                                    mock_init, sample_path, sample_inactive_pos, 
                                    sample_active_pos):
        """Test player 1 gets yellow color."""
        from piece import Piece
        piece = Piece(1, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        mock_fillcolor.assert_called_with("yellow")
        
    def test_color_assignment_blue(self, mock_onclick, mock_goto, 
                                  mock_fillcolor, mock_penup, mock_speed, 
                                  mock_pencolor, mock_pensize, mock_shape, 
                                  mock_init, sample_path, sample_inactive_pos, 
                                  sample_active_pos):
        """Test player 2 gets blue color."""
        from piece import Piece
        piece = Piece(2, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        mock_fillcolor.assert_called_with("blue")
        
    def test_color_assignment_red(self, mock_onclick, mock_goto, 
                                 mock_fillcolor, mock_penup, mock_speed, 
                                 mock_pencolor, mock_pensize, mock_shape, 
                                 mock_init, sample_path, sample_inactive_pos, 
                                 sample_active_pos):
        """Test player 3 gets red color."""
        from piece import Piece
        piece = Piece(3, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        mock_fillcolor.assert_called_with("red")
        
    def test_initial_position_matches_inactive(self, mock_onclick, mock_goto, 
                                              mock_fillcolor, mock_penup, mock_speed, 
                                              mock_pencolor, mock_pensize, mock_shape, 
                                              mock_init, sample_path, sample_inactive_pos, 
                                              sample_active_pos):
        """Test piece starts at inactive position."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        mock_goto.assert_called_with(sample_inactive_pos[0])
        
    def test_is_active_false_initially(self, mock_onclick, mock_goto, 
                                      mock_fillcolor, mock_penup, mock_speed, 
                                      mock_pencolor, mock_pensize, mock_shape, 
                                      mock_init, sample_path, sample_inactive_pos, 
                                      sample_active_pos):
        """Test is_active is False initially."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        assert piece.is_active == False
        
    def test_current_pos_negative_one_initially(self, mock_onclick, mock_goto, 
                                                mock_fillcolor, mock_penup, mock_speed, 
                                                mock_pencolor, mock_pensize, mock_shape, 
                                                mock_init, sample_path, sample_inactive_pos, 
                                                sample_active_pos):
        """Test current_pos is -1 initially."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        assert piece.current_pos == -1
        
    def test_path_len_is_56(self, mock_onclick, mock_goto, 
                           mock_fillcolor, mock_penup, mock_speed, 
                           mock_pencolor, mock_pensize, mock_shape, 
                           mock_init, sample_path, sample_inactive_pos, 
                           sample_active_pos):
        """Test path_len is 56."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        assert piece.path_len == 56
        
    def test_is_finished_false_initially(self, mock_onclick, mock_goto, 
                                        mock_fillcolor, mock_penup, mock_speed, 
                                        mock_pencolor, mock_pensize, mock_shape, 
                                        mock_init, sample_path, sample_inactive_pos, 
                                        sample_active_pos):
        """Test is_finished is False initially."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        assert piece.is_finished == False
        
    def test_shape_is_circle(self, mock_onclick, mock_goto, 
                            mock_fillcolor, mock_penup, mock_speed, 
                            mock_pencolor, mock_pensize, mock_shape, 
                            mock_init, sample_path, sample_inactive_pos, 
                            sample_active_pos):
        """Test piece shape is circle."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        mock_shape.assert_called_with("circle")
        
    def test_onclick_handler_registered(self, mock_onclick, mock_goto, 
                                       mock_fillcolor, mock_penup, mock_speed, 
                                       mock_pencolor, mock_pensize, mock_shape, 
                                       mock_init, sample_path, sample_inactive_pos, 
                                       sample_active_pos):
        """Test onclick handler is registered."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        assert mock_onclick.called


@patch('piece.Turtle.__init__', return_value=None)
@patch('piece.Turtle.shape')
@patch('piece.Turtle.pensize')
@patch('piece.Turtle.pencolor')
@patch('piece.Turtle.speed')
@patch('piece.Turtle.penup')
@patch('piece.Turtle.fillcolor')
@patch('piece.Turtle.goto')
@patch('piece.Turtle.onclick')
@patch('piece.Turtle.pos')
@patch('piece.Player.current_player', 0)
@patch('piece.Dice.current_value', 3)
class TestPieceMovement:
    """Test suite for piece movement when active."""
    
    def test_move_updates_position(self, mock_pos, mock_onclick, mock_goto, 
                                  mock_fillcolor, mock_penup, mock_speed, 
                                  mock_pencolor, mock_pensize, mock_shape, 
                                  mock_init, reset_class_variables):
        """Test that move updates current position."""
        from piece import Piece
        from piece_path import path_1, inactive_pos_1, active_pos_1
        
        Piece.allow_moving = True
        piece = Piece(0, path_1, inactive_pos_1[0], active_pos_1[0])
        piece.is_active = True
        piece.current_pos = 0
        mock_pos.return_value = (0, 0)
        
        with patch('piece.Dice.current_value', 3):
            with patch('piece.check_overlap'):
                piece.move()
                assert piece.current_pos == 3
                
    def test_move_only_for_current_player(self, mock_pos, mock_onclick, mock_goto, 
                                         mock_fillcolor, mock_penup, mock_speed, 
                                         mock_pencolor, mock_pensize, mock_shape, 
                                         mock_init, reset_class_variables):
        """Test piece only moves on its player's turn."""
        from piece import Piece
        from piece_path import path_1, inactive_pos_1, active_pos_1
        
        Piece.allow_moving = True
        piece = Piece(1, path_1, inactive_pos_1[0], active_pos_1[0])  # Player 1
        piece.is_active = True
        piece.current_pos = 0
        mock_pos.return_value = (0, 0)
        
        with patch('piece.Player.current_player', 0):  # But it's player 0's turn
            with patch('piece.Dice.current_value', 3):
                with patch('piece.check_overlap'):
                    old_pos = piece.current_pos
                    piece.move()
                    assert piece.current_pos == old_pos  # Should not have moved
                    
    def test_move_respects_allow_moving_flag(self, mock_pos, mock_onclick, mock_goto, 
                                            mock_fillcolor, mock_penup, mock_speed, 
                                            mock_pencolor, mock_pensize, mock_shape, 
                                            mock_init, reset_class_variables):
        """Test piece respects allow_moving flag."""
        from piece import Piece
        from piece_path import path_1, inactive_pos_1, active_pos_1
        
        Piece.allow_moving = False  # Not allowed to move
        piece = Piece(0, path_1, inactive_pos_1[0], active_pos_1[0])
        piece.is_active = True
        piece.current_pos = 0
        mock_pos.return_value = (0, 0)
        
        with patch('piece.Player.current_player', 0):
            with patch('piece.Dice.current_value', 3):
                with patch('piece.check_overlap'):
                    old_pos = piece.current_pos
                    piece.move()
                    assert piece.current_pos == old_pos
                    
    def test_move_wont_exceed_path_len(self, mock_pos, mock_onclick, mock_goto, 
                                      mock_fillcolor, mock_penup, mock_speed, 
                                      mock_pencolor, mock_pensize, mock_shape, 
                                      mock_init, reset_class_variables):
        """Test piece won't move beyond path_len."""
        from piece import Piece
        from piece_path import path_1, inactive_pos_1, active_pos_1
        
        Piece.allow_moving = True
        piece = Piece(0, path_1, inactive_pos_1[0], active_pos_1[0])
        piece.is_active = True
        piece.current_pos = 55  # Near end
        mock_pos.return_value = (0, 0)
        
        with patch('piece.Player.current_player', 0):
            with patch('piece.Dice.current_value', 6):  # Would go to 61, beyond 56
                with patch('piece.check_overlap'):
                    piece.move()
                    assert piece.current_pos == 55  # Should not move


@patch('piece.Turtle.__init__', return_value=None)
@patch('piece.Turtle.shape')
@patch('piece.Turtle.pensize')
@patch('piece.Turtle.pencolor')
@patch('piece.Turtle.speed')
@patch('piece.Turtle.penup')
@patch('piece.Turtle.fillcolor')
@patch('piece.Turtle.goto')
@patch('piece.Turtle.onclick')
class TestPieceActivation:
    """Test suite for piece activation."""
    
    def test_piece_activates_with_six(self, mock_onclick, mock_goto, 
                                     mock_fillcolor, mock_penup, mock_speed, 
                                     mock_pencolor, mock_pensize, mock_shape, 
                                     mock_init, reset_class_variables):
        """Test piece activates only with dice value 6."""
        from piece import Piece
        from piece_path import path_1, inactive_pos_1, active_pos_1
        
        piece = Piece(0, path_1, inactive_pos_1[0], active_pos_1[0])
        piece.is_active = False
        
        with patch('piece.Player.current_player', 0):
            with patch('piece.Dice.current_value', 6):
                with patch('piece.action_writer'):
                    piece.move()
                    assert piece.is_active == True
                    
    def test_piece_moves_to_active_pos_on_activation(self, mock_onclick, mock_goto, 
                                                     mock_fillcolor, mock_penup, 
                                                     mock_speed, mock_pencolor, 
                                                     mock_pensize, mock_shape, 
                                                     mock_init, reset_class_variables):
        """Test piece moves to active position when activated."""
        from piece import Piece
        from piece_path import path_1, inactive_pos_1, active_pos_1
        
        piece = Piece(0, path_1, inactive_pos_1[0], active_pos_1[0])
        piece.is_active = False
        
        with patch('piece.Player.current_player', 0):
            with patch('piece.Dice.current_value', 6):
                with patch('piece.action_writer'):
                    piece.move()
                    # Check that goto was called with active_pos
                    calls = [call[0] for call in mock_goto.call_args_list]
                    assert any(active_pos_1[0] in call for call in calls)
                    
    def test_piece_status_updates_on_activation(self, mock_onclick, mock_goto, 
                                               mock_fillcolor, mock_penup, 
                                               mock_speed, mock_pencolor, 
                                               mock_pensize, mock_shape, 
                                               mock_init, reset_class_variables):
        """Test piece_status active count increases on activation."""
        from piece import Piece
        from piece_path import path_1, inactive_pos_1, active_pos_1
        
        Piece.piece_status[0]["active"] = 0
        piece = Piece(0, path_1, inactive_pos_1[0], active_pos_1[0])
        piece.is_active = False
        
        with patch('piece.Player.current_player', 0):
            with patch('piece.Dice.current_value', 6):
                with patch('piece.action_writer'):
                    piece.move()
                    assert Piece.piece_status[0]["active"] == 1


@patch('piece.Turtle.__init__', return_value=None)
@patch('piece.Turtle.shape')
@patch('piece.Turtle.pensize')
@patch('piece.Turtle.pencolor')
@patch('piece.Turtle.speed')
@patch('piece.Turtle.penup')
@patch('piece.Turtle.fillcolor')
@patch('piece.Turtle.goto')
@patch('piece.Turtle.onclick')
class TestPieceSetInactive:
    """Test suite for set_inactive method."""
    
    def test_set_inactive_changes_is_active(self, mock_onclick, mock_goto, 
                                           mock_fillcolor, mock_penup, mock_speed, 
                                           mock_pencolor, mock_pensize, mock_shape, 
                                           mock_init, sample_path, sample_inactive_pos, 
                                           sample_active_pos):
        """Test set_inactive sets is_active to False."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        piece.is_active = True
        
        piece.set_inactive()
        assert piece.is_active == False
        
    def test_set_inactive_moves_to_inactive_pos(self, mock_onclick, mock_goto, 
                                               mock_fillcolor, mock_penup, mock_speed, 
                                               mock_pencolor, mock_pensize, mock_shape, 
                                               mock_init, sample_path, sample_inactive_pos, 
                                               sample_active_pos):
        """Test set_inactive moves piece to inactive position."""
        from piece import Piece
        piece = Piece(0, sample_path, sample_inactive_pos[0], sample_active_pos[0])
        piece.is_active = True
        
        piece.set_inactive()
        # Check that goto was called with inactive_pos
        calls = [call[0] for call in mock_goto.call_args_list]
        assert any(sample_inactive_pos[0] in call for call in calls)


class TestPieceClassVariables:
    """Test suite for Piece class-level state management."""
    
    def test_initial_piece_status(self, reset_class_variables):
        """Test initial piece_status for all players."""
        from piece import Piece
        expected_status = {
            0: {"available": 4, "active": 0},
            1: {"available": 4, "active": 0},
            2: {"available": 4, "active": 0},
            3: {"available": 4, "active": 0},
        }
        assert Piece.piece_status == expected_status
        
    def test_allow_moving_flag(self, reset_class_variables):
        """Test allow_moving flag exists."""
        from piece import Piece
        assert hasattr(Piece, 'allow_moving')
        
    def test_next_player_flag(self, reset_class_variables):
        """Test next_player flag exists."""
        from piece import Piece
        assert hasattr(Piece, 'next_player')


class TestCheckOverlap:
    """Test suite for check_overlap function."""
    
    def test_check_overlap_function_exists(self):
        """Test that check_overlap function is defined."""
        from piece import check_overlap
        assert callable(check_overlap)
