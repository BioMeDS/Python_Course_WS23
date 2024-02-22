import unittest
from pyboy import PyBoy
from fake_ct import current_tetromino

class TestCurrentTetromino(unittest.TestCase):

    def setUp(self):
        self.pyboy = PyBoy("Tetris.gb", game_wrapper=True)
        self.pyboy.set_emulation_speed(0)
        self.tetris = self.pyboy.game_wrapper()
        self.tetris.start_game(timer_div=0x00)
    
    def test_tetromino_0(self):
        self.tetris.reset_game(timer_div=0)
        ct = current_tetromino(self.tetris)
        self.assertEqual(ct, "J")

    def test_tetrominos_1_to_9(self):
        expectation = "IOZSTOJIO"
        for i,t in enumerate(expectation):
            self.tetris.reset_game(timer_div=i+1)
            self.assertEqual(current_tetromino(self.tetris), t)

    def test_tetrominos_L(self):
        expectation = "L"
        self.tetris.reset_game(timer_div=227)
        self.assertEqual(current_tetromino(self.tetris), expectation)
        
if __name__ == '__main__':
    unittest.main()