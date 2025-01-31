import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubNode(Node):
    def __init__(self):
        super().__init__("example_sub")
        self.create_subscription(String, "/pose", self.__callback, 10)

        self.__count = 0

    def __callback(self, _message: String):
        self.__count += 1
        print(f"Received: {self.__count}")


def main():
    rclpy.init()
    node = SubNode()
    rclpy.spin(node)
    rclpy.shutdown()
