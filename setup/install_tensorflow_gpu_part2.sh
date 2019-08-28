# > Step 5: Install cuDNN 7.5.0 (part 2)
tar -xf cudnn-10.0-linux-x64-v7.5.0.56.tgz
sudo cp -R cuda/include/* /usr/local/cuda-10.0/include
sudo cp -R cuda/lib64/* /usr/local/cuda-10.0/lib64

# > Step 6: Install Dependencies
# Install libcupti:
sudo apt-get install libcupti-dev
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
# Python related:
sudo apt-get install python3-numpy python3-dev python3-pip python3-wheel

# > Step 7: Install Tensorflow-GPU
# Install Tensorflow-GPU 1.13 using pip:
pip3 install --user tensorflow-gpu==1.13.1
# Now you can check which tensorflow version you install:
pip3 show tensorflow-gpu
