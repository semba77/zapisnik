from facade import Facade
import ast

with open('..\Omega\config/config_file.txt', ) as f:
    conf_dictionary = ast.literal_eval(f.read())
    server = conf_dictionary["host"]
    user = conf_dictionary["user"]
    password = conf_dictionary["password"]
    facade = Facade(server,user,password)