import pytest

@pytest.fixture(scope="class")
def prepare_emoji():
    print("^-^", '\n')
    yield
    print(":3", '\n')
# 2 смайлика (но 1 раз выполнится, yield передаст управление всем использующим)

@pytest.fixture()
def very_important():
    print(":)", '\n')
# 1 смайлик

@pytest.fixture(autouse=True)
def print_smile():
    print(":-p", '\n')
# 2 смайлика

class TestPrintEmoji():
    def test_first(self, prepare_emoji, very_important):
        print("first test")

    def test_second(self, prepare_emoji):
        print("second test")

