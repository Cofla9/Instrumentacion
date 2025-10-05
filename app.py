from flask import Flask, jsonify, render_template, request
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)

# --- CONFIGURACIÓN ---
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = '15XFBtrdqyOJ4r-djW3vfEpXfFDrk1XJk'  # ID de tu carpeta raíz en Google Drive


# --- FUNCIÓN PARA CONECTARSE A GOOGLE DRIVE ---
def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)


# --- RUTA PRINCIPAL ---
@app.route('/')
def index():
    return render_template('index.html')


# --- RUTA PARA LISTAR SOLO LAS CARPETAS ---
@app.route('/folders')
def get_folders():
    try:
        service = get_drive_service()
        folders = []

        def find_folders(folder_id, current_path=""):
            results = service.files().list(
                q=f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false",
                fields="files(id, name)",
                pageSize=1000
            ).execute()
            items = results.get('files', [])
            for item in items:
                folder_name = f"{current_path}/{item['name']}" if current_path else item['name']
                folders.append({'id': item['id'], 'path': folder_name})
                find_folders(item['id'], folder_name)

        find_folders(FOLDER_ID)
        return jsonify(folders)
    except Exception as e:
        print(f"Error al obtener carpetas: {e}")
        return jsonify({"error": "No se pudieron obtener las carpetas."}), 500


# --- RUTA PARA LISTAR PDFs DE UNA CARPETA ---
@app.route('/pdfs')
def get_pdfs():
    folder_id = request.args.get('folder_id', FOLDER_ID)
    try:
        service = get_drive_service()
        results = service.files().list(
            q=f"'{folder_id}' in parents and mimeType='application/pdf' and trashed=false",
            fields="files(id, name)",
            pageSize=1000
        ).execute()

        pdfs = [
            {
                'nombre': item['name'],
                'url': f"https://drive.google.com/file/d/{item['id']}/preview"
            }
            for item in results.get('files', [])
        ]
        return jsonify(pdfs)
    except Exception as e:
        print(f"Error al obtener PDFs: {e}")
        return jsonify({"error": "No se pudieron obtener los PDFs."}), 500


if __name__ == '__main__':
    app.run(debug=True)


