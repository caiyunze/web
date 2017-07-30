$ sudo mkdir /usr/share/redmine/plugins
$ wget http://projects.andriylesyuk.com/attachments/download/563/redmine_scm-0.5.0b.tar.bz2
$ sudo tar xfj redmine_scm-0.5.0b.tar.bz2 -C /usr/share/redmine/plugins/
$ cd /usr/share/redmine/
$ sudo chown -R www-data:www-data plugins/redmine_scm/
$ sudo rake redmine:plugins:migrate RAILS_ENV=production
$ sudo service apache2 restart
