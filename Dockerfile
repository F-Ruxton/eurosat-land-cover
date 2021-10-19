# Run Jupyter lab in docker with tensorflow GPU
# and other dependencies

FROM tensorflow/tensorflow:latest-gpu-py3

RUN mkdir -p /project && chown 1000 /project

USER 1000:1000

# Used for juypterlab
EXPOSE 8888
ENV PATH="/project/.local/bin:${PATH}"
ENV PATH="/root/.local/bin:${PATH}"

ENV HOME=/project
WORKDIR /project

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

# # Run lab by default
CMD [ "jupyter", "lab", "--ip", "0.0.0.0" ]
