import xmlrpclib 

db="demo"
username="admin"
password="admin"
url="https://10.0.2.15:8069"

common=xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid=common.authenticate(db,username,password,{})

models=xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

id=models.excute_kw(db,uid,password,'jessebia.atabla','create',[{'name':'jessenia','age':5}])


