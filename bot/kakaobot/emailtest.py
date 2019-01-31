# -*- coding:utf-8 -*-
#from email.mime.multipart import MIMEMultipart
#from email.header import Header

#from email.utils import formataddr

import smtplib, os, json
from email.mime.text import MIMEText
from django.core.exceptions import ImproperlyConfigured

secret_file = "../secrets.json"

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


def send_email_feedback(email_content):
	subject = "여성폭력 상담챗봇 개선사항에 대한 이메일입니다."
	body = email_content
	send_result = send_email(subject, body)
	return send_result

def send_email_bug(email_content):
	subject = "여성폭력 상담챗봇 버그신고에 대한 이메일입니다."
	body = email_content
	send_result = send_email(subject, body)
	return send_result


def send_email(email_subject,email_content):
	#msg=MIMEMultipart('alternative')
	naver_user = 'kwonsye@naver.com'
	naver_password = get_secret("NAVER_PASS")
 
	sent_from = naver_user
	to = 'kwonsye@naver.com'
	# to = ['cust1@gmail.com', 'cust2@naver.com'] #다중대상 전송
	subject = email_subject
	body = email_content
 
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['To'] = to
	#  msg['From']=fromataddr((str(Header('test','utf-8')),sent_from))
 
	try:
		server = smtplib.SMTP_SSL('smtp.naver.com', 465)
		server.ehlo()  # say hello
		# server.starttls()
		server.login(naver_user, naver_password)
		server.sendmail(sent_from, to, msg.as_string())
		server.quit()
		return True
		#print('Email sent!')
	except:
		#print('Something went wrong...')

		return False 
if __name__ == "__main__":
    send_email("테스트","내용")


