#!/usr/bin/env python3

import random

import rospy
import rospkg
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose, Point, Quaternion

rospy.init_node('insert_object',log_level=rospy.INFO)

# get an instance of RosPack with the default search paths
rospack = rospkg.RosPack()
package_path = rospack.get_path('psr_apartment_description') + '/description/models/'


#Add here mode poses
placements = []
placements.append({'pose':Pose(position=Point(x=-5.69, y=4.37, z=0.6), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'large_bedroom', 'place': 'bed'})
placements.append({'pose':Pose(position=Point(x=-7.33, y=5.29, z=0.58), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'large_bedroom', 'place': 'bedside_cabinet'})


model_names = ['sphere_v']

# Add here several models. All should be added to the robutler_description package
model_name = random.choice(model_names)

f = open( package_path + model_name + '/model.sdf' ,'r')
sdff = f.read()

rospy.wait_for_service('gazebo/spawn_sdf_model')
spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)


model_placement = random.choice(placements)
name = model_name + '_in_' + model_placement['place'] + '_of_' + model_placement['room']
spawn_model_prox(name, sdff, model_name, model_placement['pose'], "world")