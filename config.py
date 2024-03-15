import pathlib


INPUT_IMAGE = pathlib.Path("data/inputs/S2B_MSIL2A_20221127T075159_N0400_R135_T36NXF_20221127T100500.SAFE.zip")
TEST_ROI_GEOJSON = pathlib.Path("data/inputs/region_of_interest.geojson")
OUTPUT_DIR = pathlib.Path("data/outputs/")
DATASET_SRS = 32636
GDAL_DRIVER_NAME = "GTiff"
