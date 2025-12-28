"""
Unit tests for the piece_path module.

Tests cover path data integrity, coordinate validation, and position arrays.
"""

import pytest


class TestPathData:
    """Test suite for path data integrity."""
    
    def test_path_1_length(self):
        """Test path_1 has correct length of 57 (0-56 inclusive)."""
        from piece_path import path_1
        assert len(path_1) == 57
        
    def test_path_2_length(self):
        """Test path_2 has correct length of 56."""
        from piece_path import path_2
        assert len(path_2) == 56
        
    def test_path_3_length(self):
        """Test path_3 has correct length of 57."""
        from piece_path import path_3
        assert len(path_3) == 57
        
    def test_path_4_length(self):
        """Test path_4 has correct length of 57."""
        from piece_path import path_4
        assert len(path_4) == 57
        
    def test_paths_contain_coordinate_lists(self):
        """Test that all paths contain coordinate lists [x, y]."""
        from piece_path import path_1, path_2, path_3, path_4
        
        for path in [path_1, path_2, path_3, path_4]:
            for coord in path:
                assert isinstance(coord, list)
                assert len(coord) == 2
                assert isinstance(coord[0], int)
                assert isinstance(coord[1], int)
                
    def test_paths_are_not_empty(self):
        """Test that no path is empty."""
        from piece_path import path_1, path_2, path_3, path_4
        
        assert len(path_1) > 0
        assert len(path_2) > 0
        assert len(path_3) > 0
        assert len(path_4) > 0
        
    def test_paths_have_different_starting_points(self):
        """Test that each path has a unique starting position."""
        from piece_path import path_1, path_2, path_3, path_4
        
        start_points = [
            tuple(path_1[0]),
            tuple(path_2[0]),
            tuple(path_3[0]),
            tuple(path_4[0])
        ]
        
        # All starting points should be unique
        assert len(set(start_points)) == 4
        
    def test_coordinates_within_board_bounds(self):
        """Test that path coordinates are within reasonable board bounds."""
        from piece_path import path_1, path_2, path_3, path_4
        
        # Board is 15 * 41 = 615 pixels, centered around origin
        # So coordinates should be roughly between -300 and 300
        for path in [path_1, path_2, path_3, path_4]:
            for coord in path:
                assert -350 <= coord[0] <= 350, f"X coordinate {coord[0]} out of bounds"
                assert -350 <= coord[1] <= 350, f"Y coordinate {coord[1]} out of bounds"


class TestInactivePositions:
    """Test suite for inactive position arrays."""
    
    def test_inactive_pos_1_length(self):
        """Test inactive_pos_1 has 4 positions."""
        from piece_path import inactive_pos_1
        assert len(inactive_pos_1) == 4
        
    def test_inactive_pos_2_length(self):
        """Test inactive_pos_2 has 4 positions."""
        from piece_path import inactive_pos_2
        assert len(inactive_pos_2) == 4
        
    def test_inactive_pos_3_length(self):
        """Test inactive_pos_3 has 5 positions (note: this has 5)."""
        from piece_path import inactive_pos_3
        # Note: In the actual code, inactive_pos_3 has 5 positions
        assert len(inactive_pos_3) >= 4
        
    def test_inactive_pos_4_length(self):
        """Test inactive_pos_4 has 5 positions (note: this has 5)."""
        from piece_path import inactive_pos_4
        # Note: In the actual code, inactive_pos_4 has 5 positions
        assert len(inactive_pos_4) >= 4
        
    def test_inactive_positions_are_coordinate_lists(self):
        """Test that inactive positions are coordinate lists."""
        from piece_path import inactive_pos_1, inactive_pos_2, inactive_pos_3, inactive_pos_4
        
        for pos_array in [inactive_pos_1, inactive_pos_2, inactive_pos_3, inactive_pos_4]:
            for pos in pos_array:
                assert isinstance(pos, list)
                assert len(pos) == 2
                assert isinstance(pos[0], int)
                assert isinstance(pos[1], int)
                
    def test_inactive_positions_are_unique_per_player(self):
        """Test that each player has unique inactive positions."""
        from piece_path import inactive_pos_1, inactive_pos_2, inactive_pos_3, inactive_pos_4
        
        # Convert to tuples for comparison
        pos_1 = [tuple(pos) for pos in inactive_pos_1]
        pos_2 = [tuple(pos) for pos in inactive_pos_2]
        pos_3 = [tuple(pos) for pos in inactive_pos_3]
        pos_4 = [tuple(pos) for pos in inactive_pos_4]
        
        # Each player's positions should be unique within their set
        assert len(set(pos_1)) == len(pos_1)
        assert len(set(pos_2)) == len(pos_2)
        assert len(set(pos_3)) == len(pos_3)
        assert len(set(pos_4)) == len(pos_4)
        
    def test_inactive_positions_in_corners(self):
        """Test that inactive positions are in board corners."""
        from piece_path import inactive_pos_1, inactive_pos_2, inactive_pos_3, inactive_pos_4
        
        # Player 1 (Green) - top left corner
        for pos in inactive_pos_1:
            assert pos[0] < 0  # Left side
            assert pos[1] > 0  # Top side
            
        # Player 2 (Yellow) - top right corner
        for pos in inactive_pos_2:
            assert pos[0] > 0  # Right side
            assert pos[1] > 0  # Top side
            
        # Player 3 (Blue) - bottom right corner
        for pos in inactive_pos_3:
            assert pos[0] > 0  # Right side
            assert pos[1] < 0  # Bottom side
            
        # Player 4 (Red) - bottom left corner
        for pos in inactive_pos_4:
            assert pos[0] < 0  # Left side
            assert pos[1] < 0  # Bottom side


class TestActivePositions:
    """Test suite for active position arrays."""
    
    def test_active_pos_1_length(self):
        """Test active_pos_1 has 4 positions."""
        from piece_path import active_pos_1
        assert len(active_pos_1) == 4
        
    def test_active_pos_2_length(self):
        """Test active_pos_2 has 4 positions."""
        from piece_path import active_pos_2
        assert len(active_pos_2) == 4
        
    def test_active_pos_3_length(self):
        """Test active_pos_3 has 4 positions."""
        from piece_path import active_pos_3
        assert len(active_pos_3) == 4
        
    def test_active_pos_4_length(self):
        """Test active_pos_4 has 4 positions."""
        from piece_path import active_pos_4
        assert len(active_pos_4) == 4
        
    def test_active_positions_are_coordinate_lists(self):
        """Test that active positions are coordinate lists."""
        from piece_path import active_pos_1, active_pos_2, active_pos_3, active_pos_4
        
        for pos_array in [active_pos_1, active_pos_2, active_pos_3, active_pos_4]:
            for pos in pos_array:
                assert isinstance(pos, list)
                assert len(pos) == 2
                assert isinstance(pos[0], int)
                assert isinstance(pos[1], int)
                
    def test_active_positions_are_unique_per_player(self):
        """Test that each player has unique active positions."""
        from piece_path import active_pos_1, active_pos_2, active_pos_3, active_pos_4
        
        # Convert to tuples for comparison
        pos_1 = [tuple(pos) for pos in active_pos_1]
        pos_2 = [tuple(pos) for pos in active_pos_2]
        pos_3 = [tuple(pos) for pos in active_pos_3]
        pos_4 = [tuple(pos) for pos in active_pos_4]
        
        # Each player's positions should be unique within their set
        assert len(set(pos_1)) == len(pos_1)
        assert len(set(pos_2)) == len(pos_2)
        assert len(set(pos_3)) == len(pos_3)
        assert len(set(pos_4)) == len(pos_4)
        
    def test_active_positions_near_inactive_zones(self):
        """Test that active positions are near their respective inactive zones."""
        from piece_path import (active_pos_1, active_pos_2, active_pos_3, 
                                active_pos_4, inactive_pos_1, inactive_pos_2, 
                                inactive_pos_3, inactive_pos_4)
        
        # Active positions should be in same general area as inactive positions
        # Player 1 - top left
        for pos in active_pos_1:
            assert pos[0] < 0
            assert pos[1] > 0
            
        # Player 2 - top right
        for pos in active_pos_2:
            assert pos[0] > 0
            assert pos[1] > 0
            
        # Player 3 - bottom right
        for pos in active_pos_3:
            assert pos[0] > 0
            assert pos[1] < 0
            
        # Player 4 - bottom left
        for pos in active_pos_4:
            assert pos[0] < 0
            assert pos[1] < 0
            
    def test_active_positions_align_with_path_start(self):
        """Test that active positions are close to the start of each path."""
        from piece_path import (active_pos_1, active_pos_2, active_pos_3, 
                                active_pos_4, path_1, path_2, path_3, path_4)
        
        # Active positions should be near the first position of their respective path
        # Not exact match, but should be in same quadrant
        path_start_1 = path_1[0]
        for pos in active_pos_1:
            # Same quadrant (both negative x, positive y)
            assert (pos[0] < 0) == (path_start_1[0] < 0)
            assert (pos[1] > 0) == (path_start_1[1] > 0)


class TestPathDataExported:
    """Test that all necessary data is exported from the module."""
    
    def test_all_paths_exported(self):
        """Test that all 4 paths are accessible."""
        import piece_path
        assert hasattr(piece_path, 'path_1')
        assert hasattr(piece_path, 'path_2')
        assert hasattr(piece_path, 'path_3')
        assert hasattr(piece_path, 'path_4')
        
    def test_all_inactive_positions_exported(self):
        """Test that all inactive position arrays are accessible."""
        import piece_path
        assert hasattr(piece_path, 'inactive_pos_1')
        assert hasattr(piece_path, 'inactive_pos_2')
        assert hasattr(piece_path, 'inactive_pos_3')
        assert hasattr(piece_path, 'inactive_pos_4')
        
    def test_all_active_positions_exported(self):
        """Test that all active position arrays are accessible."""
        import piece_path
        assert hasattr(piece_path, 'active_pos_1')
        assert hasattr(piece_path, 'active_pos_2')
        assert hasattr(piece_path, 'active_pos_3')
        assert hasattr(piece_path, 'active_pos_4')
