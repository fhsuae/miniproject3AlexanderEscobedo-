### INF601 - Advanced Programming in Python
### Alexander Escobedo 
### Mini Project 3 
 
 
# Project Title
 
**Miniproject 3 Scholarship Tracker**
 
## Description
 
Scholarship Tracker is a Flask web application using SQLite and Bootstrap that helps students manage scholarships efficiently.  

Key features include:  
* Secure user registration and login  
* Add, edit, delete, and view scholarships  
* Track scholarship details such as name, amount, deadline, status, and notes  
* Statistics page showing total scholarships and status breakdown  
* Responsive interface with Bootstrap styling, modals, and form validation  

This project provides a simple, intuitive workflow for students to stay organized and streamline their scholarship application process.
## Getting Started
 
### Prerequisites
 
Before running the project, ensure you have:
*  Python 3.10+ installed
* pip package manager
* SQLite (bundled with Python)
* Required Python packages (install via requirements.txt)


### Installing
 
Clone the repository:
```
git clone https://github.com/fhsuae/miniproject3AlexanderEscobedo-
```
Create a virtual environment and activate it: 
```
python -m venv venv
```
Now run this on your machine to activate the environment:

Windows:
```
venv\Scripts\activate
```
MacOS/Linux:
```
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
 
### Executing program

* Before running the app, initialize the SQLite database using Flask CLI:
```
flask --app flaskr init-db
```
This command will:
* Create the user and scholarship tables
* Set up foreign key relationships
* Store the database in instance/app.sqlite


Start the Flask development server:
```
flask --app flaskr run
```
Open your web browser and go to:
```
http://127.0.0.1:5000/
```
* You should see the Scholarship Tracker homepage.
### Using an IDE(Optional)

If you are using an IDE like PyCharm or similar:

* Select the current file in the project.

* Go to Edit Configurations.

* Click Add New Configuration and choose Flask Server.

* On the right-hand side, select the script you want to run — in this project, choose app/.

* Use the Play button to start the Flask development server.

This ensures the IDE knows which Flask app to execute and allows you to run the project with one click.
 
## Project Pages
The app contains the following pages:
* Home / Index – View all scholarships
* Add Scholarship – Form to create a new scholarship
* Edit Scholarship – Update existing scholarship details
* Scholarship Details – View detailed information about a scholarship
* Statistics – View total scholarships and status breakdown



## Authors
 
Alexander Escobedo
 
## Version History

* 0.1
    * Initial Release

 
## Acknowledgments

* [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
* [SQLite Documentation](https://sqlite.org/docs.html)
* [Bootstrap Documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
* [The Official Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)– Project structure and authentication adapted from this tutorial

