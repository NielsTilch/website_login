# Login website page

This is a simple Flask web application that provides login and signup functionalities with session management. User credentials are stored in an SQLite database with passwords hashed using MD5.

## Features

- User login
- User signup
- View all accounts
- Print accounts table to the console

## Requirements

- Python 3.x
- Flask
- SQLite

### `Python`

To download latest stable release of python : https://www.python.org/downloads/windows/ .

### `Flask`
After installing python 3.X on your computer, install flask via the following command in a command terminal:

```bash
    pip install flask
```

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/NielsTilch/website_login.git
    cd website_login
    ```

2. **Install the dependencies**:

    Go to section [requirements](#requirements).

3. **Run the application**:

    ```bash
    python app.py
    ```

4. **Access the application**:

    Open your browser and go to `http://127.0.0.1:5000` (or other if the command interface tell you so).

## Project Structure
### `app.py`

This is the main application file that contains all the routes and logic for the application.

### `templates/`

This directory contains the HTML templates for the application.

- `login.html`: The login page.
- `signup.html`: The signup page.
- `accounts.html`: The page that lists all accounts stored in the database.

### `static/`

This directory contains the CSS file for styling the application.

## Routes

- **`/`**: The login page. Users can log in from here.
- **`/signup`**: The signup page. Users can create a new account here.
- **`/home`**: The home page after logging in. Displays a welcome message and a link to view all accounts.
- **`/accounts`**: The accounts page. Lists all accounts in the database.

## Functionality

### Login

- Users can log in using their username and password.
- If the credentials are correct, a session is created and the user is redirected to the home page.
- If the credentials are incorrect, an error message is displayed.

### Signup

- Users can create a new account by providing a username and password.
- The password is hashed using MD5 before being stored in the database.
- After signup, the user is redirected to the login page.

### View Accounts

- The accounts page lists all accounts in the database.


