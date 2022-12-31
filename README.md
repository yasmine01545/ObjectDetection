
we will Create applications that upload images or videos to detect the object and the category of all objects present in this image.
1. Training a performing deep learning model for object detection
2. Evaluate your model.
3. Test it with random images and video.

# OpenCV
OpenCv is the huge open-source library for computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems. By using it, one can process images and videos to identify objects, faces, or even the handwriting of a human. This article Readme we will focus on detecting objects.
## Installation
*** 
Run The following command in the terminal to install opencv
```
pip install opencv-python
```
# ObjectDetection
Object Detection is a computer technology related to computer vision, image processing, and deep learning that deals with detecting instances of objects in images and videos.
## Database
Microsoft's Common Objects in Context dataset (COCO) is the most popular object detection dataset at the moment. It is widely used to benchmark the performance of computer vision methods.

The COCO Dataset: The MS COCO dataset is a large-scale object detection, segmentation, and captioning dataset published by Microsoft.

COCO stands for Common Objects in Context, as the image dataset was created with the goal of advancing image recognition.

The COCO dataset contains challenging, high-quality visual datasets for computer vision, mostly state-of-the-art neural networks.
# List of the COCO Object Classes
The COCO dataset classes for object detection and tracking include the following pre-trained 80 objects:
![image](https://user-images.githubusercontent.com/80918787/210131839-90dcb3e6-f484-441b-b613-c955a983d0d2.png)
# How to download the COCO dataset
There are different dataset splits available to download for free.

To download them and see the most recent Microsoft COCO 2020 challenges, visit the official MS COCO website https://cocodataset.org/#download
# Object Detection using Mobilenet SSD
## What is MobilenetSSD?

Convolutional neural networks are used to develop a model that consists of multiple layers for classifying given objects into one of the defined classes. 
These objects are detected using higher resolution feature maps made possible by recent advances in deep learning with image processing. 
Mobilenet SSD is an object detection model that computes the output bounding box and object class from the input image.
This Single Shot Detector (SSD) object detection model uses Mobilenet as a backbone and can achieve fast object detection optimized for mobile devices.


![image](https://user-images.githubusercontent.com/80918787/210132312-79c223f8-aacb-473b-b7df-327de4ecc09a.png)

OpenCV needs an extra configuration file to import object detection models from TensorFlow
## Use existing config file for your model
we can use configs files that has been tested in OpenCV


| Model | version   |  weights   |    architecture   |
| :-----: | :---: | :---: | :---: |
| MobileNet-SSD v3  | 2020_01_14  | [weights](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v3_large_coco_2020_01_14.tar.gz)   |[config](https://gist.github.com/dkurt/54a8e8b51beb3bd3f770b79e56927bd7) 
