from App.database import db

class Student(db.Model):
    studentID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    studentName = db.Column(db.String(100), nullable=False)
    studentEmail = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', backref=db.backref('student', uselist=False))

    def __init__(self, user_id, studentName, studentEmail):
        self.studentID = user_id
        self.studentName = studentName
        self.studentEmail = studentEmail

    def get_json(self):
        return {
            'studentID': self.studentID,
            'studentName': self.studentName,
            'studentEmail': self.studentEmail
        }