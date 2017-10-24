**TEMPER ONBOARDING RETENTION CURVE CHART**

Setup Instructions(Ubuntu 16.04 Server)

1. Install system requirements.
    sudo apt install python-dev python-virtualenv python-pip git nginx supervisor git
    
2. Create the virtualenvironment.

    mkdir ~/.virtualenvs && cd ~/.virtualenvs
    virtualenv temper -p /usr/bin/python2
    source ~/.virtualenvs/temper/bin/activate
    
    
3. Clone the repo and install app requirements.
    mkdir ~/sites && cd ~/sites
    git clone https://github.com/Arlus/temper.git
    cd temper
    pip install -r requirements.txt
    
4. Create Nginx configuration for the app.  
    sudo nano /etc/nginx/sites-available/temper
    - You can copy the configuration outlined in the bundled file temper_nginx.conf.

    sudo ln -s /etc/nginx/sites-available/temper.conf /etc/nginx/sites-enabled/
    sudo service nginx reload

5. Supervisor setup for process control and monitoring.
    sudo apt-get install supervisor
    sudo vim /etc/supervisor/conf.d/temper.conf
    - You can copy the configuration outlined in the bundled file temper_supervisor.conf.

6. Kill gunicorn and restart the process using Supersisor. 
    sudo pkill gunicorn
    
    sudo supervisorctl reread
    sudo supervisorctl update
    sudo supervisorctl start temper


Running tests
    coverage run tests.py
    coverage report -m *.py
