from user_ms import db
import json

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    role = db.Column(db.Integer)
    status = db.Column(db.Integer)
    teacher_token = db.Column(db.String)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit() 

    def __repr__(self):
        return f"<User (user_id {self.user_id}, first_name {self.first_name}, last_name {self.last_name}, created_at {self.created_at}, role {self.role}, status {self.status})>"