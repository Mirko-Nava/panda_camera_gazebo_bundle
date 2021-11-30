# Panda Camera Gazebo Bundle

A bundle of ros packages used to simulate a [panda robotic arm](https://www.franka.de/robot-system "Franka Panda") with a [realsense d435 camera](https://www.intelrealsense.com/depth-camera-d435 "Intel RealSense D435") attached to one side of the gripper, in the simulator gazebo.

#### Requirements

- ros-melodic-librealsense2
- ros-melodic-realsense2-camera
- ros-melodic-realsense2-description
- https://github.com/justagist/panda_simulator

The software is tested on Ubuntu 18.04.6 LTS x86_64 with ROS Melodic, Gazebo 9 and Python 2.7.

## Singularity

To alleviate the burden of installing everything from scratch, i also provide a singularity container definition file [here](https://github.com/Mirko-Nava/panda_camera_gazebo_bundle/blob/main/container.def).
The container consists in a Ubuntu 18.04 system with the following installed.

- ZSH
- Python 2.7
- ROS Melodic
- Gazebo 9
- PyTorch 1.4.0 with CUDA support

It requires a binding between the container's home folder and the host's home folder, in which it will install the catkin workspace and the required ros packages.

The definition file is tested with singularity-ce version 3.9.1 on Ubuntu 18.04.6 LTS x86_64.

#### Installing singulairty

Please follow the instructions [here](https://sylabs.io/guides/3.9/user-guide/quick_start.html).

#### Running the container

Before running, you have to build the contrainer into an image file (.sif) using the following command.

```sh
singularity build --fakeroot container.sif container.def
```

To run the container with zsh use the following command.

```sh
singularity exec --cleanenv --contain --nv --bind /home/$USER container.sif /usr/bin/zsh
```

In order to setup the catkin workspace with the required ros packages, while inside the container's shell use the following commands.

```sh
mkdir -p $HOME/catkin_ws/src
cd $HOME/catkin_ws
source /opt/ros/melodic/setup.zsh
catkin init
source $HOME/catkin_ws/devel/setup.zsh
cd src
git clone -b melodic-devel https://github.com/justagist/panda_simulator
cd panda_simulator
./build_ws.sh
cd $HOME/catkin_ws/src
git clone -b main https://github.com/Mirko-Nava/panda_camera_gazebo_bundle
catkin build
source $HOME/catkin_ws/devel/setup.zsh
cd $HOME/catkin_ws
```

*Note: one needs to create the catkin workspace only once*
