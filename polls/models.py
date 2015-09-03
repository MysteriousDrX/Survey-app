from django.db import models

class Question(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharFeild(max-length=200)
    pub_date = models.DateTimeFeild('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharFeild(max_legth=200)
    votes= models.IntegerFeild(default=0)