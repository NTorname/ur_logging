<h1>UR_LOGGING README</h1>

This script is intended for logging of test subject's interacting with the scooter's user interfaces. It currently is untested...

<h2>Description of Function</h2>

Currently, the script works by being called from another script by instantiating the object with the participant number and whether they are using tui or gui as an argument.
Like so: ```name = logger([participant_number], "gui"/"tui")```
This object subscribes to ```/logging_topic``` and appends a new line to the .csv file with the contents of the topic with a time stamp.

<h2>/logging_topic</h2>

/logging_topic is currently a std_msgs String with a string of comma separated values indicating what state the scooter is in.

The information contained is: button pressed, current state, and next state.

<h2>Output</h2>

The output is a .csv file titled ```[subject number]_[gui/tui]_[trial number].csv```. 
The file has a small human-readable header and each subsequent new line begins with a timestamp and strings containing scooter state.

<ln />

file written using tab not spaces!

