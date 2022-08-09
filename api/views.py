from rest_framework import viewsets
from .models import Income
from .serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.order_by("start_age")
    serializer_class = IncomeSerializer
