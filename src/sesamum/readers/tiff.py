from typing import Tuple, Any, Dict
import numpy as np
import tifffile
from .base import BaseReader

class TiffReader(BaseReader):
    def read(self, path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
        with tifffile.TiffFile(path) as tif:
            data = tif.asarray()
            # Basic metadata extraction
            metadata = {}
            if tif.pages:
                page = tif.pages[0]
                metadata['shape'] = data.shape
                metadata['dtype'] = str(data.dtype)
                metadata['axes'] = tif.series[0].axes if tif.series else 'UNKNOWN'
                # Extract some common tags if available
                for tag in ['ImageWidth', 'ImageLength', 'BitsPerSample', 'Compression']:
                    if tag in page.tags:
                        metadata[tag] = page.tags[tag].value
            
            return data, metadata

    @classmethod
    def supported_extensions(cls) -> Tuple[str, ...]:
        return ('.tif', '.tiff')
