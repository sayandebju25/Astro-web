from django.db import models
from django.core.validators import MaxValueValidator

class ZodiacSign(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='zodiac_images/')

    def __str__(self):
        return self.name


# from django.core.exceptions import ObjectDoesNotExist

# class Horoscope(models.Model):
#     # Choices for the period
#     PERIOD_CHOICES = [
#         ('daily', 'Daily'),
#         ('weekly', 'Weekly'),
#         ('monthly', 'Monthly'),
#         ('yearly', 'Yearly'),
#     ]

#     zodiac_sign = models.ForeignKey(ZodiacSign, on_delete=models.CASCADE, default=None)
#     period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
#     date = models.DateField()
#     author = models.CharField(max_length=255, default='Anonymous')  # Default author
#     updated_at = models.DateTimeField(auto_now=True)
#     content = models.TextField()
#     lucky_number = models.IntegerField()
#     lucky_color = models.CharField(max_length=50)
#     remedy = models.TextField()
#     health_rating = models.IntegerField(validators=[MaxValueValidator(5)], default=0)  # Default value
#     wealth_rating = models.IntegerField(validators=[MaxValueValidator(5)], default=0)  # Default value
#     love_rating = models.IntegerField(validators=[MaxValueValidator(5)], default=0)  # Default value
#     occupation_rating = models.IntegerField(validators=[MaxValueValidator(5)], default=0)  # Default value
#     family_rating = models.IntegerField(validators=[MaxValueValidator(5)], default=0)  # Default value

#     # Handling the save method
#     def save(self, *args, **kwargs):
#         if not self.zodiac_sign:
#             try:
#                 # Get the actual ZodiacSign object by name
#                 self.zodiac_sign = ZodiacSign.objects.get(name='libra')
#             except ObjectDoesNotExist:
#                 # Handle if 'libra' doesn't exist
#                 raise ValueError("ZodiacSign 'libra' does not exist.")
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f'{self.zodiac_sign.name} Horoscope: {self.date}'
