#!/usr/bin/python
# -*- Mode: Python; python-indent: 8; indent-tabs-mode: t -*-

import sys, os, errno
import datetime
import re

devel_time = False
if devel_time:
	def log_debug(x):
		print x

        def log_slight_risk(x):
		print x

        def log_warning(x):
		print x

	def log_error(x):
		print x

	def exit_pass():
		sys.exit(0)

	def exit_fail():
		sys.exit(1)

	def exit_error():
		sys.exit(-1)
else:
	from preupg.script_api import *

#END GENERATED SECTION

# exit functions are exit_{pass,not_applicable, fixed, fail, etc.}
# logging functions are log_{error, warning, info, etc.}
# for logging in-place risk use functions log_{extreme, high, medium, slight}_risk

def cgroup_daemon():
	cgroup_re = re.compile(r"\bCGROUP_DAEMON\b") #\b  Matches the empty string, but only at the beginning or end of a word. A word is defined as a sequence of alphanumeric or underscore characters,
	found = False
	for root, dirs, files in os.walk('/etc/sysconfig'):
		for filename in files:
			with open(root+"/"+filename, "r") as f:
				data = f.read()
			if cgroup_re.search(data):
				found = True
				log_slight_risk("The '" + filename + "' file mentions CGROUP_DAEMON.")

	return found


if __name__ == "__main__":
	if cgroup_daemon():
		exit_fail()
	else:
		exit_pass()
