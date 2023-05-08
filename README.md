# Tensorflow_model_learning

## Common Setup and First Model
### Pre-requisite
    Python (Version 3.9) 
    Protobuf
    Anaconda
### Create Virtual Environment
    git clone https://github.com/tensorflow/models.git
    conda create -n {environment_name} pip python=3.9
    conda activate {environment_name}
### Install Protobuf in project
    conda install protobuf
    Add use_protobuf.py into models/research/ directory
    cd models/research/
    python use_protobuf.py object_detection/protos protoc
    protoc object_detection/protos/*.proto --python_out=.
### Install Dependencies
    Copy /models/research/object_detection/packages/tf2/setup.py to models/research/ directory
    python -m pip install .
### Test all dependencies are installed or not
    python object_detection\builders\model_builder_tf2_test.py
    If any dependecy is pending: conda install {name}
### Tensorflow Model Zoo
    pip install wget
    python model_downloader.py

## Training New Model from Scratch
