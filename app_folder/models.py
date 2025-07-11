from app_folder import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "salary": self.salary
        }

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', salary={self.salary})>"