class TestMatching(unittest.TestCase):
    @patch('engine.managers.resource_manager.ResourceManager')
    def test_basic_match(self, mock_rm):
        model = LevelModel(mock_rm)
        model.grid = [[1, 1, 1], [2, 3, 4]]
        self.assertTrue(model.check_match(0, 0))
