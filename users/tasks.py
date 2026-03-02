from celery import shared_task
import time

@shared_task
def send_welcome_email(email):
    print(f"Sending welcome email to {email}...")
    time.sleep(5)
    print("Email sent successfully!")