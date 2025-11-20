from typing import Tuple, Any, Dict
import numpy as np
import nd2
from .base import BaseReader

class Nd2Reader(BaseReader):
    def read(self, path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
        with nd2.ND2File(path) as f:
            data = f.asarray()
            metadata = {
                'shape': f.shape,
                'dtype': str(f.dtype),
                'ndim': f.ndim,
                'sizes': f.sizes,
                'metadata': f.metadata, # This might be a complex object, but useful
                'text_info': f.text_info,
                'experiment': f.experiment
            }
            return data, metadata

    @classmethod
    def supported_extensions(cls) -> Tuple[str, ...]:
        return ('.nd2',)
