from abc import ABC, abstractmethod
from typing import Tuple, Any, Dict
import numpy as np
import os

class BaseReader(ABC):
    @abstractmethod
    def read(self, path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
        """
        Reads the file at path and returns the data as a numpy array and a metadata dictionary.
        """
        pass

    @classmethod
    def can_read(cls, path: str) -> bool:
        """
        Returns True if this reader can read the file at path.
        Default implementation checks extensions.
        """
        return any(path.lower().endswith(ext) for ext in cls.supported_extensions())

    @classmethod
    @abstractmethod
    def supported_extensions(cls) -> Tuple[str, ...]:
        """
        Returns a tuple of supported file extensions (e.g., ('.tif', '.tiff')).
        """
        pass
