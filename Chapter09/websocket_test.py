from httpx_ws.transport import ASGIWebSocketTransport
import pytest_asyncio
from asgi_lifespan import LifespanManager

@pytest_asyncio.fixture
async def test_client():
    async with LifespanManager(app):