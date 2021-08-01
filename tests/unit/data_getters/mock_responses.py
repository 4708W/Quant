import pytest
import responses


@pytest.fixture
def mock_responses() -> responses.RequestsMock:
    with responses.RequestsMock() as res:
        yield res
