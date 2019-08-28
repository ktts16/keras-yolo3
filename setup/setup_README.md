# Installation #
## Install Prerequisites ##

cd $HOME/github/keras-yolo3/setup

sh ./update_packages.sh

## Install Keras Prerequisites ##
[Install Keras to Ubuntu 18.04](https://github.com/hsekia/learning-keras/wiki/How-to-install-Keras-to-Ubuntu-18.04)
sh ./install_keras_prerequisites.sh

## Install Python pip packages including Keras  ##

sh ./install_pip_packages.sh

## Install Tensorflow with GPU Support ##
[Install Tensorflow with GPU Support](https://medium.com/better-programming/install-tensorflow-1-13-on-ubuntu-18-04-with-gpu-support-239b36d29070)

sh ./install_tensorflow_gpu.sh

### Install cuDNN 7.5.0 ###
Go [here](https://developer.nvidia.com/cudnn) and click Download CuDNN. Log in and accept the required agreement. 
Click the following: 
 * “Download cuDNN v7.5.0 (Feb 21, 2019), for CUDA 10.0” and
 * “cuDNN Library for Linux”.

sh ./install_tensorflow_gpu_part2.sh

Note: for Tensorflow without GPU support

sudo pip3 install tensorflow
