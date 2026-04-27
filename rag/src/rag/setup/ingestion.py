from rag.backend.constants import DATA_PATH, VECTOR_DB_PATH
import lancedb

# TODO: create a knowledge_base with an appropriate table
def setup_vector_db(path):
    vector_db = lancedb.connect(uri = path)
    vector_db.create_table("articles", schema=Article, exist_ok=True)


def ingest_docs_to_vector_db(table):
    for file in DATA_PATH.glob("*.txt"):
        with open(file) as f:
            content = f.read()

        # TODO: put the raw text or content into knowledge_base

        # print(file.name)
        # print(content)

    # print(VECTOR_DB_PATH)