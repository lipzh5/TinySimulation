# TinySimulation
## assets
Contains the resources (.urdf files) to load 

## outputs
Contains observations (saved as image or video) of the simulation environment.

## [`const.py`](...)
- asset names, download urls and other predifined settings 

## [`PickPlaceEnv.py`](...)
- contains the main control flow of the simulation environment: reset, execute action, render image etc.

## [`Robotiq2F85.py`](...)
- gripper's primitive motions

## [`runenv.py`](...)
- entry point, and t**he file you are going to manipulate**. 
- **comments** in this file give you hints on how to modify
