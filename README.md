# Django audio does not work



**Django Files**
- main/views.py
- main/templates/audio_test.html


**Flask Files**
- app.py
- templates/index.html






**Run Flask**


cd test

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cd audio_test

flask run

access url - http://127.0.0.1:5000/




**Run Django**

cd test

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cd audio_test

python manage.py runserver

access url - http://127.0.0.1:8000/





