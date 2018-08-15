from django.db import models

class Code(models.Model):
    Title = models.CharField(max_length = 200, blank=False)
    Content = models.TextField(blank=False)
    Date = models.DateTimeField('published date')
    Language = models.CharField(max_length= 100, blank= False)

    def __str__(self):
        return ('%s' % self.Title)


