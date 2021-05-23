import imapclient
import datetime
conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('youremail@gmail.com','yourpwd')
conn.select_folder('INBOX',readonly=True)
UIDs = conn.search([u'SINCE', datetime.datetime(2021,5,1)])
print(UIDs)

rawMessages = conn.fetch([4026],['BODY[]','FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[4026][b'BODY[]'])
print(message.get_subject())
# print(message.text_part.get_payload().decode('UTF-8')) -> Obsolete