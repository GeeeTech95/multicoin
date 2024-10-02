#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
python manage.py loaddata country.json
#python manage.py loaddata plans.json
#python manage.py loaddata superuser.json

export DJANGO_SUPERUSER_EMAIL=admin.multicoin@bitcoinvoyager.finance
export DJANGO_SUPERUSER_USERNAME=admin1
export DJANGO_SUPERUSER_PASSWORD=NRX6@i*845

python manage.py createsuperuser --no-input
