#!/bin/bash -e
#
# install_wordpress_debian.sh
# Historical one-shot installer for WordPress on Debian ~10 (buster era).
# From https://wiki.debian.org/WordPress
#
# WARNING: This does a full dist-upgrade + reboot as root.
# Review and update before using on modern systems (Debian 12+ uses different WP packaging).


apt update
apt-get dist-upgrade -y
apt install ntp wordpress curl apache2 mariadb-server iputils-ping fail2ban -y

chmod +x /usr/share/doc/wordpress/examples/setup-mysql
/usr/share/doc/wordpress/examples/setup-mysql localhost
mv /etc/wordpress/config-localhost.php  /etc/wordpress/config-default.php

echo "
<VirtualHost *:80>
        ServerName myblog.example.com

        ServerAdmin webmaster@example.com
        DocumentRoot /usr/share/wordpress

        Alias /wp-content /var/lib/wordpress/wp-content
        <Directory /usr/share/wordpress>
            Options FollowSymLinks
            AllowOverride Limit Options FileInfo
            DirectoryIndex index.php
            Require all granted
        </Directory>
        <Directory /var/lib/wordpress/wp-content>
            Options FollowSymLinks
            Require all granted
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
" > /etc/apache2/sites-enabled/000-default.conf

/usr/sbin/a2enmod rewrite
/usr/sbin/a2enmod vhost_alias
/usr/bin/systemctl restart apache2

apt install ufw -y
ufw allow ssh
ufw allow http
ufw allow https
mysql_secure_installation
reboot


# ve onde ta instalado
# chown www-data:www-data plugins themes
# chmod 775 plugins themes
# no wp-config.php adicionar a linha: define('FS_METHOD','direct');
