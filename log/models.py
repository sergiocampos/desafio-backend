from django.db import models
from uuid import uuid4

# Create your models here.

class Log(models.Model):
	id_log = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	request_tipo = models.CharField(max_length=100, blank=False)
	user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	id_tjrj = models.IntegerField(blank=False, null=False)
	desc_doc = models.TextField(blank=False)
	data_criacao = models.DateField()
	data_tramitacao = models.DateField()

	def __str__(self):
		return str(self.doc)