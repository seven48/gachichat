git fetch --all
git reset --hard origin/${BRANCH}

python manage.py migrate

>&2 echo "Running server http://localhost:${PORT:=8000}"
python manage.py runserver 0.0.0.0:8080
