from unittest import TestCase

import dublinbus


class TestStop(TestCase):

    def test_is_string(self):
        s = dublinbus.print_stop('00353')
        self.assertTrue(isinstance(s, str))
