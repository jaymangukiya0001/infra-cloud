import unittest
from Mockserver.api_call import api_call
from unittest.mock import patch

class TestApiCall(unittest.TestCase):
    def test_api_call(self):
        actual_result=api_call("https://www.youtube.com/watch")
        assert actual_result["shorten_url"]=="https://bit.ly/3OnEhPb"
    
if __name__ == '__main__':
    unittest.main()