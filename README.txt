About
-----
"All fiction is real, it just takes place in other universes." --Alexander Moses Moffett
The Transverse Traveler Association is a group of people with the ability to travel between universes. The history of this group has not yet been determined, but it includes a character named Zhera with a better-established history.


Disclaimers
-----------
The information in the fixtures (other than the CMS one) is subject to change and additions.
I'm not using South because it annoys me. You use it once, and it has polluted your database. I don't want to give you my ghost migrations.


Deployment
----------
At the moment, it's configured for SQLite and the Django development server. Classy, I know.


Quick start
-----------
Clone the repo
Put a virtual environment in it
pip install -r requirements.txt
python manage.py syncdb --all
python manage.py loaddata all.json
python manage.py runserver

