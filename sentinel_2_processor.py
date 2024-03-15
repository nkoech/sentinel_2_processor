from dataclasses import dataclass
import pathlib
import pprint
import typing

import numpy as np
from osgeo import gdal
import rasterstats

import config
import file_io
import compute_index as index


@dataclass(frozen=True)
class Bands:
    blue: np.ndarray
    green: np.ndarray
    red: np.ndarray
    nir: np.ndarray


def print_metadata(input_dataset: gdal.Dataset):
    metadata = input_dataset.GetMetadata()
    if metadata is None:
        raise RuntimeError("Could not read metadata")
    pprint.pprint(metadata)
    pprint.pprint("======================= END OF METADATA PRINT =======================")


def get_subdataset_name(input_dataset: gdal.Dataset, resolution: str) -> gdal.Dataset:
    subdatasets = input_dataset.GetSubDatasets()
    if subdatasets is None:
        raise RuntimeError(
            f"Could not get subdatasets for the resolution: {resolution}"
        )
    # Last two subdatasets are preview images, so we skip them.
    for subdataset in subdatasets[:-2]:
        if resolution in subdataset[1]:
            return subdataset[0]


def crop_dataset(
    input_file: pathlib.Path, output_file: pathlib.Path, roi_extent: typing.Tuple[float]
) -> pathlib.Path:
    gdal.Translate(
        str(output_file),
        str(input_file),
        projWin=[roi_extent[0], roi_extent[3], roi_extent[2], roi_extent[1]],
        metadataOptions=[config.TEST_ROI_METADATA],
    )
    return output_file


def get_bands(input_dataset: gdal.Dataset) -> Bands:
    bands = []
    for i in range(1, input_dataset.RasterCount + 1):
        band = input_dataset.GetRasterBand(i)
        if band is None:
            raise RuntimeError(f"Could not open band {i}")
        bands.append(band.ReadAsArray())
    return Bands(*bands)


def compute_indices(
    input_dataset: gdal.Dataset, output_dir: pathlib.Path
) -> typing.List[pathlib.Path]:
    output_files = []
    bands = get_bands(input_dataset)
    index_computations = {
        config.Index.NDVI: index.compute_ndvi(bands, config.NO_DATA),
        config.Index.NDWI: index.compute_ndwi(bands, config.NO_DATA),
        config.Index.EVI: index.compute_evi(bands, config.NO_DATA),
    }
    for index_name, data in index_computations.items():
        output_file = output_dir / config.INDEX_OUTPUT_FILES[index_name]
        file_io.write_dataset(
            input_dataset, output_file, data, gdal.GDT_Float32, config.NO_DATA
        )
        output_files.append(output_file)
    return output_files


def compute_zonal_statistics(
    input_files: typing.List[pathlib.Path], zone_file: pathlib.Path
) -> typing.List[typing.List[typing.Dict[str, float]]]:
    zonal_stats = []
    for input_file in input_files:
        stats = rasterstats.zonal_stats(
            zone_file, str(input_file), stats=config.ZONAL_STATISTICS
        )
        zonal_stats.append(stats)
    return zonal_stats


def process_satellite_image():
    cwd = pathlib.Path(__file__).parent
    output_dir = cwd / config.OUTPUT_DIR
    input_dataset = file_io.read_dataset(cwd / config.INPUT_IMAGE)
    print_metadata(input_dataset)
    roi_geom = file_io.read_geojson(cwd / config.TEST_ROI_GEOJSON, config.DATASET_SRS)
    roi_extent = roi_geom.bounds.iloc[0].values.tolist()
    sub_dataset_name = get_subdataset_name(input_dataset, config.SUBDATASET_RESOLUTION)
    test_roi_file = crop_dataset(sub_dataset_name, config.TEST_ROI_FILE, roi_extent)
    test_roi_dataset = file_io.read_dataset(test_roi_file)
    indices_files = compute_indices(test_roi_dataset, output_dir)
    zone_stats = compute_zonal_statistics(indices_files, roi_geom)


if __name__ == "__main__":
    process_satellite_image()
