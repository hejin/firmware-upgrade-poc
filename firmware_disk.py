#!/usr/bin/env python

from subprocess import Popen, PIPE, call
import sys
import os

def is_bootdisk(disk_devname):
	print ""

# check if the usb disk contains a valid FAT32 partition
# NOTE: we only use FAT32 partition in USB disk to store firmware
def has_fat32_part(disk_devname):
	cmdpath = os.getcwd() + "/check-diskpart.sh"
	pipe = Popen([cmdpath, disk_devname], stdout = PIPE)
	rc, err = pipe.communicate()
	if err is not None:
		print "something wrong!!!"
		return None

	if rc == "":
		print "No fat32 partition detected..."
		return None
	else:
		return rc

def list_usbdisks():
	cmdpath = os.getcwd() + "/find-usbdisk.sh"
	pipe = Popen([cmdpath], stdout = PIPE)
	rc, err = pipe.communicate()
	if err is not None:
		print "something wrong!!!"
		return None

	if rc == "":
		print "No USB disks detected..."
		return None
	else:
		udisk_list = rc.splitlines()
#		print udisk_list.size() + "usb disk(s) found as followings: \n" + udisk_list
		print "usb disk(s) found as followings: "
		#for d in udisk_list: print d
		return udisk_list

if __name__ == "__main__":
	udisks = list_usbdisks()
	for d in udisks: 
		print d
		rc = has_fat32_part(d)
		if rc is not None:
			print rc
			
