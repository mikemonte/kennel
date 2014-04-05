from django.core.mail import send_mail
from django.conf import settings

from fabric.api import lcd, local, run


def prepare_deployment(branch_name):
	local('python manage.py test')
	local('git add -p && git commit')


def deploy():
	with lcd('/path/to/my/prod/area/'):  # need to edit later when ready for production

		# Pull changes from development branch
		local('git pull ~/documents/djcode/flapsta_project/')

		# Migrate Apps
		local('python manage.py migrate core')
		local('python manage.py migrate products')

		# Test Apps
		local('python manage.py test core')
		local('python manage.py test products')

		# Command to restart web server
		local('/my/command/to/restart/webserver')


def hello():
	print 'hello world'


def git_add():
	local('git add .')


def git_commit(msg):
	local('git commit -m %s') % msg


def git_push():
	local('git push -u origin master')


def git_deploy(msg):
	git_add()
	git_commit(msg)
	git_push()





