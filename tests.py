import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 1)

        board1 = [
            ['O', None, 'X'],
            [None, 'O', None],
            [None, 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board1), 2)

        board3 = [
            ['O', 'X', 'X'],
            ['O', 'O', None],
            [None, 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board3), None)

    # TODO: Test all functions from logic.py!
    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')


if __name__ == '__main__':
    unittest.main()
    board = TestLogic() 
    print (logic.make_empty_board())
    print (logic.get_winner(board))