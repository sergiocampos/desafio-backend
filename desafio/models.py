from django.db import models
from uuid import uuid4


# Caso precise criar algum modelo para sua aplicação

class Documento(models.Model):
	id_doc = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	id_tjrj = models.IntegerField(blank=False, null=False)
	doc = models.TextField(blank=False)
	data_criacao = models.DateField()
	data_tramitacao = models.DateField()

	def __str__(self):
		return str(self.doc)