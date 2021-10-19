#!/bin/bash

# Start a container using the tensorflow-jupyterlab image,
# mounting notebooks, data, models etc to the container's
# /project directory.
#
# Usage: Run from the repo's root directory
#
#   ./scripts/docker/run.sh       # launch jupyterlab server
#   ./scripts/docker/run.sh bash  # enter interactive bash shell, useful for managing dependencies etc

flags=(
    --gpus all \
    -v "$(pwd)/notebooks:/project/notebooks" \
    -v "$(pwd)/data:/project/data" \
    -v "$(pwd)/models:/project/models" \
    -v "$(pwd)/.jupyter/jupyter_notebook_config.py:/project/.jupyter/jupyter_notebook_config.py" \
    -p 8888:8888
)

if [ "$1" = "bash" ] ; then
    docker run "${flags[@]}" --rm -it tf-lab bash
else
    docker run "${flags[@]}" tf-lab "$@"
fi
