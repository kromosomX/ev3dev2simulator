import sys
import unittest

from unittest.mock import MagicMock

from ev3dev2._platform.ev3 import INPUT_2
from ev3dev2simulator.config.config import load_config

load_config(None)

class SensorConnectorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.clientSocketModuleMock = MagicMock()
        sys.modules['ev3dev2simulator.connection.ClientSocket'] = cls.clientSocketModuleMock
        # you cannot import ClientSocket, since that sets up a connection

        cls.clientSocketMock = MagicMock()
        cls.clientSocketModuleMock.get_client_socket = lambda: cls.clientSocketMock

    @classmethod
    def tearDownClass(cls) -> None:
        del sys.modules['ev3dev2simulator.connection.ClientSocket']

    def tearDown(self):
        self.clientSocketMock.reset_mock()

    def test_leds_set_color(self):
        from ev3dev2.sensor.lego import ColorSensor

        self.clientSocketMock.send_command.return_value = 3
        sensor = ColorSensor(INPUT_2)
        val = sensor.value()
        self.assertEqual(val, 3)
        self.assertEqual(len(self.clientSocketMock.mock_calls), 1)
        fn_name, args, kwargs = self.clientSocketMock.mock_calls[0]
        self.assertEqual(fn_name, 'send_command')
        self.assertDictEqual(args[0].serialize(),
                             {'type': 'DataRequest', 'address': 'ev3-ports:in2'})

        val2 = sensor.value()
        self.assertEqual(len(self.clientSocketMock.mock_calls), 1)
        self.assertEqual(val, val2)


if __name__ == '__main__':
    unittest.main()