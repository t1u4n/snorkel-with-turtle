from embedding.base_embedding_system import BaseEmbeddingSystem
import tensorflow_hub as hub
from numpy import array

class USEEmbeddingSystem(BaseEmbeddingSystem):
    def __init__(
        self,
        model_url: str = "https://www.kaggle.com/models/google/universal-sentence-encoder/frameworks/TensorFlow2/variations/universal-sentence-encoder/versions/2"
    ) -> None:
        super().__init__()
        self.encoder = hub.load(model_url)
        self.logger.info("USE Lite model loaded successfully.")

    def preprocess(self, text: str) -> str:
        """
        Preprocesses the input text.

        Args:
            text (str): The input text to be preprocessed.

        Returns:
            str: The preprocessed text.
        """
        return text

    def embed(self, text: str) -> array:
        """
        Embeds the given text using the embedding system.

        Args:
            text (str): The input text to be embedded.

        Returns:
            array: The embeddings of the input text.
        """
        return self.encoder(self.preprocess(text))[0]