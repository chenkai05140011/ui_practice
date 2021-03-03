import pytest

test_data = [("3+5", 8), ("2+4", 6), ("6*9", 55)]
@pytest.mark.skip("zhus")
@pytest.mark.parametrize("test_input,expect", [("3+5", 8), ("2+4", 6), ("6*9", 55)])

def test_demo(test_input,expect):
    assert eval(test_input) == expect