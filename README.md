# Flask Database Application

This project is a simple web application built using Flask that allows users to add and retrieve user information from an SQLite database.

## Project Structure

```
flask-db-app
├── app.py                # Main application file
├── requirements.txt      # Project dependencies
├── database.db          # SQLite database file
├── templates
│   └── index.html       # HTML template for the main page
├── static
│   └── style.css        # CSS styles for the web application
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository** (if applicable):
   ```
   git clone <repository-url>
   cd flask-db-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   The database will be automatically created when you run the application for the first time.

5. **Run the application**:
   ```
   python app.py
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000/` to view the application.

## Usage

- To add a user, fill out the form on the main page with the user's name and email, then submit.
- To view all users, you can implement a feature to display the list of users on the web page or access the `/get_users` endpoint directly.

## License

This project is licensed under the MIT License - see the LICENSE file for details.