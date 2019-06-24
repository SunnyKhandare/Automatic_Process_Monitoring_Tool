import psutil

def get_and_write_process_info(dirname):
	try:
		file_descriptor = open("/home/sunny/"+dirname+"/process.log","w+");

		for process in psutil.process_iter():
			process_info = process.as_dict(attrs = ['name' , 'pid' , 'username']);

			file_descriptor.write(process_info['name'] + " "+ str(process_info['pid']) +" "+process_info['username']+"\n");
	except Exception as E:
		print("Unable to Create Process Logs ",E);
