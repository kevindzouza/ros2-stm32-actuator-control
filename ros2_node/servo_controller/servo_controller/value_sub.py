#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import serial
from my_custom_interfaces.msg import RT2String

class Sub(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.get_logger().info("The Subscriber node has Begun")

        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0.1)

        self.sub_inform = self.create_subscription(
            RT2String,
            'TOPIC_servo',
            self.get_callback,
            10
        )

    def get_callback(self, msg):
        value = msg.str    # must be exactly 3 characters

        if (len(value) != 3) :
            self.get_logger().error(f"Invalid length: '{value}' — must be EXACTLY 3 characters")
            return

        data = value.encode()  # sends EXACT 3 bytes
        self.ser.write(data)

        self.get_logger().info(f"Sent 3 bytes: {data}")


def main(args=None):
    rclpy.init(args=args)
    node = Sub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()