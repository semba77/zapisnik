from facade import Facade
from sentences import SentenceFactory
from names import Nameguesser
from fun_fact import Fun_factorior
from animal import Animals
from city import City
from countries import Country
from rivers import River
import ast

sentence = SentenceFactory()
true_name = Nameguesser()
facts = Fun_factorior()
animal = Animals()
city = City()
country = Country()
river = River()
with open('../config/config_file.txt') as f:
    conf_dictionary = ast.literal_eval(f.read())
    skolni = conf_dictionary["skolni"]
    if skolni == False:
        print(1)
        server = conf_dictionary["server"]
        user = conf_dictionary["user"]
        password = conf_dictionary["password"]
        facade = Facade("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE=Omega;UID="+user+";PWD="+password)
    else:
        print(2)
        host = conf_dictionary["host"]
        facade = Facade(f"DRIVER={{SQL Server}};SERVER={host};DATABASE=Omega;Trusted_Connection=yes;")