from djongo import models
from djongo import models as mongoModels


# Create your models here.

class user_col(models.Model):
    using = 'default'
    user_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, default='신규 회원', blank=True)
    major = models.CharField(max_length=128, blank=True)
    degree = models.CharField(max_length=16, blank=True)
    contact_email = models.CharField(max_length=32, blank=True)
    belong = models.CharField(max_length=64, blank=True)
    career = models.CharField(max_length=128, blank=True)
    img_link = models.SlugField(max_length=128, blank=True)

class thesis_plan_col(models.Model):
    using = 'default'
    thesis_plan_Id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=128)
    schedule = models.IntegerField()
    on_domestic = models.BooleanField()  # true : on domestic
    journal_tier = models.BooleanField()  # true : top tier
    purpose = models.CharField(max_length=32)
    user_Id = models.IntegerField()

class mentor_answer_col(models.Model):
    using = 'default'
    mentor_answer_Id = models.BigAutoField(primary_key=True)
    mentor_answer = models.TextField()
    mentee_question_Id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    user_Id = models.IntegerField()

class mentee_question_col(models.Model):
    using = 'default'
    mentee_question_Id = models.BigAutoField(primary_key=True)
    thesis_plan_Id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    mentee_question = models.TextField()

class search_col(models.Model):
    using = 'default'
    search_Id = models.AutoField(primary_key=True)
    major = models.CharField(max_length=128, blank=True)
    career = models.TextField(blank=True)

