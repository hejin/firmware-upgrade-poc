#!/bin/bash
cat /proc/mounts |grep boot |awk '{print $1}'
