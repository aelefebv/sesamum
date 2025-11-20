# Sesamum

A lightweight bioformats-like library for Python.

## Description

Sesamum provides a simple, unified interface for reading various microscopy image formats (TIFF, LSM, ND2) into NumPy arrays, along with their metadata. It aims to be minimal and lightweight, avoiding heavy dependencies.

## Installation

```bash
pip install sesamum
```

## Usage

```python
import sesamum

# Read a file (format detected automatically)
data, metadata = sesamum.read('path/to/image.tif')

print(f"Shape: {data.shape}")
print(f"Metadata: {metadata}")
```

## Supported Formats

- **TIFF** (`.tif`, `.tiff`)
- **LSM** (`.lsm`)
- **Nikon ND2** (`.nd2`)

## Dependencies

- `numpy`
- `tifffile`
- `nd2`
