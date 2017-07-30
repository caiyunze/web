$ python manage.py makemigrations polls
You are trying to add a non-nullable field 'pub_date' to poll without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
