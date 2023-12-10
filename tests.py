import unittest
from main import clean_usernames


class Test(unittest.TestCase):

    def setUp(self):
        # Setup for the tests
        self.test_followers = set(clean_usernames('followers.txt'))
        self.test_following = set(clean_usernames('following.txt'))

    def test_following(self):
        # Test if specific users are followed
        self.assertIn('kyliejenner', self.test_following)

    def test_followers(self):
        # Test if specific users are followers
        self.assertIn('fuad.hossain', self.test_followers)

    def test_non_followers(self):
        # Test for non-followers
        non_followers = self.test_following - self.test_followers
        self.assertIn('kyliejenner', non_followers)
        self.assertNotIn('fuad.hossain', non_followers)


if __name__ == '__main__':
    unittest.main()
