pip install opencv-python
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:80
