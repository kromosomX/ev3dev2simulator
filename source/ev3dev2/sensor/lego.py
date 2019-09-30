# -----------------------------------------------------------------------------
# Copyright (c) 2015 Ralph Hempel <rhempel@hempeldesigngroup.com>
# Copyright (c) 2015 Anton Vanhoucke <antonvh@gmail.com>
# Copyright (c) 2015 Denis Demidov <dennis.demidov@gmail.com>
# Copyright (c) 2015 Eric Pascual <eric@pobot.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------

import sys

from ev3dev2.sensor.mock.MockColorSensor import MockColorSensor
from ev3dev2.sensor.mock.MockTouchSensor import MockTouchSensor

if sys.version_info < (3, 4):
    raise SystemError('Must be using Python 3.4 or higher')


class ColorSensor(MockColorSensor):

    def __init__(self, address, name_pattern=MockColorSensor.SYSTEM_DEVICE_NAME_CONVENTION, name_exact=False, **kwargs):
        super(ColorSensor, self).__init__(address, name_pattern, name_exact, **kwargs)


class TouchSensor(MockTouchSensor):

    def __init__(self, address, name_pattern=MockColorSensor.SYSTEM_DEVICE_NAME_CONVENTION, name_exact=False, **kwargs):
        super(TouchSensor, self).__init__(address, name_pattern, name_exact, **kwargs)