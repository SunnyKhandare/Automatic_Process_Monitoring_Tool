import schedule
import time
from Mail_Sender import check_connection , Mail_sender
from Get_Processes_Info import get_and_write_process_info
from sys import *

def driver_function(email_id, password ,dirname):
	if check_connection():
		get_and_write_process_info(dirname);
		Mail_sender(email_id ,password , "sunnyakhandare5618@gmail.com", dirname);


schedule.every().minutes.do( lambda : driver_function(argv[2], argv[3] ,argv[1]) );

while 1:
	schedule.run_pending();
	time.sleep(1);

