# To run ORB-SLAM 3

clone this repository on your local computer - https://github.com/UZ-SLAMLab/ORB_SLAM3

Run the following commands on the terminal to build 

    $ chmod +x build.sh
    $ ./build.sh

This will create libORB_SLAM3.so at lib folder and the executables in Examples folder

# Dependencies and Errors 
The following are the dependencies of the code - 

    1. C++14 
    2. Pangolin v5.0 
    3. Python3
    4. OpenCV 4.2
    5. DBoW2 and g20 latest versions
    6. Ubuntu 20.04

To install Pangolin, version 5

    git clone --recursive https://github.com/stevenlovegrove/Pangolin.git
    ./scripts/install_prerequisites.sh --dry-run recommended
    ./scripts/install_prerequisites.sh -m brew all
    ./scripts/install_prerequisites.sh recommended

Some common issues : https://github.com/UZ-SLAMLab/ORB_SLAM3/issues/387
slot reference error - (to upgrade C++ version from 11 to 14)
    sed -i 's/++11/++14/g' CMakeLists.txt 

# To run ORB-SLAM on EuRoC execute the following command - 

    cd ~
    mkdir -p Datasets/EuRoc
    cd Datasets/EuRoc/
    wget -c http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_01_easy/MH_01_easy.zip
    mkdir MH01
    unzip MH_01_easy.zip -d MH01/

# For running Monocular 
    ./Examples/Monocular/mono_euroc ./Vocabulary/ORBvoc.txt ./Examples/Monocular/EuRoC.yaml ~/Datasets/EuRoc/MH01 ./Examples/Monocular/EuRoC_TimeStamps/MH01.txt dataset-MH01_mono

The in general command is - path_to_executable path_to_vocabulary path_to_settings path_to_images path_to_timestamps trajectory_name
