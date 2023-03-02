
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja
class Dojo:

    db="dojos_and_ninjas_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]
    @classmethod
    def save_dojo(cls,data):
        query = """INSERT INTO dojos (name)
                VALUES (%(name)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
    
        results = connectToMySQL(cls.db).query_db(query)
    
        dojos = []

        for result in results:
            dojos.append( cls(result) )
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        dojo=cls(result[0])
        return dojo

    @classmethod
    def get_one_with_ninjas(cls,data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojos.id=%(id)s"
        results=connectToMySQL(cls.db).query_db(query,data)
        dojo=cls(results[0])
        for item in results:
            print(item)
            temp_ninja = {
                'id':item['ninjas.id'],
                'first_name':item['first_name'],
                'last_name':item['last_name'],
                'age':item['age'],
                'dojo_id':item['dojo_id'],
                'created_at':item['ninjas.created_at'],
                'updated_at':item['ninjas.updated_at'],   
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        print(dojo.ninjas)
        return dojo
        


    

