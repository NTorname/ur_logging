#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import os
import csv

'''Noah's Logging Script

	sticks everything in a .csv file with time it was recorded

	make the stinking string comma separated to hack std_msgs'''


class Logger:

	def __init__(self, part_num, ui):
		self.participant_num = part_num
		self.ui_type = ui
		self.trial = 0
		self.string = ""
		self.date = datetime.datetime.now()

		rospy.loginfo("Checking for pre-existing logs...".format(self.participant_num))

		while os.path.isfile("{}_{}_{}.csv".format(self.participant_num, self.ui_type, self.trial)):
			rospy.loginfo("found {} trail {}".format(self.ui_type, self.trail))
			self.trial += 1
		
		rospy.loginfo("Creating log.")
		self.log_file = open("{}_{}_{}.csv".format(self.participant_num, self.ui_type, self.trial), "w", newline='')
		self.writer = csv.writer(self.logfile)
		self.writer.writerow("time, button, current state, next state")
		self.log_file.close()
		
		rospy.loginfo("Log file ready.")

		self.start_log()
		

	def get_log(self, log_msg):
		if log_msg != self.string:
			self.string = log_msg
			self.log_file = open("{}_{}_{}.csv".format(self.participant_num, self.ui_type, self.trial), "a", newline='')
			self.writer = csv.writer(self.logfile)
			self.writer.writerow("{}, {}".format(self.log_msg.header.stamp, self.string))
			rospy.loginfo("New event logged")
			self.log_file.close()
				

	def start_log(self):
		rospy.loginfo("Begin logging now.")

		rospy.Subscriber("logging_topic", String, self.get_log)

		rospy.spin()


if __name__ == '__main__':
	rospy.init_node('logger', anonymous=True)
	Logger(999, "guh")    

