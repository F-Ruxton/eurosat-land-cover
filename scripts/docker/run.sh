#!/bin/bash

# Start a container using the tensorflow-jupyterlab image,
# mounting the cwd to the container's /project directory.

if [ $1 = "bash" ] ; then
    docker run \
        --gpus=all \
        -v "$(pwd)/notebooks:/project/notebooks" \
        -v "$(pwd)/.jupyter/jupyter_notebook_config.py:/project/.jupyter/jupyter_notebook_config.py" \
        -p 8888:8888 \
        --rm -it \
        tf-lab bash
else
    docker run \
        --gpus=all \
        -v "$(pwd)/notebooks:/project/notebooks" \
        -v "$(pwd)/.jupyter/jupyter_notebook_config.py:/project/.jupyter/jupyter_notebook_config.py" \
        -p 8888:8888 \
        tf-lab "$@"
fi
