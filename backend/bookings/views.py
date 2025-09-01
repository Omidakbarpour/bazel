from rest_framework import viewsets, permissions, status, decorators
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().select_related('user', 'specialist')
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user, status='pending')
        if booking.overlaps():
            booking.delete()
            raise ValueError('Booking overlaps with existing booking')

    @decorators.action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        booking = self.get_object()
        if booking.status != 'pending':
            return Response({'detail': 'not_pending'}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = 'confirmed'
        booking.save()
        return Response({'detail': 'confirmed'})
