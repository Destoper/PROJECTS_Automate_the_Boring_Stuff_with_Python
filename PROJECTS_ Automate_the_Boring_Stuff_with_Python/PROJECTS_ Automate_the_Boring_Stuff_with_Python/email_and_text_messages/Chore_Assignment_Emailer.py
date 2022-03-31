# Take personal emails and chores and randomly linking an email to a chore.
import pyinputplus, smtplib, sys
from random import choice

def randon_chores(emails, chores):
    '''create a dictionary by randomly linking an email to a chore'''
    chores_emails_dict = {}
    for email in emails:
        random_chore = choice(chores)
        chores_emails_dict[email] = random_chore
        chores.remove(random_chore)
    return chores_emails_dict

def send_emails(chores_emails_dict):
    # Config the smtp
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login('youremail@example.com', sys.argv[1]) # When you run the script pass by command line the mail password

    # Send a message to each email reporting the chore of the week
    for email, chore in chores_emails_dict.items():
        sendmailStatus = smtp_obj.sendmail('youremail@example.com', email,
                    f'Subject: Week Chore.\n Hey there! your chore of the week is {chore}.')
        
        if sendmailStatus != {}:
            print(f'\nThere was a problem sending email to {email}: {sendmailStatus}')
        else:
            print(f'Chore Send to {email}...')

    smtp_obj.quit()

chores, emails = [], []
while True:
    print("\n[LET BLANK TO CONTINUE] Enter persons' emails:")
    e = pyinputplus.inputEmail(blank=True )    
    if not e:
        break
    else:
        emails.append(e)

for index in range(len(emails)):
    print(f"\n[{index+1}]Enter a chore:")
    chore = pyinputplus.inputStr()
    chores.append(chore)

chores_emails_dict = randon_chores(emails, chores)
send_emails(chores_emails_dict)

