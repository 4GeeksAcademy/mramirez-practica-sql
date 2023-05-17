from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_student = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    programming_skills = db.Column(db.Boolean)

    def __repr__(self):
        return '<Student %r>' % self.name_student

    def serialize(self):
        return {
            "id": self.id,
            "name_student": self.name_student,
            "email": self.email,
            "programming_skills": self.programming_skills
        } 