from snorkel.labeling.model import LabelModel
from snorkel.labeling import PandasLFApplier
from typing import Dict, Any
import logging
from labeling_function_lib.labeling_function_lib import LabelingFunctionLib
from pandas import DataFrame


class ModelTrainer:
    DEFAULT_N_EPOCHS = 500

    def __init__(self, config: Dict[str, Any] | None = None) -> None:
        self.config = config or {}
        self.logger = logging.getLogger(self.__class__.__name__)

    def train(
            self,
            data: DataFrame,
            lf_lib: LabelingFunctionLib,
            cardinality: int
        ) -> LabelModel:
        """
        Trains a LabelModel using the provided data and labeling function library.

        Args:
            data (DataFrame): The input data for training.
            lf_lib (LabelingFunctionLib): The labeling function library.
            cardinality (int): The cardinality of the label space.

        Returns:
            LabelModel: The trained LabelModel.
        """
        self.logger.info("Applying labeling functions...")

        applier = PandasLFApplier(lfs=lf_lib.get_all())
        L_train = applier.apply(data)
        model = LabelModel(cardinality=cardinality)
        n_epochs = self.config.get('n_epochs', self.DEFAULT_N_EPOCHS)

        self.logger.info(f"Training label model for {n_epochs}...")

        model.fit(L_train=L_train,n_epochs=n_epochs)

        self.logger.info("Training completed.")

        return model
