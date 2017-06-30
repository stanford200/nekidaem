# nekidaem

Commands:

cd folder_where_you_will_deploy_project
virtualenv env -p python3
source env/bin/activate

git clone https://github.com/vladimir-grishchenko/nekidaem.git
cd nekidaem/
pip install -r requirements.txt

cd test_project/
python manage.py migrate
python manage.py createsuperuser

python manage.py loaddata fixtures/blog.json fixtures/subscriptions.json

python manage.py runserver


USE IT!!!


ВНИМАНИЕ, SMTP не настроен, GMAIL требует привязку телефона к новому аккаунту.
Можно использовать что-то вроде: https://sendgrid.com/docs/Integrate/Frameworks/django.html
Настройка очень просто, и по сути описана по ссылке.

Для корректного отображения ссылки в письме необходимо задать верный domain, по ссылке: /admin/sites/site/1/change/