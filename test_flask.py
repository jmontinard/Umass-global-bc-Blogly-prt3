from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.drop_all()
db.create_all()


class UserModelsTestcase(TestCase):
    """Tests for User Models"""

    def setUp(self):
        """clean all previous users"""
        User.query.delete()

    def tearDown(self):
        """clean all transactions"""
        User.query.rollback()

    def test__repr__(self):
        """test function for functionality"""
        u = User(first_name="John", last_name="Doe",
                 image_url="www.google.com")
        self.assertEquals(
            User.__repr__(), "User id=1 firstname=John lastname=Doe imgUrl =www.google.com")

    def test_get_full_name(self):
        """test function for functionality"""
        u = User(first_name="John", last_name="Doe",
                 image_url="www.google.com")
        self.assertEquals(User.get_full_name(), "John Doe")


        # do a test page for 4 our our routes
