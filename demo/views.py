from rest_framework import viewsets
from rest_framework import filters
from demo.models import MyModel
from demo.serializers import MyModelSerializer


class MyModelsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    filter_backends = (filters.DjangoObjectPermissionsFilter,)
