# Seninel-2 Data Processor


This is a simple tool to process Sentinel-2 data. It is based on the [Sentinel-2 L2A](https://dataspace.copernicus.eu/) dataset available on Copernicus Dataspace. The tool follows the following workflow:

1. Read the Sentinel-2 L2A and region of interest data from local the directory.
2. Get the required Sentinel-2 10m bands.
3. Print out the metadata.
4. Subset the bands to the region of interest.
5. Computes indices, specifically NDVI NDWI and EVI.
6. Save the output indices datasets to the local directory.
7. Compute zone statistics for the indices for the region of interest.
8. Insert the zone statistics to the PostgreSQL database.
9. Print zonal statistics values if insert to the database is successful.


## How to use

1. Install required packages using the following command:

```bash
pip install -r requirements.txt
```

2. On your terminal, navigate to the directory where the `sentinel2_data_processor.py` file is located.
3. Run the following command:

```bash
python sentinel2_data_processor.py
```
