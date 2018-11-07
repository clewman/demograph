
from django.db import models



class EducationLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IncomeLevel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class County(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    fips = models.CharField(max_length=50)

    def __str__(self):
        return self.state.name + ' - ' + self.name


class IncomeData(models.Model):
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    income_level = models.ForeignKey(IncomeLevel, on_delete=models.CASCADE)
    population = models.IntegerField()
    year = models.IntegerField()
    county = models.ForeignKey(County, on_delete=models.PROTECT)

    def __str__(self):
        return self.education_level.name + ' - ' + self.gender.name + ' - ' + self.income_level.name + ' - ' + str(self.population) + ' - ' + str(self.year) + ' - ' + self.county.state.name + ' - ' + self.county.name


    def to_dictionary(self):
        return {#'education_level': self.education_level.name,
                #'gender': self.gender.name,
                #'income_level': self.income_level.name,
                'year': self.year,
                #'population': self.population,
                #'county': self.county.name
        }