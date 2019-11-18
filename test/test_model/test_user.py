import unittest
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



if __name__ == '__main__':
    unittest.main()
