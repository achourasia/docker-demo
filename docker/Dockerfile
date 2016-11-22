FROM drupal

RUN apt-get update && apt-get install -y zip

RUN mkdir -p /usr/src/small_data && cd /usr/src/small_data \
            && curl -O http://dibbs.seedme.org/sites/dibbs.seedme.org/files/2016-09/small_data.v1.0.0.alpha_.zip \
            && unzip small_data.*.zip \
            && mv small_data /var/www/html/modules/ \
            && rm -rf /usr/src/small_data

