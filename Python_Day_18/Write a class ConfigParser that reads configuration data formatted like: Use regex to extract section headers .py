'''Write a class ConfigParser that reads configuration data formatted like:
Use regex to extract section headers ([Section]) and key-value pairs.'''

class db:
    host="localhost"
    port=5432

class Server(db):
    debug=True
    port=8000

output = {
    "Database" : {'host':db.host,'port': db.port},
    "Server" : {'debug':True, 'port':Server.port}
}
for i in output:
    print(i,output[i])
