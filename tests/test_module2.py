import unittest
import pandas as pd
from src.module2 import save_to_sqlite, load_from_db

class TestModule2(unittest.TestCase):

    def test_save_and_load(self):
        # Create a simple DataFrame
        data = {
            'Name': ['Alice', 'Bob'],
            'Survived': [1, 0],
            'Pclass': [1, 2]
        }
        df = pd.DataFrame(data)

        # Save to SQLite
        save_to_sqlite(df)

        # Load from SQLite
        loaded_df = load_from_db()

        # Test that loaded data matches original data
        pd.testing.assert_frame_equal(df, loaded_df)

if __name__ == '__main__':
    unittest.main()
