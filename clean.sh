rm -r MicroBiome/__pycache__
rm -r MicroBiome/migrations
rm db.sqlite3
python manage.py makemigrations MicroBiome
python manage.py migrate
