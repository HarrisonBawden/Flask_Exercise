from datetime import datetime
import numbers
from urllib import request
from flask import Flask, render_template, request
import datetime, calendar

app = Flask(__name__, template_folder='templates', static_folder='statics')
studentOrganisationDetails = {"Charlie" : "French Fluency", "Tom" : "French Fluency", "Bob" : "French Fluency", "Sadie" : "Chess Club", "Avery" : "Tennis Club",}
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    timeRn = datetime.datetime.now()
    currentDate = timeRn.strftime("%B %d %Y %H:%M:%S")
    return render_template('index.html', currentDate=calendar.day_name[timeRn.weekday()] + ', ' + currentDate)

@app.get('/calculate')
def displayNumberPage():
    return render_template('form.html')

@app.route('/calculate', methods=['POST'])
def checkNumber():
    number = request.form['number']

    if len(number) == 0:
        render_template('result.html')
    try:
        if int(request.form['number']) % 2 == 0:
            msg = number + ' is even'
        if int(number) % 2 != 0:
            msg = number + ' is odd'
    except:
        msg = 'Provided input is not an integer!'
    
    return render_template('result.html', ans = msg)


@app.get('/addStudentOrganisation')
def displayStudentForm():
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrg = request.form['org']
    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName] = studentOrg
    
    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)



if __name__ == "__main__":
    app.run(debug=True)