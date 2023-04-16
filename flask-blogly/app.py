"""Blogly application."""

from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


# GET /
@app.route('/')
def index():
    return redirect(url_for('show_users'))

# GET /users
@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('user_list.html', users=users)

# GET /users/new
@app.route('/users/new', methods=['GET'])
def new_user():
    return render_template('new_user.html')

# POST /users/new
@app.route('/users/new', methods=['POST'])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    user = User(first_name=first_name, last_name=last_name, email=email, image_url=image_url)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('show_users'))

# GET /users/[user-id]
@app.route('/users/<int:user_id>', methods=['GET'])
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('user_detail.html', user=user)

# GET /users/[user-id]/edit
@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit_user(user_id):
    user = User.query.get(user_id)
    return render_template('edit_user.html', user=user)

# POST /users/[user-id]/edit
@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    db.session.commit()
    return redirect(url_for('show_user', user_id=user_id))

# POST /users/[user-id]/delete
@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('show_users'))


# GET /users/[user-id]/posts/new
# Show form to add a post for that user.
@app.route('/users/[user-id]/posts/new', methods=['GET', 'POST'])
def new_post(user_id):
    user= User.query.get(user_id)
    if request.method=='POST':
        title=request.form('title')
        content=request.form('content')
        post= Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('user_profile'), user_id=user_id)
    return render_template('new_post', user=user)

# GET /posts/[post-id]
# Show a post.
@app.route('/posts/[post-id]')
def post_detail(post_id):
    post= Post.query.get(post_id)
    return render_template('post_detail', post=post)

# Show buttons to edit and delete the post.

# GET /posts/[post-id]/edit
# Show form to edit a post, and to cancel (back to user page).
# POST /posts/[post-id]/edit
# Handle editing of a post. Redirect back to the post view.

@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get(post_id)

    if request.method == 'POST':
        if request.form['submit'] == 'Save Changes':
            post.title = request.form['title']
            post.content = request.form['content']
            db.session.commit()
            flash('Post updated successfully!')
            return redirect(url_for('show_post', post_id=post_id))
        elif request.form['submit'] == 'Cancel':
            return redirect(url_for('show_user', user_id=post.user.id))
    return render_template('edit_post.html', post=post)


# POST /posts/[post-id]/delete
# Delete the post.
@app.route('/posts/[post-id]/delete', methods=['POST'])
def delete_post(post_id):
    post=Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('show_users'))