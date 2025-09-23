#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

"""Triggers a terrain change between scene1 and scene0 every 30 seconds in Unity."""

def main():
    rospy.init_node("terrain_trigger_publisher")
    pub = rospy.Publisher("/trigger_terrain_change", String, queue_size=10)

    rate = rospy.Rate(1.0 / 30.0)  # 1 message every 30 seconds
    toggle = False

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "scene_1" if toggle else "scene_0"
        rospy.loginfo("Publishing: %s", msg.data)
        pub.publish(msg)

        toggle = not toggle
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
