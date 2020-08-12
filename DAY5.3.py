import imaplib

g=imaplib.IMAP4_SSL('imap.gmail.com')
em=input('enter email id')
pw=input('password')

g.login(em,pw)

g.select('INBOX')
a,b = g.status('INBOX','(UNSEEN)')

c=str(b[0])
n=c[18:32]
print("There are "+n+" unread messages in your account.")