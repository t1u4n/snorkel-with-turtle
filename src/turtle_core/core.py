from alert.alert_system import AlertSystem
from drift_detector.base_drift_detector import BaseDriftDetector
from embedding.base_embedding_system import BaseEmbeddingSystem
from ingestor_interface.base_ingestor import BaseIngestor
from labeling_function_lib.labeling_function_lib import LabelingFunctionLib
from loader_interface.base_loader import BaseLoader
from model_trainer.model_trainer import ModelTrainer
import logging


class Core:
    def __init__(self) -> None:
        self.alert_sys: AlertSystem = None
        self.drift_detector: BaseDriftDetector = None
        self.embedding: BaseEmbeddingSystem = None
        self.ingestor: BaseIngestor = None
        self.labeling_function_lib: LabelingFunctionLib = None
        self.loader: BaseLoader = None
        self.model_trainer: ModelTrainer = None
        self.logger = logging.getLogger(self.__class__.__name__)


class CoreBuilder:
    def __init__(self) -> None:
        self.core = Core()

    def with_alert_system(self, alert_system: AlertSystem) -> None:
        self.core.alert_sys = alert_system

    def with_drift_detector(self, drift_detector: BaseDriftDetector) -> None:
        self.core.drift_detector = drift_detector

    def with_embedding(self, embedding: BaseEmbeddingSystem) -> None:
        self.core.embedding = embedding
    
    def with_ingestor(self, ingestor: BaseIngestor) -> None:
        self.core.ingestor = ingestor
    
    def with_labeling_function_lib(self, lf_lib: LabelingFunctionLib) -> None:
        self.core.labeling_function_lib = lf_lib

    def with_loader(self, loader: BaseLoader) -> None:
        self.core.loader = loader

    def with_model_trainer(self, model_trainer: ModelTrainer) -> None:
        self.core.model_trainer = model_trainer

    def build(self) -> Core:
        return self.core
    
