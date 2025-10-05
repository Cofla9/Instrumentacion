from flask import Flask, jsonify, render_template
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = '15XFBtrdqyOJ4r-djW3vfEpXfFDrk1XJk'  # Reemplaza por el ID de tu carpeta

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdfs')
def get_pdfs():
    try:
        creds = service_account.Credentials.from_service_account_file(
            'credentials.json', scopes=SCOPES)
        service = build('drive', 'v3', credentials=creds)
        
        all_pdfs = []
        def find_pdfs_recursively(folder_id):
            page_token = None
            while True:
                # Query for both folders and PDF files within the current folder_id
                results = service.files().list(
                    q=f"'{folder_id}' in parents and (mimeType='application/pdf' or mimeType='application/vnd.google-apps.folder')",
                    fields="nextPageToken, files(id, name, mimeType)",
                    pageSize=1000,
                    pageToken=page_token
                ).execute()
                
                items = results.get('files', [])
                for item in items:
                    if item['mimeType'] == 'application/vnd.google-apps.folder':
                        # If it's a folder, recurse into it
                        find_pdfs_recursively(item['id'])
                    else:
                        # If it's a PDF, add it to our list
                        all_pdfs.append({
                            'nombre': item['name'],
                            'url': f"https://drive.google.com/file/d/{item['id']}/preview"
                        })
                
                page_token = results.get('nextPageToken')
                if not page_token:
                    break

        # Start the recursive search from the root folder
        find_pdfs_recursively(FOLDER_ID)
        
        return jsonify(all_pdfs)

    except FileNotFoundError:
        print("Error: credentials.json not found.")
        return jsonify({"error": "Server configuration error: credentials file missing."}), 500
    except Exception as e:
        print(f"An error occurred while fetching from Google Drive: {e}")
        return jsonify({"error": "Could not retrieve files from Google Drive."}), 500

if __name__ == '__main__':
    app.run(debug=True)

