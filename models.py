"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



"""Models for Blogly."""

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    first_name = db.Column(db.Text,
                     nullable=False)
    last_name = db.Column(db.Text,
                     nullable=False)
    image_url = db.Column(db.Text,
                     nullable= False,
                     default='https://images.unsplash.com/photo-1525357816819-392d2380d821?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80')
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")
    # @property
    # def __repr__(self):
    #     u = self
    #     return f"<User id={u.id} firstname={u.first_name} lastname={u.last_name} imgUrl ={u.image_url} >"
    #     # see if you need classmethod?z

    @property    
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"



class Post(db.Model):
     __tablename__ = 'posts'
     id = db.Column(db.Integer,
                   primary_key=True)
     title = db.Column(db.Text,
                     nullable=False)
     content = db.Column(db.Text,
                     nullable=False)
     created_at = db.Column(db.DateTime,
                     nullable=False,
                     default=datetime.datetime.now)

    #  user = db.relationship('User', backref='posts')


     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

     @property
     def friendly_date(self):
         """Return nicely-formatted date."""
         return self.created_at.strftime("%a %b %-d %Y, %-I:%M %p")




class PostTag(db.Model):
     __tablename__ = 'posts_tags'
     post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
     tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)



class Tag(db.Model):
     __tablename__ = 'tags'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.Text, nullable=False,unique=True)  

     posts = db.relationship(
        'Post',
        secondary="posts_tags",
        # cascade="all,delete",
        backref="tags",
    )

