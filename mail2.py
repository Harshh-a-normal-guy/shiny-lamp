import base64
from email import message_from_string
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def decode_body(body):
    try:
        # Decode base64 and decode bytes to UTF-8
        decoded_bytes = base64.urlsafe_b64decode(body.encode('UTF-8'))
        decoded_text = decoded_bytes.decode('UTF-8')
        return decoded_text
    except Exception as e:
        print(f"Error decoding body: {e}")
        return None

def main():
    # Your existing code...

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=crede)
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])
        
        if not labels:
            print("No labels found.")
            return

        print("Labels:")
        for label in labels:
            print(label["name"])

        # List messages
        messages = service.users().messages().list(userId='me').execute()
        if 'messages' in messages:
            for message in messages['messages']:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                print(f"Message ID: {msg['id']}")
                
                # Retrieve the body
                if 'body' in msg['payload']:
                    if 'data' in msg['payload']['body']:
                        body = msg['payload']['body']['data']
                        decoded_body = decode_body(body)
                        if decoded_body:
                            print(f"Decoded Message Body: {decoded_body}")
        else:
            print("No messages found.")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
