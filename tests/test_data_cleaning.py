from nbresult import ChallengeResultTestCase


class TestDataCleaning(ChallengeResultTestCase):
    def test_columns_reduced(self):
        self.assertLess(
            self.result.df_cols,
            75,
            f"Expected < 75 columns after dropping high-missing columns, got {self.result.df_cols}")

    def test_id_column_dropped(self):
        self.assertFalse(
            self.result.has_id_column,
            "Id column should be dropped")

    def test_X_and_y_defined(self):
        self.assertGreater(self.result.X_cols, 0, "X not defined properly")
        self.assertGreater(self.result.y_length, 0, "y not defined properly")
