from rest_framework.response import Response
from rest_framework.views import APIView
from zeep import Client
from zeep.wsse.username import UsernameToken
from .models impor *
from django.shortcuts import render, redirect
import psycopg2


#view para acesso ao serviço soap do TJRJ
def call_soap(request, id_tjrj):

	cliente = Client(wsdl_url, wsse=UsernameToken(username, password)
	req_data = {username: my_username, password: my_password, doc_id: id_tjrj}

#view para localizar os dados do documento no banco!
def search_documento(request, id):
	conn = psycopg2.connect(
		host="host",
		user="user",
		password="senha")
	conn.set_session(autocommit=True)

	cur = conn.cursor()
	
	cur.execute(query_para_pegar os dados)#doc = Documento.objects.get(id=id)
	dados = cur.fetchall()

	#return render()