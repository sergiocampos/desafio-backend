from django.db import models

# Create your models here.
class Tramitacao(models.Model):
	idtram = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	data = models.DateField()
	doc = models.TextField(blank=True)

	def __str__(self):
		return str(self.doc)