from unittest import TestCase

from app import app
from models import db, User,Post,PostTag,Tag

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.drop_all()
db.create_all()


class UserModelsTestcase(TestCase):
    """Tests for User Models"""

    def setUp(self):
        """clean all previous users"""
        User.query.delete()
        print('inside teardown')


        print('inside tearup')
    def tearDown(self):
        """clean all transactions"""
        User.query.rollback()
        print('inside teardown')


    # def test__repr__(self):
    #     """test function for functionality"""
    #     u = User(first_name="John", last_name="Doe",
    #              image_url="www.google.com")
    #     db.session.add()
    #     self.assertEquals(
    #         User.__repr__(), "User id=1 firstname=John lastname=Doe imgUrl =www.google.com")

    def test_get_full_name(self):
        """test function for functionality"""
        u = User(first_name="John", last_name="Doe",
                 image_url="www.google.com")
        db.session.add(u)
        db.session.commit()

        self.assertEquals(u.get_full_name(), "John Doe")

class PostModelsTestcase(TestCase):
    """Tests for User Models"""

    def setUp(self):
        """clean all previous users"""
        Post.query.delete()
        print('inside teardown')


        print('inside tearup')
    def tearDown(self):
        """clean all transactions"""
        Post.query.rollback()
        print('inside teardown')


    def test_friendly_date(self):
        """test function for functionality"""
        p = Post(title="first post",content="content")
        db.session.add(p)
        db.session.commit()

        self.assertEquals(p.friendly_date(), "Sun Oct 1 2023, 9:19 AM")

#         # do a test page for 4 our our routes
# import unittest
# from flask import Flask
# from your_module import db, connect_db, User, Post, Tag, PostTag
# import datetime

# Assuming your module containing the code is named "your_module"
# import unittest
# from flask import Flask
# from models import db, connect_db, User, Post, Tag, PostTag
# from app import app
# import datetime

# class TestBloglyModels(unittest.TestCase):

#     def setUp(self):
#         # Create a test Flask application and configure it for testing
#         app = Flask(__name__)
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#         # Initialize the test database
#         db.init_app(app)
#         connect_db(app)

#         # Create the database tables
#         with app.app_context():
#             db.create_all()

#     def tearDown(self):
#         # Clean up the test database after each test
#         with app.app_context():
#             db.drop_all()

#     def test_user_model(self):
#         # Create a sample user
#         user = User(first_name='John', last_name='Doe')
#         db.session.add(user)
#         db.session.commit()

# import unittest
# from flask import Flask
# from models import db, connect_db, User, Post, Tag, PostTag
# from app import app
# import datetime

# # Assuming your module containing the code is named "your_module"

# class TestBloglyModels(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         # Create a test Flask application and configure it for testing
#         cls.app = Flask(__name__)
#         cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#         cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#         # Initialize the test database
#         db.init_app(cls.app)
#         connect_db(cls.app)

#         # Create the database tables
#         with cls.app.app_context():
#             db.create_all()

#     @classmethod
#     def tearDownClass(cls):
#         # Clean up the test database after all tests have run
#         with cls.app.app_context():
#             db.drop_all()

#     def setUp(self):
#         # Create a new database session for each test
#         self.client = self.app.test_client()
#         with self.app.app_context():
#             db.create_all()

#     def tearDown(self):
#         # Close the database session after each test
#         with self.app.app_context():
#             db.session.remove()





#         # Retrieve the user from the database
#         retrieved_user = User.query.get(user.id)

#         # Assert that the retrieved user matches the created user
#         self.assertEqual(retrieved_user.first_name, 'John')
#         self.assertEqual(retrieved_user.last_name, 'Doe')
#         self.assertEqual(retrieved_user.get_fullname, 'John Doe')

#     def test_post_model(self):
#         # Create a sample user
#         user = User(first_name='Alice', last_name='Smith')
#         db.session.add(user)
#         db.session.commit()

#         # Create a sample post
#         post = Post(title='Test Post', content='This is a test post', user_id=user.id)
#         db.session.add(post)
#         db.session.commit()

#         # Retrieve the post from the database
#         retrieved_post = Post.query.get(post.id)

#         # Assert that the retrieved post matches the created post
#         self.assertEqual(retrieved_post.title, 'Test Post')
#         self.assertEqual(retrieved_post.content, 'This is a test post')
#         self.assertIsInstance(retrieved_post.created_at, datetime.datetime)
#         self.assertEqual(retrieved_post.user_id, user.id)
#         self.assertEqual(retrieved_post.friendly_date, retrieved_post.created_at.strftime("%a %b %-d %Y, %-I:%M %p"))

#     def test_tag_model(self):
#         # Create a sample tag
#         tag = Tag(name='TestTag')
#         db.session.add(tag)
#         db.session.commit()

#         # Retrieve the tag from the database
#         retrieved_tag = Tag.query.get(tag.id)

#         # Assert that the retrieved tag matches the created tag
#         self.assertEqual(retrieved_tag.name, 'TestTag')

# if __name__ == '__main__':
#     unittest.main()
