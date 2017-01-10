#!/bin/bash

# Assumes that django is running on 4444. Be careful about this!
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon pramod_io
python manage.py create_static_site
deactivate
appcfg.py -A pixy-1310 -V v1 update helloworld/
