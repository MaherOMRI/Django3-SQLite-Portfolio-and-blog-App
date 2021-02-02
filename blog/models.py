from django.db import models

class Blog(models.Model):
     
    blogtitle = models.CharField(max_length=100)
    blogdate = models.DateField()  
    blogmain = models.TextField()

    def __str__(self):
        """Function to display titles into admin pages""",
        return self.blogtitle