from django.shortcuts import render, redirect

# Create your views here.
'''view para registrar dados de request, 
usuário que requisitou e o resultado do TJ'''

def registra_log(request, id_doc):
	user_id = request.user
	obj_doc = Documento.objects.get(id=id_doc)
	id_tjrj = obj_doc.id_tjrj
	desc_doc = obj_doc.doc
	data_criacao = obj_doc.data_criacao
	data_tramitacao = obj_doc.data_tramitacao

	if request.method == 'post':
		request_tipo = 'POST'
	if request.method == 'get':
		request_tipo = 'GET'
	if request.method == 'defele':
		request_tipo = 'delete'
	if request.method == 'put':
		request_tipo = 'PUT'


	log = Log.objects.create(
	id_log = id_log,
	request_tipo = 	request_tipo,
	user_id = 	user_id,
	id_tjrj = 	id_tjrj,
	desc_doc = 	desc_doc,
	data_criacao = 	data_criacao,
	data_tramitacao = 	data_tramitacao,
	)

	return redirect('/')