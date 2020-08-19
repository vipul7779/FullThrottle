from django.db import models

class Date(models.Model):
     user_id = models.IntegerField()
     start_time = models.DateTimeField('Start Time')
     end_time = models.DateTimeField('End Time')
     counter = models.IntegerField()

     class Meta:
        unique_together = (("user_id", "counter"),)

class Member_Details(models.Model):
    real_name = models.CharField(max_length = 100)
    tz = models.CharField(max_length=100)
    activity_periods = models.ForeignKey("Date", on_delete = models.CASCADE, null=True) # models.ForeignKey('Date', on_delete = models.CASCADE, null=True)

class Member(models.Model):
    ok = models.BooleanField(default=False) 
    members = models.ForeignKey('Member_Details', on_delete = models.CASCADE, null=True)
