from App.database import db

class Position(db.Model):
    positionID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    employerID = db.Column(db.Integer, db.ForeignKey('employer.employerID'), nullable=False)

    def __init__(self, title, description, requirements, employerID):
        self.title = title
        self.description = description
        self.requirements = requirements
        self.employerID = employerID

    def get_json(self):
        return {
            'positionID': self.positionID,
            'title': self.title,
            'employerID': self.employerID
        }