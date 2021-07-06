import os
import sys
import subprocess as subp
from platform import system

ROOT_DIR = os.path.abspath("../")

#   .\env\Scripts\activate for Windows
#   source env/bin/activate for Linux
#   deactivate

# =============================================================================
# Setup on Windows
# =============================================================================
if system() == "Windows":

    subp.run("pip install virtualenv")
    subp.run("virtualenv env")
    subp.run("pip install --user --upgrade pip")
    

    subp.run("pip install --target=env/Lib/site-packages -r requirements/Windows_on_Python3.9.2/requirements.txt")

# =============================================================================
# Setup on Linux
# =============================================================================
elif system() == "Linux":
    
    subp.run("sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 \
                    libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev \
                    liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev") # install system dependencies
    
    subp.run("python3 -m pip install --user virtualenv") # install venv module

    subp.run("virtualenv env") # create virtual environment

    subp.run("source env/bin/activate")

    subp.run("pip3 install --user --upgrade pip") # upgrade pip

    subp.run("python3 -m pip3 install --target=env/lib/python3.7/site-packages -r requirements/Linux_on_Python3.7.3/requirements.txt")
    
    subp.run("python3 -m pip3 install --target=env/lib/python3.7/site-packages keras_applications==1.0.8 --no-deps")

    subp.run("python3 -m pip3 install --target=env/lib/python3.7/site-packages keras_preprocessing==1.1.0 --no-deps")

    subp.run("python3 -m pip3 install --target=env/lib/python3.7/site-packages numpy==1.20.3")

    subp.run("python3 -m pip3 install --target=env/lib/python3.7/site-packages h5py==3.1.0")

    subp.run("python3 -m pip3 install --target=env/lib/python3.7/site-packages pybind11")

    subp.run("python3 -m pip3 install -U --user --target=env/lib/python3.7/site-packages six wheel mock")

    subp.run('wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh"')

    subp.run("source tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh")

    subp.run("sudo pip3 uninstall tensorflow")

    subp.run("sudo -H pip3 install tensorflow-2.5.0-cp37-none-linux_armv7l.whl")

    subp.run("sudo reboot")


# =============================================================================
# Else-Statement
# =============================================================================
else:
    print("Sorry but this script is only designed to work on Windows or Linux")




