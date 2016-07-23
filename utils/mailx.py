# -*- coding: UTF-8 -*-
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.Header import Header


class Mailx:
    def __init__(self, conf):
        self.conf = conf

    def send(self, from_nm, to_list, subject, content, subtype='plain', charset='UTF-8', attachs=[]):
        if 'smtp_able' not in self.conf or not self.conf['smtp_able']:
            return False

        if not to_list:
            return False

        msgs = MIMEMultipart('alternative')
        msgs['subject'] = Header(subject, charset)
        if from_nm == '':
            msgs['from'] = self.conf['smtp_from'] 
        else:
            msgs['from'] = from_nm
        msgs['sender'] = self.conf['smtp_from']
        msgs['to'] = ';'.join(to_list)
        msgs['reply-to'] = msgs['from']

        msgs.attach(MIMEText(content, _subtype=subtype, _charset=charset))
        for item in attachs:
            msgs.attach(item)

        try:
            if 465 == int(self.conf['smtp_port']):
                smtp = smtplib.SMTP_SSL(self.conf['smtp_host'], self.conf['smtp_port'])
            elif 587 == int(self.conf['smtp_port']):
                smtp = smtplib.SMTP(self.conf['smtp_host'], self.conf['smtp_port'])
                smtp.ehlo()
                smtp.starttls()
            else:
                smtp = smtplib.SMTP(self.conf['smtp_host'], self.conf['smtp_port'])

            smtp.ehlo()

            smtp.login(self.conf['smtp_user'], self.conf['smtp_pswd'])
            smtp.sendmail(msgs['from'], to_list, msgs.as_string())
            smtp.quit()

            return True
        except: # Exception as e:
            return False
