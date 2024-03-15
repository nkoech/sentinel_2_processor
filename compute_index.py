import numpy as np

from sentinel_2_processor import Bands


def compute_index(band_1: np.ndarray, band_2: np.ndarray, no_data: float) -> np.ndarray:
    # Convert band to float so that floating point math is used.
    band_1 = band_1.astype(np.float64)
    # Mask to avoid ZeroDivisionError
    band_1 = np.ma.masked_where(band_1 + band_2 == 0, band_1)
    index = (band_1 - band_2) / (band_1 + band_2)
    return index.filled(no_data)


def compute_ndvi(bands: Bands, no_data: float) -> np.ndarray:
    return compute_index(bands.nir, bands.red, no_data)


def compute_ndwi(bands: Bands, no_data: float) -> np.ndarray:
    return compute_index(bands.green, bands.nir, no_data)
