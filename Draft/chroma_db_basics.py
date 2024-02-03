import chromadb

chroma_client = chromadb.Client()

collections = chroma_client.create_collection(name="my_collection")

collections.add(
    documents=["my name is Byron, but not Harry", "my name is not Byron, but Harry"],  # The documents we have
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],  # The metadata for the documents
    ids=["id1", "id2"]  # Unique id for each document
)

results = collections.query(
    query_texts=["what is my name"],    # The question to be queried
    n_results=1     # Number of top documents
)

print(results)
