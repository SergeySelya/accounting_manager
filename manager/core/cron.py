import os

def scheduled_job():
    os.system("python manage.py send_queued_mail")
