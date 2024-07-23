import pytest

from fastapi_app.embeddings import compute_text_embedding
from fastapi_app.openai_clients import create_openai_embed_client
from tests.data import test_data


@pytest.mark.asyncio
async def test_compute_text_embedding(mock_default_azure_credential, mock_openai_embedding):
    openai_embed_client = await create_openai_embed_client(mock_default_azure_credential)
    result = await compute_text_embedding(
        q="test",
        openai_client=openai_embed_client,
        embed_model="text-embedding-ada-002",
        embed_deployment="text-embedding-ada-002",
        embedding_dimensions=1536,
    )
    assert result == test_data.embeddings
