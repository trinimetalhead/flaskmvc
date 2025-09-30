from App.database import db

class Shortlist(db.Model):
    shortlistID = db.Column(db.Integer, primary_key=True)
    positionID = db.Column(db.Integer, db.ForeignKey('position.positionID'), nullable=False)
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'), nullable=False)

    def __init__(self, positionID, studentID, staffID):
        self.positionID = positionID
        self.studentID = studentID
        self.staffID = staffID

    def get_json(self):
        return {
            'shortlistID': self.shortlistID,
            'positionID': self.positionID,
            'studentID': self.studentID,
            'staffID': self.staffID
        }