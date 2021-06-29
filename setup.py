import os
from platform import system

ROOT_DIR = os.path.abspath("../")

try:
# =============================================================================
# Setup on Windows
# =============================================================================
    if system() == "Windows":

        #os.system("pip install virtualenv")

        activate_this_file = "./env/bin/activate_this.py"
        exec(activate_this_file, dict(__file__=activate_this_file))

        #os.system("pip install -r requirements/Windows_on_Python3.9.2/requirements.txt")

# =============================================================================
# Setup on Linux
# =============================================================================
    elif system() == "Linux":

        os.system("python3 -m pip install --user virtualenv") # install venv module


        os.system("source env/bin/activate")

        os.system("pip3 install pip --upgrade")

        os.system("python3 -m pip install -r requirements/Linux_on_Python3.7.3/requirements.txt") # install dependencies

        os.system("sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 \
                        libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev \
                        liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev")
        
        os.system("pip3 install keras_applications==1.0.8 --no-deps")

        os.system("pip3 install keras_preprocessing==1.1.0 --no-deps")

        os.system("pip3 install numpy==1.20.3")

        os.system("pip3 install h5py==3.1.0")

        os.system("pip3 install pybind11")

        os.system("pip3 install -U --user six wheel mock")

        os.system('wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh"')

        os.system("source tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh")

        os.system("sudo pip3 uninstall tensorflow")

        os.system("sudo -H pip3 install tensorflow-2.5.0-cp37-none-linux_armv7l.whl")

        os.system("sudo reboot")


# =============================================================================
# Else-Statement
# =============================================================================
    else:
        print("Sorry but this script is only designed to work on Windows or Linux")

except:
    pass


