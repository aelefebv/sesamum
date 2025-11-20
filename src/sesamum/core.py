from typing import Tuple, Any, Dict, List, Type
import os
import numpy as np

from .readers.base import BaseReader
from .readers.tiff import TiffReader
from .readers.lsm import LsmReader
from .readers.nd2 import Nd2Reader

# Registry of available readers
READERS: List[Type[BaseReader]] = [
    TiffReader,
    LsmReader,
    Nd2Reader,
]

def read(path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
    """
    Reads a microscopy file and returns the image data and metadata.
    
    Args:
        path: Path to the file to read.
        
    Returns:
        Tuple containing:
            - numpy.ndarray: The image data.
            - dict: Metadata associated with the image.
            
    Raises:
        ValueError: If the file format is not supported or file does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    for reader_cls in READERS:
        if reader_cls.can_read(path):
            reader = reader_cls()
            return reader.read(path)
            
    raise ValueError(f"Unsupported file format for file: {path}")
