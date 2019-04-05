#!/usr/bin/env python2

import unittest

from unittest_utils import loadHyQ, loadTalos, loadTalosArm, loadTiago, loadTiagoNoHand


class RobotTestCase(unittest.TestCase):
    ROBOT = None
    NQ = None
    NV = None

    def test_nq(self):
        model = self.ROBOT.model
        self.assertEqual(model.nq, self.NQ, "Wrong nq value.")

    def test_nv(self):
        model = self.ROBOT.model
        self.assertEqual(model.nv, self.NV, "Wrong nv value.")

    def test_q0(self):
        self.assertTrue(hasattr(self.ROBOT, "q0"), "It doesn't have q0")


class TalosArmTest(RobotTestCase):
    RobotTestCase.ROBOT = loadTalosArm()
    RobotTestCase.NQ = 7
    RobotTestCase.NV = 7


class TalosArmFloatingTest(RobotTestCase):
    RobotTestCase.ROBOT = loadTalosArm()
    RobotTestCase.NQ = 14
    RobotTestCase.NV = 13


class TalosTest(RobotTestCase):
    RobotTestCase.ROBOT = loadTalos()
    RobotTestCase.NQ = 39
    RobotTestCase.NV = 38


class HyQTest(RobotTestCase):
    RobotTestCase.ROBOT = loadHyQ()
    RobotTestCase.NQ = 19
    RobotTestCase.NV = 18


class TiagoTest(RobotTestCase):
    RobotTestCase.ROBOT = loadTiago()
    RobotTestCase.NQ = 50
    RobotTestCase.NV = 48


class TiagoNoHandTest(RobotTestCase):
    RobotTestCase.ROBOT = loadTiagoNoHand()
    RobotTestCase.NQ = 14
    RobotTestCase.NV = 12


if __name__ == '__main__':
    unittest.main()
