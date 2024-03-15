import pathlib

import geopandas as gpd
from osgeo import gdal


def read_dataset(input_file: pathlib.Path) -> gdal.Dataset:
    dataset = gdal.Open(str(input_file))
    if dataset is None:
        raise RuntimeError(f"Could not open the file: {input_file}")
    return dataset


def read_geojson(input_file: pathlib.Path, target_crs: int) -> gdal.Dataset:
    geom = gpd.read_file(input_file)
    return geom.to_crs(epsg=target_crs)
