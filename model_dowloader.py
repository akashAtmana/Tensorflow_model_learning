import wget
model_link = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz"
wget.download(model_link)
import tarfile
tar = tarfile.open('ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz')
tar.extractall('.')
tar.close()