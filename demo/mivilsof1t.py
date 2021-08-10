import functools
import xmlrpclib 

db="demo"
username="admin"
password="admin"
url="https://10.0.2.15:8069"
HOST='10.0.2.15'
PORT=8069
DB='demo'
USER='admin'
PASS='admin'
ROOT='http://%s:%d/xmlrpc/'%(HOST,PORT)

#login
uid=xmlrpclib.ServerProxy(ROOT+'common').login(DB,USER,PASS)
call = functools.partial(xmlrpclib.ServerProxy(ROOT+'object').execute,DB,uid,PASS)

#leer 
registros = call('jessenia.atabla','search_read',[],['name'])

for item in registros:
    print "registro %s"%(item['name'])

#insertar
registro_id = call('jessenia.atabla','create',{'name':'Jessenia',})





#common=xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
#uid=common.authenticate(db,username,password,{})

#models=xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

#id=models.excute_kw(db,uid,password,'jessebia.atabla','read',[ids],{'fields':['name','age','promedio','tablab']})

#print (id)
