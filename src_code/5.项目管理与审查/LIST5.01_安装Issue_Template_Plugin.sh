$ wget https://bitbucket.org/akiko_pusu/redmine_issue_templates/downloads/redmine_issue_templates-0.0.9.zip
$ sudo mkdir /usr/share/redmine/plugins
$ unzip redmine_issue_templates-0.0.9.zip -d /usr/share/redmine/plugins/
$ cd /usr/share/redmine
$ sudo chown -R www-data:www-data plugins
$ sudo mkdir -p public/plugin_assets
$ sudo cp -pr plugins/redmine_issue_templates/assets public/plugin_assets/redmine_issue_templates
$ sudo chown -R www-data:www-data public/plugin_assets
$ sudo rake redmine:plugins:migrate RAILS_ENV=production
$ sudo bundle install
$ sudo service apache2 reload

# =============================================================================
# 在执行“sudo bundle install”的时候，
# 若遇到如下错误信息：
# An error occurred while installing json (2.0.2), and Bundler cannot continue.
# Make sure that `gem install json -v '2.0.2'` succeeds before bundling.
# 
# 需要编辑文件“/usr/share/redmine/plugins/redmine_issue_templates/Gemfile”，
# 将第4行的gem "simplecov"改为gem "simplecov", "0.9.0"，即
# 
# source 'https://rubygems.org'
# 
# group :test do
#   gem "simplecov", "0.9.0"
#   gem "simplecov-rcov"
#   gem "yard"
# end
# 
# 修改后重新执行“sudo bundle install”
#
# 若遇到如下错误信息：
# Could not verify the SSL certificate for https://rubygems.org/.
# There is a chance you are experiencing a man-in-the-middle attack, but most likely your system doesn't
# have the CA certificates needed for verification. For information about OpenSSL certificates, see
# http://bit.ly/ruby-ssl. To connect without using SSL, edit your Gemfile sources and change 'https' to
# 'http'.
# 
# 需要编辑文件“/usr/share/redmine/Gemfile”和“/usr/share/redmine/plugins/redmine_issue_templates/Gemfile”，
# 分别将第一行“source 'https://rubygems.org'”中的“https”改为“http”
# 
# 修改后重新执行“sudo bundle install”