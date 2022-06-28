import unittest
from Mockserver.api_call import api_call
from unittest.mock import patch

class TestApiCall(unittest.TestCase):
    def test_api_call(self):
        actual_result=api_call("https://www.youtube.com/watch?v=1KZK1pTkmP0")
        assert actual_result["shorten_url"]=="http://127.0.0.1:5000/Kxk0iGKb"
    
if __name__ == '__main__':
    unittest.main()