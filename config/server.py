import datetime
from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n%2 == 0

def data_atual(n):
	now = datetime.datetime.now()
	return str(n) + str(now)

def salvar_tarefas(n):
	print(n)
	return n

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.register_function(data_atual, "data_atual")
server.register_function(salvar_tarefas, "salvar_tarefas")
server.serve_forever()
