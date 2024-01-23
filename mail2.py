# import os.path
# import base64
# import quopri
# from bs4 import BeautifulSoup as bs 
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


# def decode_body(body, encoding):
#     if encoding == "BASE64":
#         return base64.urlsafe_b64decode(body).decode("utf-8")
#     elif encoding == "QUOTED-PRINTABLE":
#         return quopri.decodestring(body).decode("utf-8")
#     else:
#         return body

# def get_body(message):
#     """Get the body of the email."""
#     if 'payload' in message and 'parts' in message['payload']:
#         for part in message['payload']['parts']:
#             if 'body' in part:
#                 data = part['body']['data']
#                 if 'attachmentId' not in part['body']:
#                     # Decode the body data
#                     decoded_data = base64.urlsafe_b64decode(data).decode("utf-8")
#                     return decoded_data
#     return None




# def main():
# #     """Shows basic usage of the Gmail API.
#     # Lists the user's Gmail labels.
#     # """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open("token.json", "w") as token:
#             token.write(creds.to_json())

#     try:
#         # Call the Gmail API
#         service = build("gmail", "v1", credentials=creds)
#         results = service.users().labels().list(userId="me").execute()
#         labels = results.get("labels", [])

#         # List messages
#         messages = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
#         # print(messages)
#         if 'messages' in messages:
#             latest_message_id = messages['messages'][0]['id']
#             msg = service.users().messages().get(userId='me', id=latest_message_id, format='full').execute()
#             # print(f"Latest Message ID: {msg['id']}")
    
#     # Retrieve the body
#             body = get_body(msg)
#             if body is not None:
#                 pass
#                 # print(f"Latest Message Body: {body}")
#             else    :
#                 print("No body found for the latest message.")
#         else:
#             print("No messages found.")


        
#     except HttpError as error:
#         # TODO(developer) - Handle errors from Gmail API.
#         print(f"An error occurred: {error}")
#     return body


# if __name__ == "__main__":
#     main()

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_raw_message(service, user_id, msg_id):
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id, format='raw').execute()
        raw_message = message['raw']
        return raw_message
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def decode_body(body, encoding):
    if encoding == "BASE64":
        return base64.urlsafe_b64decode(body).decode("utf-8")
    elif encoding == "QUOTED-PRINTABLE":
        return quopri.decodestring(body).decode("utf-8")
    else:
        return body

def main():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)

        # List messages
        messages = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
        
        if 'messages' in messages:
            latest_message_id = messages['messages'][0]['id']
            raw_message = get_raw_message(service, 'me', latest_message_id)
            if raw_message is not None:
                decoded_message = base64.urlsafe_b64decode(raw_message).decode("utf-8")
                print(decoded_message)
            else:
                print("Failed to retrieve the raw message.")
        else:
            print("No messages found.")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
