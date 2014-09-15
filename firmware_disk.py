#!/usr/bin/env python

from subprocess import Popen, PIPE, call
import sys
import os
import re

# use /boot's belonging partition to determine the boot disk
def is_bootdisk(disk_devname):
	cmdpath = os.getcwd() + "/find-bootdisk.sh"
	pipe = Popen([cmdpath], stdout = PIPE)
	bootdisk, err = pipe.communicate()
	if err is not None or bootdisk == "":
		print "something wrong!!!"
		return None
	
	m = re.search("\d", bootdisk)
	if m:
		parent_disk = bootdisk[: m.start()]
#		print parent_disk
	else:
		return None	

	if disk_devname == parent_disk: 
		return True
	else:
		return False


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
		print "\tNo fat32 partition detected..."
		return None
	else:
		return rc

# list all available USB disks
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
	if udisks is None:
		print "aborted"
		exit()

	for d in udisks: 
#		print d
		if is_bootdisk(d): 
			print d + " : boot disk"
		else:
			print d + " : normal disk"
		rc = has_fat32_part(d)
		if rc is not None:
			print "\t" + rc
