
# from unittest import TestCase


# from app import app
# from models import db, User, Post,Tag,PostTag


# # Use test database and don't clutter tests with SQL make this test
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
# app.config['SQLALCHEMY_ECHO'] = False


# # Make Flask errors be real errors, rather than HTML pages with error info
# app.config['TESTING'] = True


# # This is a bit of hack, but don't use Flask DebugToolbar
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


# db.drop_all()
# db.create_all()


# DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


# class PetViewsTestCase(TestCase):
#    """Tests for views for Pets."""


#    def setUp(self):
#        """Add sample pet."""


#        User.query.delete()


#        u = User(first_name="John",last_name="Doe", image_url= DEFAULT_IMAGE_URL) 
#     #    // maybe ddd post
#        db.session.add(u)
#        db.session.commit()


#        self.user_id = u.id


#    def tearDown(self):
#        """Clean up any fouled transaction."""


#        db.session.rollback()


#    def test_users_index(self):
#         " see if users returns u"
#         with app.test_client() as client:
#            resp = client.get("/users")
#            html = resp.get_data(as_text=True)




#            self.assertEqual(resp.status_code, 200)
#            self.assertIn('John Doe', html)




#    def test_users_new_get(self):
#         " see if users returns new test u"
#         with app.test_client() as client:
#            resp = client.get("/users/new")
#            html = resp.get_data(as_text=True)


#            self.assertEqual(resp.status_code, 200)
#            self.assertIn('<h1>Create a user</h1>', html)




#            # test redirect


#    def test_users_new_post(self):
#        " see if new users adds test u"
#        with app.test_client() as client:
#            d = {"first_name":"Jane","last_name":"Doe", "image_url": DEFAULT_IMAGE_URL}
#            resp = client.post("/users/new", data=d, follow_redirects=True)
#            html = resp.get_data(as_text=True)


#            self.assertEqual(resp.status_code, 200)
#            self.assertIn("<a>Jane Doe</a>", html) 


#    def test_user_show(self):
#        " see if users  display page works"
#        with app.test_client() as client:
#            resp = client.get(f"/users/{self.u_id}")
#            html = resp.get_data(as_text=True)


#            self.assertEqual(resp.status_code, 200)
#            self.assertIn('<h1>John Doe</h1>', html)


#    def test_users_edit_get(self):
#        " see if users  edit form is returned"
#        with app.test_client() as client:
#            resp = client.get("/users/{self.u_id}/edit")
#            html = resp.get_data(as_text=True)


#            self.assertEqual(resp.status_code, 200)
#            self.assertIn('<label>First Name</label>', html)


#    def test_users_edit_post(self):
#        " see if  users  is edited and takes effect"
#        with app.test_client() as client:
           
#            d = {"first_name":"Jake","last_name":"Doe", "image_url": DEFAULT_IMAGE_URL}
#            resp = client.post("/users/new", data=d, follow_redirects=True)
#            html = resp.get_data(as_text=True)


#            self.assertEqual(resp.status_code, 200)
#            self.assertIn("<a>Jake Doe</a>", html)

#    def test_users_delete(self):
#        " see if  users  is deleted and takes effect"

#     # post 














   # def test_list_pets(self):
   #     with app.test_client() as client:
   #         resp = client.get("/")
   #         html = resp.get_data(as_text=True)


   #         self.assertEqual(resp.status_code, 200)
   #         self.assertIn('TestPet', html)


   # def test_show_pet(self):
   #     with app.test_client() as client:
   #         resp = client.get(f"/{self.pet_id}")
   #         html = resp.get_data(as_text=True)


   #         self.assertEqual(resp.status_code, 200)
   #         self.assertIn('<h1>TestPet</h1>', html)


   # def test_add_pet(self):
   #     with app.test_client() as client:
   #         d = {"name": "TestPet2", "species": "cat", "hunger": 20}
   #         resp = client.post("/", data=d, follow_redirects=True)
   #         html = resp.get_data(as_text=True)


   #         self.assertEqual(resp.status_code, 200)
   #         self.assertIn("<h1>TestPet2</h1>", html)
import unittest
from flask import Flask
from models import db, connect_db, User, Post, Tag, PostTag
from app import app
import datetime

# Assuming your module containing the code is named "your_module"

class TestBloglyModels(unittest.TestCase):

   @classmethod
   def setUpClass(cls):
        # Create a test Flask application and configure it for testing
        cls.app = Flask(__name__)
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Initialize the test database
        db.init_app(cls.app)
        connect_db(cls.app)

        # Create the database tables
        with cls.app.app_context():
            db.create_all()

   @classmethod
   def tearDownClass(cls):
        # Clean up the test database after all tests have run
        with cls.app.app_context():
            db.drop_all()

   def setUp(self):
        # Create a new database session for each test
        self.client = self.app.test_client()

        # Establish the application context for the test
        self.app_context = self.app.app_context()
        self.app_context.push()

   def tearDown(self):
        # Close the database session after each test
        with self.app_context:
            db.session.remove()
        
        # Pop the application context after the test
        self.app_context.pop()

    # Your test methods go here...




# class PetViewsTestCase(TestCase):
#    """Tests for views for Pets."""


   def setUp(self):
       """Add sample pet."""


       User.query.delete()


       u = User(first_name="John",last_name="Doe", image_url= DEFAULT_IMAGE_URL) 
    #    // maybe ddd post
       db.session.add(u)
       db.session.commit()


       self.user_id = u.id


   def tearDown(self):
       """Clean up any fouled transaction."""


       db.session.rollback()


   def test_users_index(self):
        " see if users returns u"
        with app.test_client() as client:
           resp = client.get("/users")
           html = resp.get_data(as_text=True)




           self.assertEqual(resp.status_code, 200)
           self.assertIn('John Doe', html)




   def test_users_new_get(self):
        " see if users returns new test u"
        with app.test_client() as client:
           resp = client.get("/users/new")
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn('<h1>Create a user</h1>', html)




           # test redirect


   def test_users_new_post(self):
       " see if new users adds test u"
       with app.test_client() as client:
           d = {"first_name":"Jane","last_name":"Doe", "image_url": DEFAULT_IMAGE_URL}
           resp = client.post("/users/new", data=d, follow_redirects=True)
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn("<a>Jane Doe</a>", html) 


   def test_user_show(self):
       " see if users  display page works"
       with app.test_client() as client:
           resp = client.get(f"/users/{self.u_id}")
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn('<h1>John Doe</h1>', html)


   def test_users_edit_get(self):
       " see if users  edit form is returned"
       with app.test_client() as client:
           resp = client.get(f"/users/{self.u_id}/edit")
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn('<label>First Name</label>', html)


   def test_users_edit_post(self):
       " see if  users  is edited and takes effect"
       with app.test_client() as client:
           
           d = {"first_name":"Jake","last_name":"Doe", "image_url": DEFAULT_IMAGE_URL}
           resp = client.post("/users/new", data=d, follow_redirects=True)
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn("<a>Jake Doe</a>", html)

  
   def test_users_delete(self):
       " see if  users  is deleted and takes effect"
       with app.test_client() as client:
           u2 = User.query.get_or_404(2)
           resp = client.get(f"/users/{u2.id}/delete")
           html = resp.get_data(as_text=True, follow_redirects=True, )


           self.assertEqual(resp.status_code, 200)
           self.assertFalse("<a>Jake Doe</a>", html)
    # post 

   def test_users_post(self):
       " see if new post form is generated"
       with app.test_client() as client:
        #    tags = Tag.query.all()
        #    self.user_id.tags = tags

           resp = client.get(f"/users/{self.u_id}/posts/new")
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn('<h1>Add Post for Jake Doe</h1>', html)

   def test_user_posted(self):
       " see if new post is added"
       with app.test_client() as client:
           
           d = {"title":"first post","content":"content"}
           resp = client.post(f"/users/{self.u_id}/posts/new", data=d, follow_redirects=True)
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn("<a>First Post</a>", html)
   
   def test_post_display(self):
       " see if post  display page works"
       with app.test_client() as client:
           resp = client.get("/post/1")
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn('<h1>First Post</h1>', html)

#    tags

   def test_add_tag(self):
       " see if new post form is generated"
       with app.test_client() as client:
           
           resp = client.get("/tags/new")
           html = resp.get_data(as_text=True)


           self.assertEqual(resp.status_code, 200)
           self.assertIn('<h1>Create a tag</h1>', html)