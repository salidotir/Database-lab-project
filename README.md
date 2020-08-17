# Database-lab-project

CRUD database application

## UI
UI implemented using python GUI toolkit, tkinter and tksheet

Run crud_main_window.py file to test the application.

## Database preparation
1. create a virtualenv and activate it
2. run: `pip install -r requirements.txt`
3. create a database named `shop`
4. Add a SQL server authentication login `Security > logins > new logins > SQL server authentication login` **login name**:postgres **password**:postgres
5. run: `alembic upgrade head`
