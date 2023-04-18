"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.model):

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name =  db.Column(db.String(50),
                    nullable=False,
                    unique=False)
    last_name = db.Column(db.String(50),
                    nullable=False,
                    unique=False)
    image_url = db.Column(db.string,
                    default = "https://media.istockphoto.com/id/587805156/vector/profile-picture-vector-illustration.jpg?s=612x612&w=0&k=20&c=gkvLDCgsHH-8HeQe7JsjhlOY6vRBJk_sKW9lyaLgmLo=",
                    unique = False)              

class Post(db.model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
    title=db.Column(db.String(100))
    contents= db.Column(db.String, nullable=False)
    created_at=db.column(db.datetime, default = datetime.utcnow)
    user_id=db.column(db.integer, db.foreignkey('users.id'), nullable=False)

class Tag(db.model):
    __tablename__ = "tags"

    id = db.column(db.integer,
        primary_key=True,
        autoincrement=True)
    tag_name= db.column(db.string(20), 
        unique=True)
        
class PostTag(db.model):
    __tablename__='posttags'

    post_id=db.column(db.integer, 
        db.foriegnkey('posts.id'),
        nullable=False)

    tag_id=db.column(db.integer,
        db.foriegnkey('tags.id'),
        nullable=False)

    post=db.relationship('Post', back_populates='tags')

    tag=db.relationship('Tag', back_populates='posts')

    __table_args__= (db.UniqueConstraint('post_id', 'tag_id'))