import truth
import pytest

class TestTruth:

    def test_basics(self):
        assert truth.truthiness(1)
        assert truth.truthiness(True)
        assert truth.truthiness('True')

        assert not truth.truthiness(0)
        assert not truth.truthiness(False)
        assert not truth.truthiness('False')

    def test_actually_bool(self):
        import sys
        print sys.path
        assert True is truth.truthiness(1)

    def test_empty_string(self):
        pytest.raises(StandardError, 
                      truth.truthiness, '')

