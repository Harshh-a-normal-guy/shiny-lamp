from bs4 import BeautifulSoup as bs
# from mail2 import get_body,main,decode_body
from user_data_generated import map_values_to_keys
import pandas as pd
import re
import email
import yaml

# a= main()
# print(a)
# def generate_inputs_from_bs4(lst):
    # character_string=''
    # input_data_creation=[]
    # for char in lst:
    #     if re.match(r'[a-zA-Z0-9.@]', char):
    #         character_string+=char
    #     else:
    #         if character_string:

    #             input_data_creation.append(character_string)
    #             character_string=''
    # return input_data_creation

# input_data_list_bs4=set(generate_inputs_from_bs4(lst))
# print(set(input_data_list_bs4))
# print(map_values_to_keys(list(input_data_list_bs4)))

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
                raw_email = str(decoded_message) # replace with your raw email data
                msg = email.message_from_string(raw_email)
                from_address = msg['From']
                to_addresses = msg['To'].split(', ')
                subject = msg['Subject']
                date = msg['Date']
                body = msg.get_payload()
                email_data = {
                    'From': from_address,
                    'To': to_addresses,
                    'Subject': subject,
                    'Date': date,
                    'Body': body
                }
                print(email_data['Body'])
                # with open('email.yaml', 'w') as file:
                #     yaml.dump(email_data, file)

                # print(msg)
                # print(decoded_message)
            else:
                print("Failed to retrieve the raw message.")
        else:
            print("No messages found.")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
