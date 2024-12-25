 echo "BUILD START"
 python3.12 -m venv env
 source env/bin/activate
 echo "Virtual ENV ACTIVATED"
 sudo apt-get install python-dev default-libmysqlclient-dev
 sudo apt-get install python3-dev
 python3.12 -m pip install -r requirements.txt
 python3.12 manage.py collectstatic
 echo "BUILD END"