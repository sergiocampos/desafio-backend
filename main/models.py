from django.db import models

# Create your models here.
class RegistraRequest(models.Model):
	id_reg_request = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	user = request.user
	id_tjrj = models.IntegerField(blank=False)

	def __str__(self):
		return str(self.id_reg_request)