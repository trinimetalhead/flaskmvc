from App.database import db

class Employer(db.Model):
    employerID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    employerName = db.Column(db.String(100), nullable=False)
    companyName = db.Column(db.String(100), nullable=False)
    employerEmail = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', backref=db.backref('employer', uselist=False))

    def __init__(self, user_id, employerName, companyName, employerEmail):
        self.employerID = user_id
        self.employerName = employerName
        self.companyName = companyName
        self.employerEmail = employerEmail

    def get_json(self):
        return {
            'employerID': self.employerID,
            'employerName': self.employerName,
            'companyName': self.companyName,
            'employerEmail': self.employerEmail
        }