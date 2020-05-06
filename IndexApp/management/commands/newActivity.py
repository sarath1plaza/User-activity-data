from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from IndexApp.models import ActivityPeriods

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        #Set start_time value as current date and time
        now = datetime.now()
        start_date=now.strftime("%b %d %Y")
        start_time=now.strftime("%I:%M %p")
        start_datetime=start_date+'  '+start_time

        # Set end_time value as 1 hour after current date and time
        end_time = datetime.now() + timedelta(minutes=60)
        formated_endtime='{:%H:%M %p}'.format(end_time)
        end_date = now.strftime("%b %d,%Y")
        end_datetime = end_date + '  ' + formated_endtime

        #get member id from command line
        memberid=input("Enter member Id: ")
        ActivityPeriods.objects.create(start_time=start_datetime,end_time=end_datetime,member_id=memberid)
        self.stdout.write("Successfully added new activity")