# upload file in Google Drive
## run requirements file
> `pip install -r requirements.txt`

## some setup you need to do
1. Locate the Service Account Email:

- Open the [Google Cloud Console.](https://console.cloud.google.com/)
2. Navigate to the API & Services Dashboard:
- In the left navigation menu, click on "APIs & Services" and then "Dashboard."

3. Enable the Google Drive API:
- Click on the "+ ENABLE APIS AND SERVICES" button.
- Search for ["Google Drive API"](https://console.cloud.google.com/apis/library/drive.googleapis.com) and click on it.
- Click the "Enable" button.

4. Create Credentials:
- Navigate to the "IAM & Admin" > ["Service accounts"](https://console.cloud.google.com/iam-admin/serviceaccounts/) section.
- Find the service account you created for your script.
- Note the email address associated with the [service account.](https://console.cloud.google.com/iam-admin/serviceaccounts)
- go to [service page](https://console.cloud.google.com/iam-admin/serviceaccounts/details/) and nevigae to key section and generate new key as json and download the json file.

5. Share the Folder:
- Open Google Drive in your web browser.
- Navigate to the folder you want to share.
- Right-click on the folder and select "Share."

6. Add the Service Account Email:
- In the sharing settings, enter the email address of the service account in the "Invite people" field.
- Set the permissions for the service account (e.g., "Editor" if you want it to have full access).
- Click "Send" to share the folder with the service account.

## Get Folder id
1. you will get your drive folder id in url path when you click on the folder in url you saw the folder id.
- EX. https://drive.google.com/drive/u/2/folders/1fHZ7r5r59X23DUjtSD9ZdJ5rvXRXv-jufg
- in above link the folder id is ~ `1fHZ7r5r59X23DUjtSD9ZdJ5rvXRXv-jufg` ~

2. replace `your_service_account_credentional.json` with your json file path. you downloaded earlier from service account>key
