from rest_framework import authentication
from engage.models import Contact
from .serializers import ContactSerializer
from rest_framework import viewsets


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Contact.objects.all()
