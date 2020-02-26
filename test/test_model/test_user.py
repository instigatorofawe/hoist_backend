import unittest
import jwt
import config
from model.User import User


class TestUser(unittest.TestCase):
    def test_password(self):
        user = User(0, 'username')

        self.assertFalse(user.verify('password'))

        user.set_password('password')
        self.assertFalse(user.verify('another_password'))
        self.assertTrue(user.verify('password'))

        user.set_password('another_password')
        self.assertFalse(user.verify('password'))
        self.assertTrue(user.verify('another_password'))

    def test_auth_token(self):
        user = User(0, 'username')
        token = user.issue_token()
        decoded_token = jwt.decode(token, config.secret_key, algorithms='HS256')
        self.assertEqual(decoded_token['user'], 0)


if __name__ == '__main__':
    unittest.main()
