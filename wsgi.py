import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Employer, Position, Shortlist
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Student Commands
'''

# create a group, it would be the first argument of the comand
# eg : flask student <command>
student_cli = AppGroup('student', help='Student object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@student_cli.command("create", help="Creates a student")
@click.argument("username", default="student1")
@click.argument("password", default="studentpass")
@click.argument("name", default="John Doe")
@click.argument("email", default="john@student.com")
def create_student_command(username, password, name, email):
    user = User(username=username, password=password)  # REMOVED user_type
    db.session.add(user)
    db.session.commit()
    
    student = Student(user_id=user.id, studentName=name, studentEmail=email)
    db.session.add(student)
    db.session.commit()
    print(f'{name} created!')

# this command will be : flask student create alice alicepass "Alice Wonderland" alice@student.com

@student_cli.command("list", help="Lists students in the database")
@click.argument("format", default="string")
def list_students_command(format):
    students = Student.query.all()
    if format == 'string':
        for student in students:
            print(f"ID: {student.studentID}, Name: {student.studentName}, Email: {student.studentEmail}")
    else:
        print([student.get_json() for student in students])

app.cli.add_command(student_cli) # add the group to the cli

'''
Staff Commands
'''

# create a group, it would be the first argument of the comand
# eg : flask staff <command>
staff_cli = AppGroup('staff', help='Staff object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@staff_cli.command("create", help="Creates a staff member")
@click.argument("username", default="staff1")
@click.argument("password", default="staffpass")
@click.argument("email", default="staff@university.com")
def create_staff_command(username, password, email):
    user = User(username=username, password=password)  # REMOVED user_type
    db.session.add(user)
    db.session.commit()
    
    staff = Staff(user_id=user.id, staffEmail=email)
    db.session.add(staff)
    db.session.commit()
    print(f'{email} created!')

# this command will be : flask staff create prof1 profpass prof@university.com

@staff_cli.command("list", help="Lists staff in the database")
@click.argument("format", default="string")
def list_staff_command(format):
    staff_members = Staff.query.all()
    if format == 'string':
        for staff in staff_members:
            print(f"ID: {staff.staffID}, Email: {staff.staffEmail}")
    else:
        print([staff.get_json() for staff in staff_members])

app.cli.add_command(staff_cli) # add the group to the cli

'''
Employer Commands
'''

# create a group, it would be the first argument of the comand
# eg : flask employer <command>
employer_cli = AppGroup('employer', help='Employer object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@employer_cli.command("create", help="Creates an employer")
@click.argument("username", default="employer1")
@click.argument("password", default="employerpass")
@click.argument("name", default="Jane Smith")
@click.argument("company", default="Tech Corp")
@click.argument("email", default="jane@techcorp.com")
def create_employer_command(username, password, name, company, email):
    user = User(username=username, password=password)  # REMOVED user_type
    db.session.add(user)
    db.session.commit()
    
    employer = Employer(user_id=user.id, employerName=name, companyName=company, employerEmail=email)
    db.session.add(employer)
    db.session.commit()
    print(f'{name} from {company} created!')

# this command will be : flask employer create google googlepass "Google HR" "Google" hr@google.com

@employer_cli.command("list", help="Lists employers in the database")
@click.argument("format", default="string")
def list_employers_command(format):
    employers = Employer.query.all()
    if format == 'string':
        for employer in employers:
            print(f"ID: {employer.employerID}, Name: {employer.employerName}, Company: {employer.companyName}, Email: {employer.employerEmail}")
    else:
        print([employer.get_json() for employer in employers])

app.cli.add_command(employer_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

@test.command("internship", help="Run Internship tests")
@click.argument("type", default="all")
def internship_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "InternshipUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "InternshipIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "Internship"]))

app.cli.add_command(test)