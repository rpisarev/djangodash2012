from fabric.api import *
from fabric.colors import green, red
from contextlib import contextmanager as _contextmanager
import os,sys

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)
import djangodash2012.settings_prod as settings_prod

env.hosts = [settings_prod.HOST ]
env.password = settings_prod.PASSWORD
env.activate = settings_prod.ENV
env.directory = settings_prod.DIR


@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            print(green('Pulling from git...'))
            yield

def deploy(requirements=False, push=False):
    if push:
        msg = raw_input('Please enter commit message: ')

        print(green('Pushing into git...'))
        local('git add .')
        local('git commit -m "%s"' % msg)
        local('git push')

    with virtualenv():
        print(green('Pulling from git...'))

        run('git pull')

        if requirements:
            print(red('Installing requirements using pip...'))
            run('pip install -r requirements.txt')

        print(green('Migrating database schema...'))
        run('python manage.py syncdb')

        run('python manage.py migrate core')

        print(green('Collecting static files...'))
        run('echo "yes" | python manage.py collectstatic')

    print(green('Restarting site with supervisor...'))
    run('supervisorctl restart djangodash2012')
