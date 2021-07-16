from django.shortcuts import render, redirect
from .models import RegistraRequest
# Create your views here.
#view para registrar usuário e id_tj quando ocorrer request

def registra_request(request, id_doc):
	user = request.user
	documento = Documento.objects.get(id=id_doc)
	id_tjrj = documento.id_tjrj

	registro = RegistraRequest.objects.create(
		user = user,
		id_tjrj = id_tjrj
		)



	return redirect('/')