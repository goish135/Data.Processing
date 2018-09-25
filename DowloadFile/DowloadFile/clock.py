from apscheduler.schedulers.blocking import BlockingScheduler
import os

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=5)
def timed_job():
	os.system("python auto_dowload_upload.py")
	print('Start download and upload')
sched.start()