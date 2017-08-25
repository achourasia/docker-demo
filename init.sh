#!/bin/bash

# This script is supposed to be in / of seedme conatiners to initialise those

demo_pwd=`/usr/bin/openssl rand -base64 6`
/bin/echo $demo_pwd
/usr/local/bin/drush -q upwd demo --password=$demo_pwd > /dev/null 2>&1

TZ='America/Los_Angeles' /bin/date '+%Y-%m-%d %H:%M:%S' -d '+7 days' | /usr/local/bin/drush -q cset -y block.block.countdowntimer_bartik settings.countdown_datetime - > /dev/null 2>&1
TZ='America/Los_Angeles' /bin/date '+%Y-%m-%d %H:%M:%S' -d '+7 days' | /usr/local/bin/drush -q cset -y block.block.countdowntimer settings.countdown_datetime - > /dev/null 2>&1
TZ='America/Los_Angeles' /bin/date '+%Y-%m-%d %H:%M:%S' -d '+7 days' | /usr/local/bin/drush -q cset -y block.block.countdowntimer_2 settings.countdown_datetime - > /dev/null 2>&1
TZ='America/Los_Angeles' /bin/date '+%Y-%m-%d %H:%M:%S' -d '+7 days' | /usr/local/bin/drush -q cset -y block.block.countdowntimer_3 settings.countdown_datetime - > /dev/null 2>&1

