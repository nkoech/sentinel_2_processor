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
    # Equation: (NIR - RED) / (NIR + RED)
    return compute_index(bands.nir, bands.red, no_data)


def compute_ndwi(bands: Bands, no_data: float) -> np.ndarray:
    # Equation: (GREEN - NIR) / (GREEN + NIR)
    return compute_index(bands.green, bands.nir, no_data)


def compute_evi(bands: Bands, no_data: float) -> np.ndarray:
    # Equation: 2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))
    # Convert band to float so that floating point math is used.
    red_band = bands.red.astype(np.float64)
    denominator = bands.nir + 6 * red_band - 7.5 * bands.blue + 1
    # Mask to avoid ZeroDivisionError
    denominator = np.ma.masked_where(denominator == 0, denominator)
    evi_data = 2.5 * ((bands.nir - red_band) / denominator)
    return evi_data.filled(no_data)
