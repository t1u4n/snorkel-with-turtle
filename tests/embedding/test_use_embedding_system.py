from embedding.use_embedding_system import USEEmbeddingSystem
import pytest
import logging

def test_process():
    try:
        embedding_system = USEEmbeddingSystem()
        embedded = embedding_system.embed(["This is a sample sentence."])
        logging.info(f"embedded: {embedded}")
    except Exception as e:
        pytest.fail(f"test_process() raised an exception {e}")
