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


def process_satellite_image():
    cwd = pathlib.Path(__file__).parent
    output_dir = cwd / config.OUTPUT_DIR
    input_dataset = file_io.read_dataset(cwd / config.INPUT_IMAGE)
    print_metadata(input_dataset)


if __name__ == "__main__":
    process_satellite_image()
