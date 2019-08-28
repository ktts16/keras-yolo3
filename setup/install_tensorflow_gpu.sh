# > Step 2: Verify You Have a CUDA-Capable GPU
lspci | grep -i nvidia

# If you do not see any settings, update the PCI hardware database that Linux maintains 
# $	update-pciids 
# (generally found in /sbin) at command line.
# $	lspci | grep -i nvidia

# > Step 3: Verify You Have a Supported Version of Linux
# Determine which distribution and release number you’re running.
uname -m && cat /etc/*release

# The x86_64 line indicates you are running on a 64-bit system which is supported by cuda 10.0.

# > Step 4: Install NVIDIA CUDA 10.0
# Remove previous cuda installation (if you installed cuda before):
sudo apt-get purge nvidia*
sudo apt-get autoremove
sudo apt-get autoclean
sudo rm -rf /usr/local/cuda*

# Add key and download:
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" | sudo tee /etc/apt/sources.list.d/cuda.list

# Install CUDA-10.0:
sudo apt-get update 
sudo apt-get -o Dpkg::Options::="--force-overwrite" install cuda-10-0 cuda-drivers

# Reboot and type:
echo 'export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc
sudo ldconfig

# To check if installation was successful: after executing next command you need to see version of your nvidia-drivers and GPU:
nvidia-smi

# If you have low screen resolution, fix this with Xorg:
sudo nvidia-xconfig

# If this has not helped, check one of my previous installation 
# (I have described in detail what should help if problems remain).
# Check nvidia-settings to find out how much GPU is loaded 
# (for example, if trained neuralnets using ML framework):
nvidia-settings
