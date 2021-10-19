#!/bin/bash

# Use this image to run scripts that depend on OSGeo's GDAL library

docker run \
    -v "$(pwd)/preprocessing:/home" \
    -v "$(pwd)/data:/home/data" \
    -w /home \
    --rm -it \
    osgeo/gdal:alpine-normal-3.3.1 sh

# Convert all tif files in EuroSAT multispectral dataset to numpy files
# python tifs_to_numpy.py data/EuroSATAllBands/sentinel_2/tif data/EuroSATAllBands/sentinel_2/np