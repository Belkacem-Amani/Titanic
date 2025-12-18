import unittest 
import pandas as pd
from src.module1 import survival_by_gender


class TestModule1(unittest.TestCase):

    def test_survival_by_gender(self):
        data = {
            'Sex': [0, 1, 0, 1],
            'Survived': [0, 1, 1, 1]
        }
        df = pd.DataFrame(data)
        result = survival_by_gender(df)
        self.assertTrue(result[1] > result[0])


if __name__ == '__main__':
    unittest.main()
