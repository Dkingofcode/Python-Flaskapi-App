from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import linked_list
import hashtable

# app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key constriants
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

db = SQLAlchemy(app)
now = datetime.now()


#models
class User(db.Model):
    __tablename__  = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade= "all, delete")

class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# routes
@app.route('/user', methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data['email'],
        address=data['address'],
        phone=data['phone'], 
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({ "message": "User created" }), 200

    

@app.route('/user/descending_id', methods=["GET"])
def get_all_users_descending():
    users = User.query.all()
    new_users_ll = linked_list.LinkedList()
     
    for user in users:
        new_users_ll.insert_beginning(
            {
              "id": user.id,
              "name": user.name,
              "email": user.email,
              "address": user.address,
              "phone": user.phone,
            }
        )

    return jsonify(new_users_ll.tolist()), 200



@app.route('/user/ascending_id', methods=["GET"])
def get_all_users_ascending():
    users = User.query.all()
    new_users_ll = linked_list.LinkedList()
     
    for user in users:
        new_users_ll.insert_at_end(
            {
              "id": user.id,
              "name": user.name,
              "email": user.email,
              "address": user.address,
              "phone": user.phone,
            }
        )

    return jsonify(new_users_ll.tolist()), 200

    pass


@app.route('/user/<user_id>', methods=["GET"])
def get_one_user_(user_id):
    users = User.query.all()
    new_users_ll = linked_list.LinkedList()
     
    for user in users:
        new_users_ll.insert_beginning(
            {
              "id": user.id,
              "name": user.name,
              "email": user.email,
              "address": user.address,
              "phone": user.phone,
            }
        )
         
    return jsonify(new_users_ll.get_user_by_id(user_id)), 200

    
    
    
    pass

@app.route('/user/<user_id>', methods=["DELETE"])
def delete_user(user_id):
   user = User.query.filter_by(id=user_id).first()
   db.session.delete(user)
   db.session.commit()
   return jsonify({}), 200

   pass

@app.route('/blog_post/<user_id>', methods=["POST"])
def create_blog_post_(user_id):
   data = request.get_json()

   user = User.query.filter_by(id=user_id).first()
   if not user:
         return jsonify({ "message": "user does not exist!" }), 400
   
   ht = hashtable.HashTable(10)
   
   ht.add_key_value("title", data["title"])
   ht.add_key_value("body", data["body"])
   ht.add_key_value("date", now)
   ht.add_key_value("user_id", user_id)

   ht.print_table()

@app.route('/blog_post/<blog_post_id>', methods=["GET"])
def get_all_blog_posts(user_id):
   blog_posts = BlogPost.query.all()
   random.shuffle(blog_posts)

   bst = binary_search_tree.BinarySearchTree()

   for post in blog_posts:
    bst.insert({
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "user_id": post.user_id,
    })
   post  = bst.search(blog_post_id)
   
   if not post:
        return jsonify({ "message": "post not found" })
   return jsonify(post) 
    


@app.route('/blog_post/<blog_post_id>', methods=["GET"])
def get_one_blog_post(blog_post_id):
    pass


@app.route('/blog_post/<blog_post_id>', methods=["DELETE"])
def delete_blog_post(blog_post_id):
    pass







