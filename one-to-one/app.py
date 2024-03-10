from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

db = SQLAlchemy(app)

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    child = db.relationship('Child',backref = 'parent',uselist=False)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, db.ForeignKey(Parent.id))


if __name__ == '__main__':
    
    app.run(debug=True)




