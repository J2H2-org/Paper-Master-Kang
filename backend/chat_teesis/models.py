from djongo import models


# Create your models here.

class user_col(models.Model):
    user_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, default='신규 회원', blank=True)
    major = models.CharField(max_length=128, blank=True)
    degree = models.CharField(max_length=16, blank=True)
    contact_email = models.CharField(max_length=32, blank=True)
    belong = models.CharField(max_length=64, blank=True)
    career = models.CharField(max_length=128, blank=True)
    img_link = models.SlugField(max_length=128, blank=True)


class thesis_plan_col(models.Model):
    thesis_plan_Id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=128)
    schedule = models.IntegerField()
    on_domestic = models.BooleanField()  # true : on domestic
    journal_tier = models.BooleanField()  # true : top tier
    purpose = models.CharField(max_length=32)
    user_Id = models.IntegerField()


class mentor_answer_col(models.Model):
    mentor_answer_Id = models.AutoField(primary_key=True)
    mentor_answer = models.TextField()
    mentee_question_Id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    user_Id = models.IntegerField()


class mentee_question_col(models.Model):
    mentee_question_Id = models.AutoField(primary_key=True)
    thesis_plan_Id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    mentee_question = models.TextField()


class c_question_col(models.Model):
    c_question_id = models.AutoField(primary_key=True)
    c_que = models.TextField()
    que_classification_id = models.IntegerField()


class c_answer_col(models.Model):
    c_answer_id = models.AutoField(primary_key=True)
    c_ans = models.TextField()
    c_question_id = models.IntegerField()

class search_info_col(models.Model):
    using = 'default'
    user_Id = models.IntegerField()
    major = models.CharField(max_length=128, blank=True)
    subject = models.CharField(max_length=128, blank=True)
    tag = models.CharField(max_length=128, blank=True)