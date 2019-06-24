import urllib.request
import smtplib
from sys import *
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def check_connection():
	try:
		urllib.request.urlopen("http://216.58.192.142",timeout=5);
		return 1;
	except urllib.request.URLError as err:
		return 0;


def Mail_sender(email_id , password , to , dirname):
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com',465);
		server.ehlo();

		message = MIMEMultipart();
		message['Subject'] = "Log File Of Process";
		message['From'] = "Sunny Khandare";
		message['To'] = "Sunny Khandare";

		text = MIMEBase('application',"octet-stream");
		text.set_payload(open("/home/sunny/"+dirname+"/process.log","rb").read());
		encoders.encode_base64(text);
		text.add_header('Content-Disposition', 'attachment; filename="process.log"');

		message.attach(text);

		server.login(email_id , password);
		server.sendmail(email_id , to , message.as_string());
		server.close();
		print("Email sent successfully");
	except Exception as E:
		print("Unable to send mail",E);

