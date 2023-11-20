
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
# Set the path to your credentials JSON file
credentials_path = 'your_service_account_credentional.json'

# Set the path to the file you want to upload
file_path = r'your_file_path'

# Set the destination folder ID in Google Drive
folder_id = r'your_folder_id'

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_path, ['https://www.googleapis.com/auth/drive']
    )
    credentials = flow.run_local_server(port=0)
    return credentials

def create_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=['https://www.googleapis.com/auth/drive']
    )
    return build('drive', 'v3', credentials=credentials)


def upload_file(service, file_path, folder_id):
    file_name = os.path.basename(file_path)
    media = MediaFileUpload(file_path)

    file_metadata = {
        'name': file_name,
        'parents': [folder_id],
    }

    request = service.files().create(body=file_metadata, media_body=media)
    request.execute()

if __name__ == "__main__":
    drive_service = create_drive_service()
    upload_file(drive_service, file_path, folder_id)
