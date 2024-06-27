from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Card
from .serializers import CardSerializer


class CardCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if 'file' in request.FILES:
            # Processar arquivo aqui
            # Exemplo simplificado, deve ser adaptado para processamento assíncrono em produção
            file = request.FILES['file']
            for line in file:
                card_number = line.decode().strip()
                Card.objects.create(card_number=card_number)
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardCheckAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, card_number):
        card = Card.objects.filter(card_number=card_number).first()
        if card:
            return Response({'exists': True, 'card_id': card.id})
        return Response({'exists': False})
