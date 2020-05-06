from IndexApp.models import Members
from rest_framework import viewsets
from rest_framework import permissions
from IndexApp.serializers import membersSerializer
from UserActivity.pagination import CustomPagination

# Return response- User activity details

class MemberViewSet(viewsets.ModelViewSet): 
    queryset = Members.objects.all()
    serializer_class = membersSerializer
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]



