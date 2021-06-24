# PROJECT: *empty*  

## Introduction
This Project is building upon Mask R-CNN (by Matterport, Inc.) for object detection and instance segmentation on Keras and TensorFlow while enhancing/altering parts to create a reliable color detecion method for Windows and Raspberri Pi 3.

## Installation 

1) Download and extract ColiChecker.zip or just clone the repo

2) Open terminal and go to the directory:
#####
    $ cd ./ColiChecker

3) Install venv module
#####
    $ python3 -m pip install --user virtualenv

4) Activate a virtual environment

#### On Windows
    $ ./env/Scripts/activate 
#### On Raspberri Pi 3/ Linux
    $ source env/bin/activate 

5) Install requirements.txt
#### If you are on Windows
    $ python3 -m pip install -r requirements_PC_Py3.9.2.txt
#### If you are on Raspberri Pi 3/Linux
    $ python3 -m pip install -r requirements_PC_Py3.7.3.txt
#### If there are any problems 
    Install from the requiremnts.txt inside Mask_RCNN or the requirements directory
    $ python3 -m pip install -r requirements.txt

6) You should now be able to run the project:
####
    $ python run.py

   [IMPORTANT: for the image analysis part there have to be images in /ColiChecker/images/images_1_camera]


## KNOWN ISSUES ON Raspberry Pi 3:

### 'keras.engine has no attribute layers' 

1) Change line 23 in Mask_RCNN/mrcnn/model.py from
#####
    $ import keras.engine as KE

to
#####
    $ import keras.engine.topology as KE

### When receiving 'what() std::bad_alloc' as output
1) Reduce the thread usage on the raspberry pi's cpu by uncommenting the following lines
####
    $ tf.config.threading.set_intra_op_parallelism_threads(1)
    $ tf.config.threading.set_inter_op_parallelism_threads(1)
    $ tf.executing_eagerly()

located right after the imports in the Mask_RCNN/mrcnn/model.py

E) Changelog:

Prior to using Training Weights I had to manually alter the following lines in Mask_RCNN/mrcnn/model.py in this order (changes are included in said file of this project however...):
    •  Line 958 ff.
    •  Line 709
    •  Line 27
    •  Line 2141 ff.

### If you are facing issues regarding modules do the following #

1) Delete the virtual environment (It has to be deactivated):
#####
    $ sudo rm -rf env

2) Create a new virtual environment with Python 3.7.3:

####   upgrade pip version
    $ python3 -m pip install --user --upgrade pip
####   install venv module
    $ python3 -m pip install --user virtualenv
####  create virtual env
    $ python3 -m venv env
####   activate env:
    $ source env//bin/activate 
####   upgrade pip inside the venv
    $ python3 -m pip install --user --upgrade pip

3) Download the modules via requirements_PI_Py3.7.3.txt file 
    [IMPORTANT: You may have to change the name to requirements.txt prior]
####
    $ python3 -m pip install -r requirements.txt

4) Copy the mrcnn directory from 
####
    /ColiChecker/Mask_RCNN/ 
into 
####
    /ColiChecker/env/lib/python3.7/site-packages/

5) Run run.py


### If the previous steps did not fix the problem you will have to do the following #
#### (May also apply to PC)

1) Delete the virtual environment (It has to be deactivated):
####
    $ sudo rm -rf env

2) Create a new virtual environment with Python 3.7.3:

####   Upgrade pip version
    $ python3 -m pip install --user --upgrade pip
####   Install venv module
    $ python3 -m pip install --user virtualenv
####   Create virtual env
    $ python3 -m venv env
####   Activate env:
    $ source env//bin/activate 
####   Upgrade pip inside the venv
    $ python3 -m pip install --user --upgrade pip

3) Install needed modules from one of the following requirements.txt:

#### If you are on Raspberri Pi 3/Linux
    $ python3 -m pip install -r requirements_PC_Py3.7.3.txt
##### (If there are any problems install from the requiremnts.txt inside Mask_RCNN)
    $ python3 -m pip install -r requirements.txt

#### On a Raspberry Pi 3 you may have to additionaly do the following

4) Manually install dependecies
####
    $ sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 \
                            libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev \
                            liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev

##### Newer pip versions activate warnings when encountering sudo pips inside of virtual environments so remove everything infront of pip3
####
    $ sudo pip3 install pip --upgrade            
    $ sudo pip3 install keras_applications==1.0.8 --no-deps
    $ sudo pip3 install keras_preprocessing==1.1.0 --no-deps
    $ sudo pip3 install numpy==1.20.3
    $ sudo pip3 install h5py==3.1.0
    $ sudo pip3 install pybind11
    $ pip3 install -U --user six wheel mock
####
    $ wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh"
    $ source tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh

    $ sudo pip3 uninstall tensorflow
    $ sudo -H pip3 install tensorflow-2.5.0-cp37-none-linux_armv7l.whl

    【Required】 Restart the terminal.

##### You may need to get a newer numpy version but run main.py prior to verify, if so:
    $ pip3 install -U numpy

##### Resources:
    https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

    https://github.com/matterport/Mask_RCNN/blob/master/requirements.txt

    https://stackoverflow.com/questions/63414493/pipenv-activate-virtual-environment-on-new-computer-after-git-clone

    https://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/ (until Step 5 (Step 5 included))


## Appendix

#### Regarding the mrcnn folder
You may have to create a mrcnn copy and put it into 
#####
"\ColiChecker\env\Lib\site-packages\"

to resolve import issues, so whenever making changes to one of these folders you need to update the other one as well.
Alternatively you may change the import structure inside the MRCNN_Balloon.py and MRCNN_Coco.py files so they may directly import from inside the Mask_RCNN directory.