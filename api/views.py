from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


# Create your views here.

class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)

            return Response(
                {
                    'data': serializer.data,
                    'message': 'Orders retrieved Successfully'
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    'data': {},
                    'message': 'something went wrong'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)

            if not serializer.is_valid():
                return Response(
                    {
                        'data': serializer.errors,
                        'message': 'something went wrong'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save()

            return Response(
                {
                    'data': serializer.data,
                    'message': 'Order placed successfully'
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    'data': {},
                    'message': 'something went wrong'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get('id'))

            if not order.exists():
                return Response(
                    {
                        'data': {},
                        'message': "order not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = OrderSerializer(order[0], data=data, partial=True)

            if not serializer.is_valid():
                return Response(
                    {
                        'data': serializer.errors,
                        'message': 'something went wrong'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save()

            return Response(
                {
                    'data': serializer.data,
                    "message": "Order updated Successfully"
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    "data": {},
                    "message": "Something went wrong"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get('id'))

            if not order.exists():
                return Response(
                    {
                        "data": {},
                        "message": "Order not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            order[0].delete()

            return Response(
                {
                    "message": "Order deleted successfully"
                },
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as e:
            return Response(
                {
                    "data": {},
                    "message": "Something went Wrong"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
