from django.db import models

class Triumph(models.Model):
    term = models.CharField('Search query', max_length=100)
    result = models.CharField('Result', max_length=255)

    def __str__(self):
        return "{0} - {1}".format(self.term)

class Search(models.Model):
    brand = models.CharField('Brand', max_length=7)
    term = models.CharField('Search query', max_length=100)
    result = models.CharField('Result', max_length=255)

    def __str__(self):
        return "{0} - {1}".format(self.brand, self.term)


class UserSearchHistory(models.Model):
    search = models.ForeignKey(Search)
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.term
