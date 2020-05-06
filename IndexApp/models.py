from django.db import models

# Create table Members to store member details
class Members(models.Model):
    id=models.CharField(primary_key=True, max_length=50)  # Member id
    real_name=models.CharField(max_length=50)             # Member name
    tz=models.CharField(max_length=100)                   # Member address/location

# Create table ActivityPeriods to store activity details(start_time and end_time)
class ActivityPeriods(models.Model):
    member = models.ForeignKey(Members, related_name='activity_periods', on_delete=models.CASCADE)
    start_time=models.CharField(max_length=50)            # Activity start_time
    end_time=models.CharField(max_length=50)              # Activity end_time

    class Meta:
        pass

    def __str__(self):
        return '%s: %s' % (self.start_time, self.end_time)
