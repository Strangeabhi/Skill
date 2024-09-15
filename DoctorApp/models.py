from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length = 255)
    specialization = models.CharField(max_length = 125)
    year_of_experience = models.IntegerField()

    def __str__(self):
        return f'[id={self.id}, name={self.name}, specialization={self.specialization}, year_of_experience={self.year_of_experience}]'
