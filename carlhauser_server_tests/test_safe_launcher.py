# -*- coding: utf-8 -*-
import logging
import time
import unittest

from carlhauser_server.safe_launcher import SafeLauncher


class InfiniteLooper:

    def __init__(self):
        self.test = None
        self.safe_stopped = False

    @staticmethod
    def start():
        n = 0
        while n < 5 :
            print("test")
            time.sleep(1)
            n += 1

    def stop(self):
        self.safe_stopped = True

class testCarlHauserServer(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        self.logger = logging.getLogger()

    def tearDown(self):
        # Launch shutdown AND FLUSH script
        # self.test_db_handler.tearDown()
        pass

    def test_absolute_truth_and_meaning(self):
        self.assertTrue(True)

    def test_safe_launcher(self):

        il = InfiniteLooper()
        sf = SafeLauncher(il, "start", "stop")

        # TODO : Find a way to kill the process ? See if it clean up behind him ?

        sf.launch(auto_stop=True)

        sf.stop()

        self.assertEqual(il.safe_stopped, True)


if __name__ == '__main__':
    unittest.main()
