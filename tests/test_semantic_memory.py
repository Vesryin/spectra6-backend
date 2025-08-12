# tests/test_semantic_memory.py

import pytest
from app.engine.semantic_memory import SemanticMemory

def test_add_and_search_memory(test_db):
    """
    Tests that a new memory can be added to the database and then
    retrieved via a semantic search.
    """
    # Use the test database connection string
    db_conn_string = test_db.dsn
    memory_engine = SemanticMemory(db_conn_string)

    # Add some memories
    memories_to_add = [
        "The sky is blue.",
        "The grass is green.",
        "The sun is bright."
    ]
    for memory in memories_to_add:
        memory_engine.add_memory(memory)

    # Search for a similar memory
    search_query = "What color is the sky?"
    results = memory_engine.search_memory(search_query, limit=1)

    # Verify the results
    assert len(results) == 1
    assert results[0][0] == "The sky is blue."
    assert results[0][1] > 0.9  # Similarity score should be high

    memory_engine.close()
