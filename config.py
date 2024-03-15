from enum import Enum
import pathlib


class Index(Enum):
    NDVI = "ndvi"
    NDWI = "ndwi"
    EVI = "evi"


INPUT_IMAGE = pathlib.Path(
    "data/inputs/S2B_MSIL2A_20221127T075159_N0400_R135_T36NXF_20221127T100500.SAFE.zip"
)
TEST_ROI_GEOJSON = pathlib.Path("data/inputs/region_of_interest.geojson")
OUTPUT_DIR = pathlib.Path("data/outputs/")
TEST_ROI_FILE = OUTPUT_DIR / "test_roi.tif"
SUBDATASET_RESOLUTION = "10m resolution"
DATASET_SRS = 32636
TEST_ROI_METADATA = "region=test roi"
NO_DATA = -999999
INDEX_OUTPUT_FILES = {
    Index.NDVI: "ndvi.tif",
    Index.NDWI: "ndwi.tif",
    Index.EVI: "evi.tif",
}
GDAL_DRIVER_NAME = "GTiff"
ZONAL_STATISTICS = ["min", "max", "mean", "median", "std"]
DB_CONN_PARAMS = {
    "dbname": "zonal_statistics_db",
    "user": "nkoech",
    "password": "mypass",
    "host": "localhost",
}
CREATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS test_roi_tbl (
        image_date DATE,
        min FLOAT,
        max FLOAT,
        mean FLOAT,
        median FLOAT,
        std_dev FLOAT
    )
"""
INSERT_VALUES_QUERY = """
    INSERT INTO test_roi_tbl (image_date, min, max, mean, median, std_dev) 
    VALUES (%s, %s, %s, %s, %s, %s)
"""
