import pytest


@pytest.fixture
def test_mask_card() -> int:
    """Вывод номера карты для теста"""

    return 7777888811119999


@pytest.fixture
def no_number_string() -> str:
    """Вывод номера карты с буквами для теста"""

    return "aoao0987lologggg"


@pytest.fixture
def test_mask_account() -> int:
    """Вывод номера аккаунта для теста"""

    return 73654108430135874305
