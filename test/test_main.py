import pytest
from httpx import AsyncClient, ASGITransport
from main import app

# This decorator instructs pytest to use a modern AnyIO event loop backend
@pytest.mark.anyio
async def test_read_root():
    # Wrap the FastAPI app directly into an ASGI transport layer
    transport = ASGITransport(app=app)
    
    # Instantiate native AsyncClient
    async with AsyncClient(transport=transport, base_url="http://local") as client:
        response = await client.get("/")
        
        # Assertions
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello User"}
