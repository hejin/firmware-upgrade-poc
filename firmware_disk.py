#!/usr/bin/env python

from subprocess import Popen, PIPE, call
import sys
import os


def list_usbdisks():
	cmdpath = os.getcwd() + "/find-usbdisk.sh"
	pipe = Popen([cmdpath], stdout = PIPE)
	rc, err = pipe.communicate()
	if err is not None:
		print "something wrong!!!"
		return

	if rc == "":
		print "No USB disks detected..."
	else:
		udisk_list = rc.splitlines()
#		print udisk_list.size() + "usb disk(s) found as followings: \n" + udisk_list
		print "usb disk(s) found as followings: "
		for d in udisk_list: print d

if __name__ == "__main__":
	list_usbdisks()
