from django.db import models

class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['show_title']) < 2:
            errors['show_title'] = "Show title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network name must be at least 3 characters"
        if postData['description'] != '' and len(postData['description']) < 10:
            errors['description'] = "Show description should be at least 10 characters"
        return errors
        


class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()
