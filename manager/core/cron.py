import os


def scheduled_every_day():
    os.system("python manage.py send_queued_mail")
