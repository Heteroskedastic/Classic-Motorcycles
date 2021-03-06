#!/bin/bash

BRANCH=master
if [ -n "$1" ]; then
    BRANCH=$1
fi

NAME="classicmotor"
GITURL=https://github.com/Old-World-Bikes/Classic-Motorcycles.git
ROOTDIR=/opt/webapps
PROJECTDIR=$ROOTDIR/$NAME
DJANGODIR=$PROJECTDIR/$NAME
ENVDIR=$PROJECTDIR/env
DJANGO_SETTINGS_MODULE=classicmotor.settings.main

echo "+++ Deploying $NAME: BRANCH=$BRANCH PROJECTDIR=$PROJECTDIR ..."

mkdir -p $PROJECTDIR
mkdir -p $PROJECTDIR/run
mkdir -p $PROJECTDIR/logs
if [ -d "$DJANGODIR" ]; then
    cd $DJANGODIR
    git reset --hard HEAD
    git pull origin
    git checkout $BRANCH
else
    git clone $GITURL -b $BRANCH $DJANGODIR
fi
sudo supervisorctl stop $NAME
sleep 1
if [ ! -d "$ENVDIR" ]; then
    virtualenv -p python3 $ENVDIR
fi
source $ENVDIR/bin/activate
cd $DJANGODIR
pip install -r requirements.txt
pip install django-gunicorn
cd $DJANGODIR/classicmotor
python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE --noinput
python manage.py collectstatic --settings=$DJANGO_SETTINGS_MODULE --noinput
sudo supervisorctl start $NAME
sudo service nginx restart

echo
echo "Finished!"
