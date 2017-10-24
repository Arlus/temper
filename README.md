sudo apt install ufw python-dev python-virtualenv python-pip git nginx supervisor git
mkdir ~/.virtualenvs && cd ~/.virtualenvs
virtualenv temper
source ~/.virtualenvs/temper/bin/activate
sudo nano /etc/nginx/sites-available/temper
mkdir ~/sites && cd ~/sites
git clone https://github.com/alexandersimoes/temper.git
cd temper
pip install -r requirements.txt

sudo ln -s /etc/nginx/sites-available/temper.conf /etc/nginx/sites-enabled/
sudo service nginx reload

sudo apt-get install supervisor
sudo vim /etc/supervisor/conf.d/temper.conf

sudo pkill gunicorn

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start temper

coverage run tests.py
coverage report -m *.py