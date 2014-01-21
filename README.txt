About
-----
"All fiction is real, it just takes place in other universes." --Alexander Moses Moffett
The Transverse Traveler Association is a group of people with the ability to travel between universes. The history of this group has not yet been determined, but it includes a character named Zhera with a better-established history.


Disclaimers
-----------
The information in the fixtures (other than the CMS one) is subject to change and additions.


Quick start
-----------
Clone the repo
Put a virtual environment in it
pip install -r requirements.txt
python manage.py syncdb --all
python manage.py loaddata cms.json archive.json community.json
python manage.py runserver


Fixtures
--------
cms.json contains NEARLY all CMS-managed content.
There is a custom plugin defined in the "community" app, so its table is in community.json.
