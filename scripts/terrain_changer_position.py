#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

"""Triggers a change in terrain between scene0 and scene1 in a Unity sim
at pre-determined locations within a Unity scene. This script was used 
for simulation experiments in the zero-to-autonomy-paper."""

class TerrainTriggerPublisher:
    def __init__(self):
        rospy.init_node("terrain_trigger_publisher")

        self.pub = rospy.Publisher("/trigger_terrain_change", String, queue_size=10)
        rospy.Subscriber("/warty/odom", Odometry, self.odom_callback)

        self.current_scene = "scene_0"  # Default

    def in_rectangle(self, x, y, x1, y1, x2, y2):
        """Check if (x, y) is inside the rectangle defined by (x1,y1) and (x2,y2)."""
        xmin, xmax = sorted([x1, x2])
        ymin, ymax = sorted([y1, y2])
        return xmin <= x <= xmax and ymin <= y <= ymax

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        # Define rectangles
        in_rect1 = self.in_rectangle(x, y, 26, 63, 71, 6)
        in_rect2 = self.in_rectangle(x, y, 112, 0, 135, 37)

        # Decide which scene
        new_scene = "scene_1" if (in_rect1 or in_rect2) else "scene_0"

        # Only publish if the scene changes
        if new_scene != self.current_scene:
            self.current_scene = new_scene
            msg_out = String(data=new_scene)
            rospy.loginfo("Position (%.2f, %.2f) -> Switching to %s", x, y, new_scene)
            self.pub.publish(msg_out)

    def run(self):
        rospy.spin()


if __name__ == "__main__":
    try:
        node = TerrainTriggerPublisher()
        node.run()
    except rospy.ROSInterruptException:
        pass
