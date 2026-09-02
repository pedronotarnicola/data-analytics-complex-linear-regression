from nbresult import ChallengeResultTestCase


class TestPreprocessing(ChallengeResultTestCase):
    def test_no_missing_values_after_imputation(self):
        self.assertEqual(
            self.result.missing_after_imputation,
            0,
            f"Found {self.result.missing_after_imputation} missing values after imputation")

    def test_data_scaled(self):
        self.assertLess(abs(self.result.scaled_mean), 0.5,
                        f"Scaled data mean should be close to 0, got {self.result.scaled_mean:.2f}")

    def test_preprocessed_data_ready(self):
        self.assertGreater(
            self.result.preprocessed_cols,
            50,
            f"Expected > 50 columns after preprocessing, got {self.result.preprocessed_cols}")

    def test_concatenation_no_nans(self):
        """Check concatenation didn't create NaN values from misaligned indices"""
        self.assertEqual(
            self.result.no_nans_after_concat,
            0,
            "Concatenation created NaN values! Did you reset indices with .reset_index(drop=True) before concatenating?")
