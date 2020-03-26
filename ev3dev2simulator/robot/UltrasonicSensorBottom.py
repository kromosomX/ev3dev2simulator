from ev3dev2simulator.config.config import get_simulation_settings
from ev3dev2simulator.robot.BodyPart import BodyPart


class UltrasonicSensorBottom(BodyPart):
    """
    Class representing an UltrasonicSensor of the simulated robot mounted towards the ground.
    """
    def __init__(self,
                 brick: int,
                 address: str,
                 robot,
                 delta_x: int,
                 delta_y: int,
                 name: str):
        dims = get_simulation_settings()['body_part_sizes']['ultrasonic_sensor_bottom']
        super(UltrasonicSensorBottom, self).__init__(brick, address, robot, delta_x, delta_y,
                                                     dims['width'], dims['height'], 'ultrasonic_sensor')
        self.name = name

    def setup_visuals(self, scale):
        img_cfg = get_simulation_settings()['image_paths']
        self.init_texture(img_cfg['ultrasonic_sensor_bottom'], scale)

    def get_latest_value(self):
        return self.distance()

    def distance(self) -> float:
        """
        Get the distance in pixels between this ultrasonic sensor and an the ground.
        :return: a floating point value representing the distance.
        """
        for o in self.sensible_obstacles:
            if o.collided_with(self.center_x, self.center_y):
                return self.get_default_value()

        return 20

    def get_default_value(self):
        """
        1 pixel == 1mm so measurement values this sensor returns are one to one mappable to millimeters.
        Max distance real world robot ultrasonic sensor returns is 2550mm.
        :return: default value in pixels.
        """
        return 2550
