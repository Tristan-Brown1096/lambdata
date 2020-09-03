"""Basic unit tests for the in-class examples of the lambdata package"""

import unittest
from random import randint
from example_module import increment, FAVORITE_COLORS
from oop_examples import SocialMediaUser

class ExampleTests(unittest.TestCase):
    """Making sure examples work as expected."""
    def test_incriment(self):
        """Testing that increment adds one to a number."""
        x0 = 0
        y0 = increment(x0)
        self.assertEqual(y0, 1)
        x1 = 123
        y1 = increment(x1)
        self.assertEqual(y1, 124)
        x2 = -57
        y2 = increment(x2)
        self.assertEqual(y2, -56)

    def test_favorite_colors(self):
        """Testing presence/absence of members of a collection."""
        self.assertIn('red', FAVORITE_COLORS)
        self.assertNotIn('auburn', FAVORITE_COLORS)
    
    def test_number_colors(self):
        """Testing that we have the expected number of colors."""
        self.assertEqual(len(FAVORITE_COLORS), 6)


class SocialMediaUserTests(unittest.TestCase):
    """Tests the usage of SocialMediaUser."""
    def setUp(self):
        """Common set up code run before all tests."""
        self.user1 = SocialMediaUser('Jane', 'Denmark')
        self.user2 = SocialMediaUser('Joe', 'Russia')

    def test_name(self):
        self.assertEqual(self.user1.name, 'Jane')
        self.assertEqual(self.user2.name, 'Joe')
    def test_location(self):
        self.assertEqual(self.user1.location, 'Denmark')
        self.assertEqual(self.user2.location, 'Russia')

    def test_default_upvotes(self):
        new_user = SocialMediaUser('Maria', 'Spain')
        self.assertEqual(new_user.upvotes, 0)
    
    def test_unpopular(self):
        """Test that a user with <=100 upvotes is not popular."""
        new_user = SocialMediaUser('Bryce', 'US')
        self.assertFalse(new_user.is_popular())
        for _ in range(randint(1, 100)):
            new_user.receive_upvote()
        self.assertFalse(new_user.is_popular())


if __name__ == '__main__':
    unittest.main()