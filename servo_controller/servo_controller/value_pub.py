#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_custom_interfaces.msg import RT2String

class Pub(Node):

    def __init__(self):
        super().__init__('node_one')
        self.get_logger().info('Node 1 has begun')
        self.pub_node_one = self.create_publisher(RT2String, 'TOPIC_servo',10)
        self.timer = self.create_timer(0.1, self.publish_str)

    def publish_str(self):
        msg = RT2String()

        deg = input("Enter rotation value in degrees")
        msg.str = deg
        self.pub_node_one.publish(msg)


def main(args = None):
    rclpy.init(args=args)
    node = Pub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

main()