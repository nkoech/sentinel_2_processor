import pathlib

import geopandas as gpd
import numpy as np
from osgeo import gdal

import config


def read_dataset(input_file: pathlib.Path) -> gdal.Dataset:
    dataset = gdal.Open(str(input_file))
    if dataset is None:
        raise RuntimeError(f"Could not open the file: {input_file}")
    return dataset


def read_geojson(input_file: pathlib.Path, target_crs: int) -> gdal.Dataset:
    geom = gpd.read_file(input_file)
    return geom.to_crs(epsg=target_crs)


def write_dataset(
    input_dataset: gdal.Dataset,
    output_file: pathlib.Path,
    data: np.ndarray,
    data_type: gdal.GDT_Unknown,
    no_data: float = None,
) -> gdal.Dataset:
    driver = gdal.GetDriverByName(config.GDAL_DRIVER_NAME)
    output_dataset = driver.Create(
        str(output_file),
        input_dataset.RasterXSize,
        input_dataset.RasterYSize,
        1,
        data_type,
    )
    output_dataset.SetProjection(input_dataset.GetProjection())
    output_dataset.SetGeoTransform(input_dataset.GetGeoTransform())
    output_band = output_dataset.GetRasterBand(1)
    if no_data is not None:
        output_band.SetNoDataValue(no_data)
    output_band.WriteArray(data)
    output_band.FlushCache()
    output_band.ComputeStatistics(False)
    return output_dataset
