from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Rate(models.Model):
    # == Fields ==
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # == Relations ==
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie', 'user'], name='unique_movie_user_rate')
        ]

    def __str__(self):
        return f'Rate {self.score} for Movie<{self.movie_id}> by User<{self.user_id}>'
