# Flask Google Drive PDF Viewer

This project is a simple web application built using Flask that allows users to search and view PDF files stored in a specific Google Drive folder.

## Project Structure

```
Instrumentacion-main/
├── app.py                # Main application file
├── requirements.txt      # Project dependencies
├── credentails.json      # Service account credentials for Google Drive API
├── Procfile              # Heroku deployment configuration
├── templates
│   └── index.html       # HTML template for the main page
└── README.md            # Project documentation
```

## Setup Instructions

1.  **Clone the repository** (if applicable):
    ```
    git clone <repository-url>
    cd Instrumentacion-main
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies**:
    ```
    pip install -r requirements.txt
    ```

4.  **Configure Google Drive API Access**:
    *   Enable the Google Drive API in your Google Cloud Console.
    *   Create a service account and download the credentials as `credentials.json`.
    *   Share the Google Drive folder you want to use with the service account's email address.
    *   Update the `FOLDER_ID` variable in `app.py` with the ID of your Google Drive folder.

5.  **Run the application**:
    ```
    python app.py
    ```

6.  **Access the application**:
    Open your web browser and go to `http://127.0.0.1:5000/` to view the application.

## Usage

- The application will load all PDF files from the configured Google Drive folder.
- Use the search bar to filter the PDFs by name in real-time.
- Click on a PDF name or link to view it directly on the page.

## License

This project is licensed under the MIT License.
