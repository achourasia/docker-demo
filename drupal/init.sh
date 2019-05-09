#!/bin/bash

# This script is supposed to be in / of seedme conatiners to initialise those

demo_pwd=`/usr/bin/openssl rand -base64 6`
echo $demo_pwd

# Setup the site
cd /var/www/html

cp sites/default/default.settings.php sites/default/settings.php
cp sites/default/default.services.yml sites/default/services.yml

#drush site-install standard --db-url=sqlite://sites/default/files/.ht.sqlite --site-name="SeedMe Demo" -y > /dev/null 2>&1
drush -q upwd demo --password=$demo_pwd > /dev/null 2>&1

TZ='America/Los_Angeles' /bin/date '+%Y-%m-%d %H:%M:%S' -d '+7 days' | drush -q cset -y block.block.countdowntimer_bartik settings.countdown_datetime - > /dev/null 2>&1
TZ='America/Los_Angeles' /bin/date '+%Y-%m-%d %H:%M:%S' -d '+7 days' | drush -q cset -y block.block.countdowntimer settings.countdown_datetime - > /dev/null 2>&1
TZ='America/Los_Angeles' /bin/date '+%Y-%m-%d %H:%M:%S' -d '+7 days' | drush -q cset -y block.block.countdowntimer_2 settings.countdown_datetime - > /dev/null 2>&1
TZ='America/Los_Angeles' /bin/date '+%Y-%m-%d %H:%M:%S' -d '+7 days' | drush -q cset -y block.block.countdowntimer_3 settings.countdown_datetime - > /dev/null 2>&1