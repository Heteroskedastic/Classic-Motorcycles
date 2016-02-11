from django.db import models

class Triumph(models.Model):
    term = models.CharField('Search query', max_length=100)
    result = models.CharField('Result', max_length=255)

    def __str__(self):
        return "{0} - {1}".format(self.term)

class Part(models.Model):
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.description

class Search(models.Model):
    brand = models.CharField('Brand', max_length=7)
    term = models.CharField('Search query', max_length=100)
    results = models.ManyToManyField('Part', blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.brand, self.term)


class UserSearchHistory(models.Model):
    search = models.ForeignKey(Search)
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.term

class UserFeedback(models.Model):
    search = models.ForeignKey(Search)
    date = models.DateTimeField()
    comment = models.CharField(max_length=2000)
    
    def __str__(self):
        return "<Feedback:ID={0}>".format(self.id) 