#!/bin/bash
/usr/bin/lsscsi -t |awk '{print $3, $5;}' | grep  "usb:" |awk '{print $2;}'
