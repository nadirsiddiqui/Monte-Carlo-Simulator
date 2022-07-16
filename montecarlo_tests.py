import montecarlo
import unittest


class TestDieMethods(unittest.TestCase):
    """
    This class is designed to test the Die class.
    """
    
    def test_1_change_weight(self):
        """
        This test assures that the change weight method assigns weights correctly.
        """
        
        die1 = Die([1, 2, 3, 4, 5, 6])
        die1.change_weight(2, 5)
        actual = die1.show().weights[1] == 5.0
        expected = True
        
        self.assertEqual(actual, expected)
        
    def test_2_roll(self):
        """
        This test assures that the roll method rolls the dice the correct
        number of times.
        """
        
        die1 = Die([1, 2, 3, 4, 5, 6])
        actual = len(die1.roll(10))
        expected = 10

        self.assertEqual(actual, expected)
        
    def test_3_show(self):
        """
        This test assures that the show method properly stores and displays
        a data frame.
        """
        
        die1 = Die([1, 2, 3, 4, 5, 6])
        actual = len(die1.show())
        expected = 6
        
        self.assertEqual(actual, expected)
        
     
class TestGameMethods(unittest.TestCase):
    """
    This class is designed to test the Game class.
    """
    
    def test_1_play(self):
        """
        This test assures that the play method rolls all die the right
        number of times.
        """
        
        die1 = Die([1, 2, 3, 4, 5, 6])
        game1 = Game([die1])
        game1.play(100)
        actual = len(game1.show())
        expected = 100
        
        self.assertEqual(actual, expected)
        
            
    def test_2_show(self):
        """
        This test assures that the show method properly stores and displays
        a data frame.
        """
        
        die1 = Die([1, 2, 3, 4, 5, 6])
        game1 = Game([die1])
        game1.play(100)
        actual = len(game1.show())
        expected = 100
        
        self.assertEqual(actual, expected)

        
class TestAnalyzerMethods(unittest.TestCase):
    """
    This class is designed to test the Analyzer class.
    """
    
    def test_1_jackpot(self):
        """
        This test assures that the jackpot method stores only rolls that
        resulted in a proper jackpot.
        """
        
        die1 = Die([1, 1, 1])
        die2 = Die([1, 1, 1])
        game1 = Game([die1, die2])
        game1.play(100)
        analysis = Analyzer(game1)
        actual = analysis.jackpot()
        expected = 99
        
        self.assertEqual(actual, expected)
    
    def test_2_combo(self):
        """
        This test assures that the combo method properly stores and displays
        a data frame of combos.
        """
        
        die1 = Die([1, 2, 3, 4, 5, 6])
        die2 = Die([1, 2, 3, 4, 5, 6])
        game1 = Game([die1, die2])
        game1.play(100)
        analysis = Analyzer(game1)
        actual = sum(analysis.combo().n)
        expected = 100
        
        self.assertEqual(actual, expected)
    
    def test_3_faces(self):
        """
        This test assures that the faces method properly stores and displays
        a data frame of face counts per roll.
        """
        
        die1 = Die([1, 2, 3, 4, 5, 6])
        die2 = Die([1, 2, 3, 4, 5, 6])
        game1 = Game([die1, die2])
        game1.play(100)
        analysis = Analyzer(game1)
        actual = [len(analysis.faces().columns), len(analysis.faces())]
        expected = [6, 100]
        
        self.assertEqual(actual, expected)
    
if __name__ == '__main__':
    unittest.main(verbosity=3)