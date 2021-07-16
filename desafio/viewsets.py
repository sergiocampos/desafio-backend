from rest_framework import viewsets
from rest_framework_permissions import IsAuthenticated
import serializers

'''
Classe viewset que controla acesso à url da api! O permission_class exige
autenticação.
'''
class DocumentoViewSet(viewsets.ModelViewSet):
	
	permission_class = (IsAuthenticated)

	serializers_class = serializers.DocumentoSerializers
	queryset = models.Documento.objects.all()
