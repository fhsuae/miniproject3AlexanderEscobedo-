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
git clone https://github.com/fhsuae/miniproject3AlexanderEscobedo-.git
```
Create and activate a virtual environment:

Windows:
```
python -m venv venv
venv\Scripts\activate
```
macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
 
### Executing program

* Before running the app, initialize the SQLite database using Flask CLI:
```
flask --app app init-db
```
This command will:
* Create the user and scholarship tables
* Set up foreign key relationships
* Store the database in instance/app.sqlite


Start the Flask development server:
```
flask --app app run
```

Open your web browser and go to:
```
http://127.0.0.1:5000/
```
Note: Register a user account via the Register page before adding scholarships.

You should see the Scholarship Tracker homepage.
### Using an IDE(Optional)

If you are using an IDE like PyCharm or VS Code:

* Open the project folder.

* Go to Run Configurations → Add New Configuration → Flask Server.

* Set the target script to the app package.

* Click the Run ▶️ button to start the development server.

This lets you run and debug the Flask app with one click.

## Database Schema 
The application uses SQLite with the following tables:

**User**
* id (Primary Key)
* username
* password_hash



**Scholarship**
* id (Primary Key)
* user_id (Foreign Key → User.id)
* name
* amount
* deadline
* status
* notes

Each scholarship is linked to a registered user via user_id, ensuring personalized data for each account.



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

