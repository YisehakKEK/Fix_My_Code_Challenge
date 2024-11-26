import unittest
import importlib.util

spec = importlib.util.spec_from_file_location("User", "C:/Users/Hareg/Desktop/Fix_My_Code_Challenge/3-user.py")
user = importlib.util.module_from_spec(spec)
spec.loader.exec_module(user)
User = user.User

class TestUser(unittest.TestCase):
    def test_password_hashing(self):
        user = User()
        password = "testPassword"
        user.password = password
        self.assertNotEqual(user.password, password)

    def test_password_validation(self):
        user = User()
        password = "testPassword"
        user.password = password
        self.assertTrue(user.is_valid_password(password))
        self.assertFalse(user.is_valid_password("wrongPassword"))

    def test_unique_id(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_none_password(self):
        user = User()
        user.password = None
        self.assertIsNone(user.password)
        self.assertFalse(user.is_valid_password(None))

if __name__ == "__main__":
    unittest.main()
