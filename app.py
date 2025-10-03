from flask import Flask, jsonify, render_template
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = '15XFBtrdqyOJ4r-djW3vfEpXfFDrk1XJk'  # Reemplaza por el ID de tu carpeta

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdfs')
def get_pdfs():
    # Autenticación OAuth (solo la primera vez, luego guarda el token)
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('drive', 'v3', credentials=creds)
    results = service.files().list(
        q=f"'{FOLDER_ID}' in parents and mimeType='application/pdf'",
        fields="files(id, name)").execute()
    files = results.get('files', [])
    pdfs = []
    for file in files:
        pdfs.append({
            'nombre': file['name'],
            'url': f"https://drive.google.com/file/d/{file['id']}/preview"
        })
    return jsonify(pdfs)

if __name__ == '__main__':
    app.run(debug=True)



