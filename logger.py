#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import datetime
import os

'''Noah's Logging Script

	sticks everything in a .txt file with time it was recorded'''


class Logger:

	def __init__(self, part_num):
		self.participant_num = part_num
		self.string = ""
		self.date = datetime.datetime.now()

		rospy.loginfo("Figuring out participant {} log or something...".format(self.participant_num))

		if os.path.isfile("{}_log.txt".format(self.participant_num)):
			rospy.loginfo("Appending existing participant {} log.".format(self.participant_num))
			self.log_file = open("{}_log.txt".format(self.participant_num), "a")
			self.log_file.write("\n===================================\n\n")
			self.log_file.close()
		
		rospy.loginfo("Creating log header.".format(self.participant_num))
		self.log_file = open("{}_log.txt".format(self.participant_num), "a")
		self.log_file.write("Begin Log for Participant #{} generated {}/{}/{} {}:{}\ntime\t\tlog event\n".format(self.participant_num,
			self.date.month, self.date.day, self.date.year, self.date.hour, self.date.minute))
		self.log_file.close()
		rospy.loginfo("Log file ready.")

		self.start_log()
		

	def get_log(self, log_msg):
		if log_msg != self.string:
			self.string = log_msg
			self.date = datetime.datetime.now()
			self.log_file = open("{}_log.txt".format(self.participant_num), "a")
			self.log_file.write("{}:{}:{}\t{}\n".format(self.date.hour, self.date.minute, self.date.second, self.string))
			rospy.loginfo("New event logged: {}".format(self.string))
			self.log_file.close()
				

	def start_log(self):
		rospy.loginfo("Begin logging now.")

		rospy.Subscriber("logging_topic", String, self.get_log)

		rospy.spin()


if __name__ == '__main__':
	rospy.init_node('logger', anonymous=True)
	Logger(1)    

