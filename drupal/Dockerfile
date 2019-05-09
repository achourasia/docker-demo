FROM drupal

RUN apt-get update && apt-get install -y zip vim sqlite3


##########################################
# Install upload progress
# Currently build from source as its not available for PHP7.x on PECL

## @see Downloaded uploaded progress pecl source from https://git.php.net/?p=pecl/php/uploadprogress.git;a=summary
## @see Install instructions https://www.drupal.org/node/2718253#comment-11806285

# cd /tmp
# curl -O http://users.sdsc.edu/~amit/temp/uploadprogress-95d8a0f.tar.gz
# tar xzf uploadprogress-95d8a0f.tar.gz
# cd uploadprogress-95d8a0f
# phpize
# ./configure
# make
# make test
# make install

## add ini config for uploadprogress as follows
## ; Enable Upload progress
## extension=uploadprogress.so
# vi /usr/local/etc/php/conf.d/seedme2-php-ext-uploadprogress.ini

## restart apache
# apachectl restart
##########################################

# Set the Drush version.
ENV DRUSH_VERSION 8.1.2

# Install Drush 8 with the phar file.
RUN curl -fsSL -o /usr/local/bin/drush "https://github.com/drush-ops/drush/releases/download/$DRUSH_VERSION/drush.phar" && \
  chmod +x /usr/local/bin/drush

# Copy over the init.sh script to the container's file path
COPY init.sh /init.sh

# Make the init.sh script executable.
RUN chmod u+x /init.sh