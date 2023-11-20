import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from tqdm import tqdm

# Set the path to your credentials JSON file
credentials_path = 'your_service_account_credentional.json'

# Set the path to the file you want to upload
file_path = r'your_file_path'

# Set the destination folder ID in Google Drive
folder_id = r'your_folder_id'

def create_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=['https://www.googleapis.com/auth/drive']
    )
    return build('drive', 'v3', credentials=credentials)

def upload_file_with_progress(service, file_path, folder_id):
    file_name = os.path.basename(file_path)
    media = MediaFileUpload(file_path, chunksize=1024 * 1024, resumable=True)

    file_metadata = {
        'name': file_name,
        'parents': [folder_id],
    }

    request = service.files().create(body=file_metadata, media_body=media)

    # Use tqdm for the progress bar
    with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True) as pbar:
        while True:
            status, done = request.next_chunk()
            if status:
                pbar.update(status.resumable_progress - pbar.n)  # Update based on bytes transferred
            if done:
                pbar.close()
                break

if __name__ == "__main__":
    drive_service = create_drive_service()
    upload_file_with_progress(drive_service, file_path, folder_id)
