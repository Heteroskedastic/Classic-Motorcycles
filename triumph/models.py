from django.db import models

class Triumph(models.Model):
    term = models.CharField('Search query', max_length=100)
    result = models.CharField('Result', max_length=255)

    def __str__(self):
        return self.term


class UserSearchHistory(models.Model):
    term = models.CharField('Search query', max_length=100)
    result = models.CharField('Result', max_length=255)
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()
    

    def __str__(self):
        return self.term
