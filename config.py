from pathlib import Path

BASE_DIR = Path(__file__).parent
CHROMADB_PATH = str(BASE_DIR / "chroma_db")
DOCS_PATH = str(BASE_DIR / "docs")
EMBEDDINGS_MODEL = "text-embedding-3-large"
