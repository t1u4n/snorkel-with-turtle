import logging


class AlertSystem:
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)

    def alert(self, message: str, severity: int = logging.INFO) -> None:
        self.logger.log(severity, f"ALERT: {message}")