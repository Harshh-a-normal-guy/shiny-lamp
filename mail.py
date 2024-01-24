import imaplib
import email
import yaml
from emailparser import generate_inputs_from_bs4
from user_data_generated import map_values_to_keys,clash_keywords
with open('EmailConfig.yml') as f:
    email_config = yaml.load(f, Loader=yaml.FullLoader)

user = email_config['user']
passwd = email_config['password']
imap_url = email_config['imap_url']
mailbox = email_config['mailbox']
include_body = email_config['content']['include_body']
max_body_length = email_config['content']['max_body_length']

my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login(user, passwd)
my_mail.select(mailbox)

# Search for all emails and fetch the latest one
status, messages = my_mail.search(None, 'ALL')
email_ids = messages[0].split()
latest_email_id = email_ids[-2]

# # Fetch the latest email
status, msg_data = my_mail.fetch(latest_email_id, '(RFC822)')
raw_email = msg_data[0][1]

# # Parse the raw email
email_message = email.message_from_bytes(raw_email)
# # Get subject and body of the email
subject = email_message["Subject"]
body = None

if include_body:
    if email_message.is_multipart():
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)[:max_body_length]
    else:
        body = email_message.get_payload(decode=True)[:max_body_length]

# Print subject and body
# print("Subject:", subject)
# if body:
#     print("Body:")
#     print(body.decode('utf-8'))

inputs=body.decode('utf-8')
# inputs=inputs.split(' ')
inputs=list(inputs)
# print(inputs)
generated_data=(map_values_to_keys(set(generate_inputs_from_bs4(inputs))))
from users import generate_html
generate_html()
