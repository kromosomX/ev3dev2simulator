import math

import arcade

from simulator.obstacle import Obstacle
from simulator.robot import Robot
from simulator.util.Util import pythagoras


class BodyPart(arcade.Sprite):
    """
    Class containing the base functionality of a part of the robot.
    """


    def __init__(self,
                 address: str,
                 src: str,
                 scale: float,
                 robot: Robot,
                 delta_x: int,
                 delta_y: int):
        super(BodyPart, self).__init__(src, scale)

        self.address = address
        self.robot = robot
        self.center_x = robot.wheel_center_x + delta_x
        self.center_y = robot.wheel_center_y + delta_y

        self.angle_addition = -math.atan(delta_x / delta_y)
        self.sweep_length = pythagoras(delta_x, delta_y)

        if delta_y < 0:
            self.angle_addition += math.radians(180)

        self.sensible_obstacles = None


    def move_x(self, distance: float):
        """
        Move this part by the given distance in the x-direction.
        :param distance: to move
        """

        self.center_x += distance


    def move_y(self, distance: float):
        """
        Move this part by the given distance in the y-direction.
        :param distance: to move
        """

        self.center_y += distance


    def rotate(self, radians: float):
        """
        Rotate this part by the given angle in radians. Make sure it
        stays 'attached' to its body by also adjusting its x and y values.
        :param radians: to rotate.
        """

        self.angle += math.degrees(radians)

        rad = math.radians(self.angle) + self.angle_addition

        self.center_x = self.sweep_length * math.sin(-rad) + self.robot.wheel_center_x
        self.center_y = self.sweep_length * math.cos(-rad) + self.robot.wheel_center_y


    def set_sensible_obstacles(self, obstacles: [Obstacle]):
        """
        Set the obstacles which can be detected via collision detection by this body part.
        :param obstacles: to be detected.
        """

        self.sensible_obstacles = obstacles
