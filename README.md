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

## Training New Model from Scratch
