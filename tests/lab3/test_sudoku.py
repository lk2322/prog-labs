import unittest

from src.lab3 import sudoku


class SudokuTestCase(unittest.TestCase):
    def test_get_row(self):
        grid = sudoku.read_sudoku('puzzle1.txt')
        self.assertEqual(sudoku.get_row(grid, (0, 0)), ['5', '3', '.', '.', '7', '.', '.', '.', '.'])
        self.assertEqual(sudoku.get_row(grid, (4, 0)), ['4', '.', '.', '8', '.', '3', '.', '.', '1'])
        self.assertEqual(sudoku.get_row(grid, (8, 0)), ['.', '.', '.', '.', '8', '.', '.', '7', '9'])

    def test_get_col(self):
        grid = sudoku.read_sudoku('puzzle1.txt')
        self.assertEqual(sudoku.get_col(grid, (0, 0)), ['5', '6', '.', '8', '4', '7', '.', '.', '.'])
        self.assertEqual(sudoku.get_col(grid, (0, 4)), ['7', '9', '.', '6', '.', '2', '.', '1', '8'])
        self.assertEqual(sudoku.get_col(grid, (0, 8)), ['.', '.', '.', '3', '1', '6', '.', '5', '9'])

    def test_get_block(self):
        grid = sudoku.read_sudoku('puzzle1.txt')
        self.assertEqual(sudoku.get_block(grid, (0, 0)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(sudoku.get_block(grid, (0, 4)), ['.', '7', '.', '1', '9', '5', '.', '.', '.'])
        self.assertEqual(sudoku.get_block(grid, (4, 0)), ['8', '.', '.', '4', '.', '.', '7', '.', '.'])
        self.assertEqual(sudoku.get_block(grid, (8, 0)), ['.', '6', '.', '.', '.', '.', '.', '.', '.'])

    def test_find_empty_positions(self):
        grid = sudoku.read_sudoku('puzzle1.txt')
        self.assertEqual(sudoku.find_empty_positions(grid), (0, 2))
        grid[0][2] = '1'
        self.assertEqual(sudoku.find_empty_positions(grid), (0, 3))
        grid[0][3] = '1'
        self.assertEqual(sudoku.find_empty_positions(grid), (0, 5))

    def test_find_possible_values(self):
        grid = sudoku.read_sudoku('puzzle1.txt')
        self.assertEqual(sudoku.find_possible_values(grid, (0, 2)), {'1', '2', '4'})
        self.assertEqual(sudoku.find_possible_values(grid, (4, 0)), {'2', '9'})
        self.assertEqual(sudoku.find_possible_values(grid, (8, 0)), {'1', '2', '3'})

    def test_solve(self):
        grid = sudoku.read_sudoku('puzzle1.txt')
        sudoku.solve(grid)
        self.assertEqual(grid, [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
                                ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                                ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
                                ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                                ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
                                ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                                ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
                                ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                                ['3', '4', '5', '2', '8', '6', '1', '7', '9']])

        grid = sudoku.read_sudoku('puzzle2.txt')
        sudoku.solve(grid)
        self.assertEqual(grid, [['7', '9', '4', '5', '8', '2', '1', '3', '6'],
                                ['2', '6', '8', '9', '3', '1', '7', '4', '5'],
                                ['3', '1', '5', '4', '7', '6', '9', '8', '2'],
                                ['6', '8', '9', '7', '1', '5', '3', '2', '4'],
                                ['4', '3', '2', '8', '6', '9', '5', '7', '1'],
                                ['1', '5', '7', '2', '4', '3', '8', '6', '9'],
                                ['8', '2', '1', '6', '5', '7', '4', '9', '3'],
                                ['9', '4', '3', '1', '2', '8', '6', '5', '7'],
                                ['5', '7', '6', '3', '9', '4', '2', '1', '8']])
    def test_check_solution(self):
        grid = sudoku.read_sudoku('puzzle1.txt')
        sudoku.solve(grid)
        self.assertTrue(sudoku.check_solution(grid))
        grid[0][0] = '3'
        self.assertFalse(sudoku.check_solution(grid))
        grid = sudoku.read_sudoku('puzzle2.txt')
        sudoku.solve(grid)
        self.assertTrue(sudoku.check_solution(grid))
        grid[0][0] = '3'
        self.assertFalse(sudoku.check_solution(grid))
        grid = sudoku.read_sudoku('puzzle3.txt')
        sudoku.solve(grid)
        self.assertTrue(sudoku.check_solution(grid))
        grid[0][0] = '3'
        self.assertFalse(sudoku.check_solution(grid))

    def test_generate_sudoku(self):
        grid = sudoku.generate_sudoku(40)
        expected_unknown = 41
        actual_unknown = sum(1 for row in grid for e in row if e == ".")
        self.assertEqual(expected_unknown, actual_unknown)
        solution = sudoku.solve(grid)
        solved = sudoku.check_solution(solution)
        self.assertTrue(solved)

        grid = sudoku.generate_sudoku(1000)
        expected_unknown = 0
        actual_unknown = sum(1 for row in grid for e in row if e == ".")
        self.assertEqual(expected_unknown, actual_unknown)
        solution = sudoku.solve(grid)
        solved = sudoku.check_solution(solution)
        self.assertTrue(solved)

        grid = sudoku.generate_sudoku(0)
        expected_unknown = 81
        actual_unknown = sum(1 for row in grid for e in row if e == ".")
        self.assertEqual(expected_unknown, actual_unknown)
        solution = sudoku.solve(grid)
        solved = sudoku.check_solution(solution)
        self.assertTrue(solved)

