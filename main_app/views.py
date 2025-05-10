from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from main_app.models     import OrderItem
from main_app.serializers import OrderItemSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class OrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderItem.objects.select_related(
        'order__user',
        'product'
    ).all()
    serializer_class = OrderItemSerializer
    pagination_class = StandardResultsSetPagination
