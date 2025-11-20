import numpy as np
import tifffile
import os
import sys
from unittest.mock import MagicMock, patch

# Add src to path
sys.path.insert(0, os.path.abspath('src'))

import sesamum

def test_tiff():
    print("Testing TIFF reader...")
    data = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
    filename = 'test.tif'
    tifffile.imwrite(filename, data)
    
    try:
        read_data, metadata = sesamum.read(filename)
        assert np.array_equal(data, read_data)
        print("TIFF data match: OK")
        print("Metadata:", metadata)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def test_nd2_mock():
    print("\nTesting ND2 reader (mocked)...")
    filename = 'test.nd2'
    # Create a dummy file just so os.path.exists passes
    with open(filename, 'w') as f:
        f.write('dummy')
        
    try:
        # Mock nd2.ND2File
        with patch('nd2.ND2File') as mock_nd2:
            mock_instance = mock_nd2.return_value
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.asarray.return_value = np.zeros((10, 10))
            mock_instance.shape = (10, 10)
            mock_instance.dtype = np.dtype('uint8')
            mock_instance.ndim = 2
            mock_instance.sizes = {'x': 10, 'y': 10}
            mock_instance.metadata = {}
            mock_instance.text_info = {}
            mock_instance.experiment = []
            
            read_data, metadata = sesamum.read(filename)
            assert read_data.shape == (10, 10)
            print("ND2 mock read: OK")
            print("Metadata:", metadata)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def test_lsm():
    print("\nTesting LSM reader...")
    # LSM is essentially a TIFF. We can write a TIFF and name it .lsm for basic verification
    # of the dispatch logic and basic read.
    data = np.random.randint(0, 255, (50, 50), dtype=np.uint8)
    filename = 'test.lsm'
    tifffile.imwrite(filename, data)
    
    try:
        read_data, metadata = sesamum.read(filename)
        assert np.array_equal(data, read_data)
        print("LSM data match: OK")
        print("Metadata:", metadata)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    try:
        test_tiff()
        test_lsm()
        test_nd2_mock()
        print("\nAll verification tests passed!")
    except Exception as e:
        print(f"\nFAILED: {e}")
        sys.exit(1)
