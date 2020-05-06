from rest_framework import serializers
from . models import Members
from . models import ActivityPeriods


# Manage activity details
class activitySerializer(serializers.ModelSerializer):
    class Meta:
        model=ActivityPeriods
        fields = ['start_time','end_time']


# Manage member details
class membersSerializer(serializers.ModelSerializer):
    activity_periods = activitySerializer(many=True,read_only=True)
    class Meta:
        model=Members
        fields = ['id','real_name','tz','activity_periods']







