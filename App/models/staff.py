from App.database import db

class Staff(db.Model):
    staffID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    staffEmail = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', backref=db.backref('staff', uselist=False))

    def __init__(self, user_id, staffEmail):
        self.staffID = user_id
        self.staffEmail = staffEmail

    def get_json(self):
        return {
            'staffID': self.staffID,
            'staffEmail': self.staffEmail
        }