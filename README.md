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
### Run Detection Script
    Create a folder "outputs"
    python .\detect_from_image.py -m ssd_mobilenet_v2_320x320_coco17_tpu-8\saved_model -l .\models\research\object_detection\data\mscoco_complete_label_map.pbtxt -i .\models\research\object_detection\test_images
### Check Results in Outputs folder
    ![detection_output0](https://user-images.githubusercontent.com/104552567/236894146-b911ffd2-0c3b-4fa4-aa73-c7e702d659fc.png)
    ![detection_output1](https://user-images.githubusercontent.com/104552567/236894183-d64056d0-348a-4ca1-851a-7335f2f5a6dd.png)
    ![detection_output2](https://user-images.githubusercontent.com/104552567/236894195-94f89b16-8225-4b51-b28c-31fd686d3bfb.png)


## Training New Model from Scratch
