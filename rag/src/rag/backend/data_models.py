from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from rag.backend.constants import EMBEDDING_MODEL

embedding_model = get_registry().get("cohere").create(name = EMBEDDING_MODEL)

class Article(LanceModel):
    document_name: str
    filepath: str
    content: str
    embedding: Vector(embedding_model.ndims()) = embedding_model.VectorField()
