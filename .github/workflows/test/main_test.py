from main import get_weather
import unittest
from unittest.mock import patch

class Test(unittest, Testcase):
@patch("main.request.get")
def test_get_weather(mock_get):
    mock_get.return_value.json.return_value = {"temperature":22}
    result = get_weather()
    self.assertTrue(resulr,22)

if_name_ == '_main_':
    unittest.main()