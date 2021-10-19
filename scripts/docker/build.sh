#!/bin/bash

# Build docker image with tensorflow-gpu and jupyterlab installed.
# Run script from the project root directory, containing the dockerfile.
docker build -t tf-lab .
