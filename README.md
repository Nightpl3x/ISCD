# ################################################# #
# Mask R-CNN for Object Detection and Segmentation  #
# ################################################# #

# ##############
# Installation #
# ##############

1) Extract ColiChecker.zip to /home/pi

2) Open terminal and go to the directory:

    $ cd /home/pi/ColiChecker

3) activate the virtual environment to gain access to modules used in the project and all the changes made by me

    $ source env//bin/activate 

4) you should now be able to run the project:

    $ python main.py

   [IMPORTANT: for the image analysis part there have to be images in /ColiChecker/images/images_1_camera]

5) Enjoy or build upon the project (as long as you dont change the directory names and/or structure of course)
# ############################################################################################################################################################################
# KNOWN ISSUES:
# ############################################################################################################################################################################

# #############################################################
# keras.engine has no attribute layers #
# #############################################################
1) change line 23 from

    import keras.engine as KE

    to

    import keras.engine.topology as KE

E) Changelog:
	• Before using the MS Coco Training Weights I had to manually update some of the mrcnn files in the respective order:
		○ 'Mask_RCNN\mrcnn\model.py':
			§ Line 951
			§ Line 702
			§ Line 27
			§ Line 2135 ff:
				□ For use on Raspberry
					® Line 23 (see above)
		○ '/?/saving.py':
            § Line 8 ff. (not so sure here but I wrote it down)


# #############################################################
# If you are facing issues regarding modules do the following #
# #############################################################

1) delete the virtual environment (It has to be deactivated):

    $ sudo rm -rf env

2) create a new virtual environment with Python 3.7.3:

#   upgrade pip version
    $ python3 -m pip install --user --upgrade pip
#   install venv module
    $ python3 -m pip install --user virtualenv
#   create virtual env
    $ python3 -m venv env
#   activate env:
    $ source env//bin/activate 
#   upgrade pip inside the venv
    $ python3 -m pip install --user --upgrade pip

3) download the modules via requirements_PI_Py3.7.3.txt file (IMPORTANT: Change the name to requirements.txt prior)

    $ python3 -m pip install -r requirements.txt

4) Copy the mrcnn directory from /ColiChecker/Mask_RCNN/ into /ColiChecker/env/lib/python3.7/site-packages/

5) run main.py

# #################################################################################
# If the previous steps did not fix the problem you will have to do the following #
# #################################################################################

1) delete the virtual environment (It has to be deactivated):

    $ sudo rm -rf env

2) create a new virtual environment with Python 3.7.3:

#   upgrade pip version
    $ python3 -m pip install --user --upgrade pip
#   install venv module
    $ python3 -m pip install --user virtualenv
#   create virtual env
    $ python3 -m venv env
#   activate env:
    $ source env//bin/activate 
#   upgrade pip inside the venv
    $ python3 -m pip install --user --upgrade pip

3) Manually install needed modules

    $ pip3 install numpy
    $ pip3 install scipy
    $ pip3 install sklearn
    $ pip3 install Pillow
    $ pip3 install cython
    $ pip3 install matplotlib
    $ pip3 install scikit-image
    $ pip3 install tensorflow>=1.3.0
    $ pip3 install keras>=2.0.8
    $ pip3 install opencv-python
    $ pip3 install h5py
    $ pip3 install imgaug
    $ pip3 install IPython[all]

4) Manually install dependecies

    $ sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 \
                            libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev \
                            liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev                          
    $ sudo pip3 install pip --upgrade                   (new pip versions activate warnings when encountering sudo pips so remove everything infront of pip3 )
    $ sudo pip3 install keras_applications==1.0.8 --no-deps
    $ sudo pip3 install keras_preprocessing==1.1.0 --no-deps
    $ sudo pip3 install numpy==1.20.3
    $ sudo pip3 install h5py==3.1.0
    $ sudo pip3 install pybind11
    $ pip3 install -U --user six wheel mock

    $ wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh"
    $ source tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh

    $ sudo pip3 uninstall tensorflow
    $ sudo -H pip3 install tensorflow-2.5.0-cp37-none-linux_armv7l.whl

    【Required】 Restart the terminal.

#   you may need to get a newer numpy version but run main.py prior to verify, if so:
    $ pip3 install -U numpy

# Resources:
    https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

    https://github.com/matterport/Mask_RCNN/blob/master/requirements.txt

    https://stackoverflow.com/questions/63414493/pipenv-activate-virtual-environment-on-new-computer-after-git-clone

    https://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/ (until Step 5 (Step 5 included))


# ####################################################################################################################
# Epilogue #
# ####################################################################################################################

# Regarding the mrcnn folder
The mrcnn folder builds the base the project stands on and is crucial for all image processes going on in the parent directory. I made many changes to fit it to the task however you can always find the original directory here:

https://github.com/matterport/Mask_RCNN/releases


Additionally I had to create a mrcnn copy and put it into 

"\ColiChecker\env\Lib\site-packages\mrcnn"

to resolve import issues, so whenver making changes to one of these folders you need to update the other one as well.