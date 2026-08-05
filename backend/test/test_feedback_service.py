# from fastapi.testclient import TestClient
import pytest

# from ..app.main import app
# client = TestClient(app)


@pytest.mark.asyncio
async def test_chat_service() -> None:
    from ..app.providers.fake_provider import FakeLLMProvider
    service = FakeLLMProvider()
    result = await service.generate("Explan Docker")
    assert result  == "Fake response"
