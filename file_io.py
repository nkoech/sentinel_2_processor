import pathlib

from osgeo import gdal


def read_dataset(input_file: pathlib.Path) -> gdal.Dataset:
    dataset = gdal.Open(str(input_file))
    if dataset is None:
        raise RuntimeError(f"Could not open the file: {input_file}")
    return dataset
