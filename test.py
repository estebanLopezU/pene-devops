import unittest
import json
from main import app

class FlaskApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app= app.test_cliente()
        self.app.testing= True
    def test_suma(self):
        response = self.app.get('/suma?a=2&b=3')
        data= json.loads(response.data)
        self.assertEqual(dara['resultado'],5)
    def test_multiplica(self):
        response =Self.app.post('/multiplica', json={'a':4,'b':5})
        data = json.loads(response.data)
        self.assertEqual(data['resultado'],20)
if __name__=='__main__':
    unittest.main()