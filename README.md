<h1>UR_LOGGING README</h1>

This script is intended for logging of test subject's interacting with the scooter's user interfaces.

<h2>Description of Function</h2>

Currently, the script works by being called from another script by instantiating the object with the participant number as an argument.
Like so: ```name = logger([participant_number])```
This object subscribes to ```/logging_topic``` and appends a new line to the .txt file with the contents of the topic with a time stamp.

<h2>/logging_topic</h2>

/logging_topic is currently a std_msgs String with a short message explaining what what state the scooter is in.

It will soon be modified to be more computer-readable

<h2>Output</h2>

The output is currently a .txt file titled \[subject number\]\_log.txt. 
The file has a small human-readable header and each subsequent new line begins with a timestamp and the string containing scooter state.

This file will soon become a .csv.
