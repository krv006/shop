mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	python3 manage.py runserver

admin:
	python3 manage.py createsuperuser