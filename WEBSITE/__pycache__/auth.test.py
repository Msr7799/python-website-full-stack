import unittest
from flask import Flask
from WEBSITE.auth import auth

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.register_blueprint(auth)
        self.client = self.app.test_client()

if __name__ == '__main__':
    unittest.main()
