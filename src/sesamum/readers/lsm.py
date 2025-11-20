from typing import Tuple, Any, Dict
import numpy as np
import tifffile
from .base import BaseReader

class LsmReader(BaseReader):
    def read(self, path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
        with tifffile.TiffFile(path) as tif:
            data = tif.asarray()
            metadata = {}
            
            # LSM specific metadata is often in the 'lsm_metadata' property of TiffFile if detected
            # or we can extract generic TIFF tags.
            if hasattr(tif, 'lsm_metadata'):
                 metadata['lsm'] = tif.lsm_metadata
            
            if tif.pages:
                page = tif.pages[0]
                metadata['shape'] = data.shape
                metadata['dtype'] = str(data.dtype)
                metadata['axes'] = tif.series[0].axes if tif.series else 'UNKNOWN'

            return data, metadata

    @classmethod
    def supported_extensions(cls) -> Tuple[str, ...]:
        return ('.lsm',)
