from flask import Flask, jsonify, render_template
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = '1VPCL0hm_SQJucJCCLF377cAGCXlzq5F4'  # Reemplaza por el ID de tu carpeta

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdfs')
def get_pdfs():
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)
    pdfs = []
    page_token = None
    while True:
        results = service.files().list(
            q=f"'{FOLDER_ID}' in parents and mimeType='application/pdf'",
            fields="nextPageToken, files(id, name)",
            pageSize=1000,
            pageToken=page_token
        ).execute()
        files = results.get('files', [])
        for file in files:
            pdfs.append({
                'nombre': file['name'],
                'url': f"https://drive.google.com/file/d/{file['id']}/preview"
            })
        page_token = results.get('nextPageToken')
        if not page_token:
            break
    return jsonify(pdfs)

if __name__ == '__main__':
    app.run(debug=True)






