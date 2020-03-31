from abc import ABC, abstractmethod
from typing import List, Tuple


class FileLoader(ABC):

    @abstractmethod
    def load_data(self, file_name: str) -> Tuple[dict, List, int]:
        pass

    @abstractmethod
    def get_default_fields(self, data_load: dict) -> dict:
        pass
