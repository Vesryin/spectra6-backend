from unittest.mock import MagicMock
from app.engine.semantic_memory import SemanticMemory

def test_add_and_search_memory(mocker):
    """
    Tests that a new memory can be added to the database and then
    retrieved via a semantic search.
    """
    # create a mock database connection
    mock_conn = MagicMock()
    # Configure the mock cursor to handle the 'with' statement
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.__enter__.return_value.fetchone.return_value = (1,)
    mock_cursor.__enter__.return_value.fetchall.return_value = [("The sky is blue.", 0.95)]
    
    # create the memory engine with the mock connection
    memory_engine = SemanticMemory(connection=mock_conn)

    # Add a memory
    memory_engine.add_memory("The sky is blue.")

    # Search for a similar memory
    search_query = "What color is the sky?"
    results = memory_engine.search_memory(search_query, limit=1)

    # Verify the results
    assert len(results) == 1
    assert results[0][0] == "The sky is blue."
    assert results[0][1] > 0.9  # Similarity score should be high

    memory_engine.close()
