from nbresult import ChallengeResultTestCase


class TestModel(ChallengeResultTestCase):
    def test_model_better_than_baseline(self):
        self.assertLess(
            self.result.mae,
            self.result.baseline_mae,
            f"Model MAE (${self.result.mae:,.0f}) should be better than baseline (${self.result.baseline_mae:,.0f})")

    def test_predictions_are_reasonable(self):
        """Catch catastrophic prediction failures from index misalignment"""
        self.assertLess(
            self.result.mae,
            1_000_000,
            f"MAE of ${self.result.mae:,.0f} suggests index misalignment! Did you reset_index(drop=True) on y_train and y_test after train_test_split?")
