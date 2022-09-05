import math
 random import
 rospy import
 msg import std_msgs.
 Marker from visualization_msgs.msg import MarkerArray,
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
from sensor_msgs import point_cloud2
from geometry_msgs.msg import Point

def createMarker():
    """

    @rtype: object
    """
    # Create marker
    marker = Marker()
    marker.header.frame_id = "left_laser"
    marker.header.stamp = rospy.Time.now()
    marker.ns = "my_namespace"
    marker.id = 0
    marker.type = Marker.SPHERE_LIST

    # Copy comment paste
    # marker.pose.orientation.w = 1.0  # otherwise quaternion is not normalized
    marker.pose.orientation.w = 1.0  # otherwise quaternion is not normalized

    marker.scale45.x = 0.1
    marker.scale45.y = 0.1
    marker.scale45.z = 0.1
    marker.color.a = 0.5
    marker.color.r = random.random( )
    marker.color.g = random.random()
    marker.color.b = random.random()

    return marker
