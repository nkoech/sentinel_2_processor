import pathlib
import pprint

from osgeo import gdal

import config
import file_io


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


def process_satellite_image():
    cwd = pathlib.Path(__file__).parent
    output_dir = cwd / config.OUTPUT_DIR
    input_dataset = file_io.read_dataset(cwd / config.INPUT_IMAGE)
    print_metadata(input_dataset)
    roi_geom = file_io.read_geojson(cwd / config.TEST_ROI_GEOJSON, config.DATASET_SRS)
    roi_extent = roi_geom.bounds.iloc[0].values.tolist()


if __name__ == "__main__":
    process_satellite_image()
