#!/bin/bash

# Start a container using the tensorflow-jupyterlab image,
# mounting the cwd to the container's /project directory.

if [ $1 = "bash" ] ; then
    docker run --gpus=all -v ${pwd}:/project --rm -it -p 8888:8888 tf-lab bash
else
    docker run --gpus=all -v ${pwd}:/project -p 8888:8888 tf-lab "$@"
fi
