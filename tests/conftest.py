# tests/conftest.py

import pytest
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def db_connection():
    """
    Creates a connection to the test database and handles setup and teardown.
    """
    test_db_url = os.getenv("TEST_DATABASE_URL")
    if not test_db_url:
        pytest.skip("TEST_DATABASE_URL not set, skipping integration tests.")

    conn = psycopg2.connect(test_db_url)
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def test_db(db_connection):
    """
    Provides a clean database for each test function.
    """
    with db_connection.cursor() as cur:
        cur.execute("DELETE FROM memories;")
    db_connection.commit()
    return db_connection
