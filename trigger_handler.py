# Copyright (c) 2021 Jan Tünnermann. All rights reserved.
# This work is licensed under the terms of the MIT license.  
# For a copy, see <https://opensource.org/licenses/MIT>.

import subprocess
from flask import Flask
import pyxid2

app = Flask(__name__, static_folder='experiment')

# Configuration:
APP_HOST = '127.0.0.1' # Defaul is localhost
APP_PORT = 8000 

@app.route('/trigger/usb/<trigger_value>')
def usb_trigger(trigger_value):
	trigger_value = int(trigger_value)
	try:
		dev.activate_line(bitmask=trigger_value)
		status = '[Success]'
		#dev.clear_all_lines()
	except:
		status = '[Fail]'
	
	msg = status + ' ' + 'Trigger ' + str(trigger_value)
	print(msg)
	return(msg)

if __name__ == '__main__':
	# get a list of all attached XID devices
	devices = pyxid2.get_xid_devices()

	if devices:
		print(devices)
	else:
		print("No XID devices detected")
		exit()

	dev = devices[0] # get the first device to use

	print("Using ", dev)

	#Setting the pulse duration to 0 makes the lines stay activated until lowered
	#manually with clear_line() or clear_all_lines().
	dev.set_pulse_duration(5)

	app.run(host=APP_HOST, port=APP_PORT)