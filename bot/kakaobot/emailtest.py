# -*- coding:utf-8 -*-
#from email.mime.multipart import MIMEMultipart
#from email.header import Header

#from email.utils import formataddr

import smtplib
from email.mime.text import MIMEText
 
def send_email():
	#msg=MIMEMultipart('alternative')
	naver_user = 'kwonsye@naver.com'
	naver_password = 'pk2vqp'
 
	sent_from = naver_user
	to = 'kwonsye@naver.com'
	# to = ['cust1@gmail.com', 'cust2@naver.com'] #다중대상 전송
	subject = "[챗봇알리미]버그가 신고되었습니다. "
	body = "여성폭력 상담챗봇에서 버그가 신고되었습니다."
 
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
    main()

