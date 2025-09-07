from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


class User(AbstractUser):
    def notify_new_rate(self, rate):
        send_mail(
            "New rate is submitted",
            f"A new rate has been submitted on {rate.movie.title}.\n"
            f"Score: {rate.score}",
            "imdb@example.com",
            [self.email],
            fail_silently=False,
        )
