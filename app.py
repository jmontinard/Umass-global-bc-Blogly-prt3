
"""Blogly application."""

from flask import Flask, request, redirect, render_template,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post ,Tag
from datetime import datetime,date
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'
# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()

# home and err routes

@app.route("/")
def list_users():
    """redirecting  to list of all users"""
  
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template("homepage.html" , posts=posts)
  
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errorPage.html'), 404

# users routes

@app.route("/users")
def show_all_users():
    """returns a list of all users """
    users = User.query.order_by(User.last_name, User.first_name).all()
    
    return render_template("index.html", users=users)



@app.route("/users/new", methods=["GET"])
def add_users():
    """displays the route to show add user form """
    return render_template("addUser.html")


@app.route("/users/new", methods=["POST"])
def post_new_users():
    """add user and redirect to user lsit """
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    imgUrl = request.form['image_url']

    user = User(first_name=firstName, last_name=lastName, image_url=imgUrl)

    db.session.add(user)
    db.session.commit()
    flash(f"{user.get_fullname} has been added.")
    return redirect("/users")


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show all info on a selected user."""

    user = User.query.get_or_404(user_id)
    return render_template("userDetails.html", user=user)


@app.route("/users/<int:user_id>/edit")
def edit_users(user_id):
    """Edit info on a selected user."""

    user = User.query.get_or_404(user_id)
    return render_template("editUser.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def post_edit_users(user_id):
    """edits user and redirect to user lsit """
    user = User.get_or_404(user_id)
    # THIS BELOW WILL WORK IF WE NOT EXPLICILTY SETTIGN THE VALUE

    # firstName = request.form['first_name']
    # lastName = request.form['last_name']
    # imgUrl = request.form['image_url']
    # firstName = firstName if firstName != " " else user.first_name
    # lastName = lastName if lastName != " " else user.last_name
    # imgUrl = imgUrl if imgUrl != " " else user.image_url
    # firstName =  request.form['first_name'] or user.first_name
    # lastName = lastName if lastName != " " else user.last_name
    # imgUrl = imgUrl if imgUrl != " " else user.image_url
    # user.first_name = firstName
    # user.last_name = lastName
    # user.image_url =imgUrl


    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    # edited_user = User(first_name=firstName, last_name=lastName, image_url=imgUrl)
    print(user)
    db.session.add(user)
    db.session.commit()
    flash(f"{user.get_fullname} has been edited.")
    return redirect("/users")



@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_users(user_id):
    """displays name of deleted user and redirects user back to user list."""

    user = User.query.get_or_404(user_id)
    # User.query.filter_by(id=user.id).delete()
    db.session.delete(user)
    db.session.commit()
    flash(f"{user.get_fullname} has been deleted.")

    return redirect("/users")



 # routes for Posts

@app.route("/users/<int:user_id>/posts/new")
def show_post_form_user(user_id):
    """displays the route to show add post form """
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template("userPostForm.html", user=user, tags=tags )



@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_post_for_user(user_id):
    """collects data from  add post form """
    user = User.query.get_or_404(user_id)
    title = request.form["post_title"]
    content = request.form["post_content"]

    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    post = Post(title=title, content=content,
    user=user,  tags=tags)

    db.session.add(post)
    db.session.commit()
    flash(f"Post: {post.title} has been added.")
    return redirect(f"/users/{user_id}")


@app.route("/posts/<int:post_id>")
def show_post_details(post_id):
    """displays the route to show edit post form """
    post = Post.query.get_or_404(post_id)
    return render_template("postDetailsPage.html", post=post)



@app.route('/posts/<int:post_id>/edit')
def posts_details_edit(post_id):
    """Show a form to edit an existing post"""

    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    return render_template('editUserPostPage.html', post=post , tags=tags)



@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def show_post_details_edit(post_id):
    """updates the session with the data from the edit post form """

    post = Post.query.get_or_404(post_id)
 
    post.title = request.form["post_title"]
    post.content = request.form["post_content"]

    tag_ids = [int(num) for num in request.form.getlist("tags")]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    
    db.session.add(post)
    db.session.commit()
    flash(f"Post:{post.title} has been updated.")

    return redirect(f"/users/{post.user_id}")



@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    """deletes post and redirects user back to user posts."""
    post = Post.query.get_or_404(post_id)
    
    # Post.query.filter_by(id=post.id).delete()
    db.session.delete(post)
    db.session.commit()
    flash(f"Post: {post.title} has been deleted.")

    return redirect(f"/users/{post.user_id}")



# routes for all the tags

@app.route("/tags")
def list_tags():
    """List all tags and shows them"""
    tags = Tag.query.all()
    return render_template("list_tags.html", tags=tags)

@app.route("/tags/new")
def display_add_tag_form():
    """adds a new tag to the list"""
    
    posts = Post.query.all()
    return render_template("add_tag.html", posts=posts)  


@app.route("/tags/new", methods=["POST"])
def add_tag():
    """adds a new tag to the list"""

    post_ids = [int(num) for num in request.form.getlist("posts")]
    posts = Post.query.filter(Post.id.in_(post_ids)).all()

    tag = Tag(name=request.form["tag_name"],posts=posts)
    db.session.add(tag)
    db.session.commit()
    flash(f"Tag '{tag.name}' added.")
    return  redirect("/tags")  


@app.route("/tags/<int:tag_id>", methods=["GET"])
def display_tag(tag_id):
    """displays a tag page for selected tag"""
    tag = Tag.query.get_or_404(tag_id)
    return render_template("tagDisplayPage.html", tag=tag)  




@app.route("/tags/<int:tag_id>/edit", methods=["GET"])
def display_edit_tag_form(tag_id):
    """ displays edit selected tag form"""
    tag = Tag.query.get_or_404(tag_id)
    posts = Post.query.all()
    return render_template("display_tag_edit_form.html", tag=tag, posts=posts)    



@app.route("/tags/<int:tag_id>/edit", methods=["POST"])
def edit_tag(tag_id):
    """ edits selected tag"""
    tag = Tag.query.get_or_404(tag_id)
    tag.name =  request.form["tag_name"]
    post_ids = [int(num) for num in request.form.getlist("posts")]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

    db.session.add(tag)
    db.session.commit()
    flash(f"Tag '{tag.name}' edited.")
    return redirect(f"/tags")    


@app.route("/tags/<int:tag_id>/delete", methods=["POST"])
def delete_tag(tag_id):
    """ deletes selected tag"""
    tag = Tag.query.get_or_404(tag_id)
    # Post.query.filter_by(id=post.id).delete()
    # Tag.query.filter_by(id=tag.id).delete()
    db.session.delete(tag)
    db.session.commit()
    flash(f"Post: {tag.name} has been deleted.")
    return redirect("/tags")   




