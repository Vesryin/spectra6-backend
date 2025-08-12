# src/app/engine/semantic_memory.py

import logging
import os
import psycopg2
from pgvector.psycopg2 import register_vector
from sentence_transformers import SentenceTransformer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SemanticMemory:
    """
    Manages Spectra's semantic memory, allowing for storage and retrieval
    of text embeddings using a PostgreSQL database with the pgvector extension.
    """
    def __init__(self, db_conn_string: str):
        """
        Initializes the semantic memory engine and connects to the database.

        Args:
            db_conn_string (str): The connection string for the PostgreSQL database.
        """
        self.conn_string = db_conn_string
        self.conn = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self._connect()
        self._initialize_db()

    def _connect(self):
        """
        Establishes a connection to the PostgreSQL database.
        """
        try:
            self.conn = psycopg2.connect(self.conn_string)
            with self.conn.cursor() as cur:
                try:
                    cur.execute("CREATE EXTENSION vector;")
                    self.conn.commit()
                except psycopg2.errors.DuplicateObject:
                    self.conn.rollback()
            register_vector(self.conn)
            logging.info("Successfully connected to the database and ensured vector extension is enabled.")
        except psycopg2.OperationalError as e:
            logging.error(f"Could not connect to the database: {e}")
            raise

    def _initialize_db(self):
        """
        Initializes the database by creating the necessary extensions and tables
        if they do not already exist.
        """
        with self.conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    embedding VECTOR(384)
                );
            """)
            self.conn.commit()
            logging.info("Database initialized with 'vector' extension and 'memories' table.")

    def add_memory(self, text: str):
        """
        Adds a new memory to the database, including its text content and
        the corresponding embedding.

        Args:
            text (str): The text content of the memory to add.
        """
        embedding = self.model.encode(text)
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO memories (content, embedding) VALUES (%s, %s)", (text, embedding))
            self.conn.commit()
        logging.info(f"Added new memory: '{text}'")

    def search_memory(self, query_text: str, limit: int = 5) -> list:
        """
        Searches for memories that are semantically similar to the query text.

        Args:
            query_text (str): The text to search for.
            limit (int): The maximum number of similar memories to return.

        Returns:
            list: A list of tuples, where each tuple contains the content of a
                  similar memory and its similarity score.
        """
        query_embedding = self.model.encode(query_text)
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT content, 1 - (embedding <=> %s) AS similarity
                FROM memories
                ORDER BY similarity DESC
                LIMIT %s;
            """, (query_embedding, limit))
            results = cur.fetchall()
        logging.info(f"Found {len(results)} memories similar to '{query_text}'")
        return results

    def close(self):
        """
        Closes the database connection.
        """
        if self.conn:
            self.conn.close()
            logging.info("Database connection closed.")
