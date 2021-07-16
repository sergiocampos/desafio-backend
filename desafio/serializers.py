from rest_framework import serializers
#from desafio import models
from main import models
from tramitacao import models
from log import models


# Caso julgue necessário criar algum serializer
class DocumentoSerializers(serializers.ModelSerializers):

	class Meta:
		model = models.Documento
		fields = '__all__'