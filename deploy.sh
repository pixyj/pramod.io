export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon site
python manage.py create_static_site
deactivate
appcfg.py -A pixy-1310 -V v1 update helloworld/
