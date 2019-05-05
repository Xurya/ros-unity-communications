# ros-unity-communications
Post-Processing JPG Encoding from Unity to ROS for use in Rviz

Testing can be run using attached Rosbag, which contains the raw data from ROS# from the original testing scene.

### Setup for actual testing scene:
1. In Unity, connect the target camera with ROS using a rosbridge, documentation can be found on the ROS# repository. 
   (If using a VM, make sure to configure the localhost, ie. have a seperate IP address on the VM for easier connection.)
2. In ROS, you can now use the image converter just like the Rosbag, you must make sure the topic in the program matches the 
   intended Unity topic, you can double check using `rostopic list`.
