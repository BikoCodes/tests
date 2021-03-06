import unittest
from unittest.mock import Mock
import requests
from requests.api import request

from requests.exceptions import Timeout

from my_calendar import get_holidays

#Mock requests to control its behavior
requests = Mock()


class TestCalendar(unittest.TestCase):

    def test_get_holidays_retry(self):
        
        #Create a new Mock to imitate a Response

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }

        # Set the side effect of .get()
        requests.get.side_effect = [Timeout, response_mock]

        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()

        # Now retry, expecting a successful response
        assert get_holidays()['12/25'] == 'Christmas'

        # Finally, assert .get() was called twice
        assert requests.get.call_count == 2

if __name__ == '__main__':
    unittest.main()

