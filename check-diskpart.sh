#!/bin/bash
disk=$1
firstpart=$1"1"
/sbin/sfdisk -l $disk 2>&1|grep $firstpart |grep FAT32
