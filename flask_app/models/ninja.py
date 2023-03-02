
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    db="dojos_and_ninjas_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id=data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query = """INSERT INTO ninjas (first_name, last_name, age,dojo_id)
                VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
    
        results = connectToMySQL(cls.db).query_db(query)
        
        ninjas = []
    
        for result in results:
            ninjas.append( cls(result) )
        return ninjas

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return result[0]

    @classmethod
    def change_ninja(cls,data):
        query="""UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s,
                age=%(age)s,dojo_id=%(dojo_id)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def delete_ninja(cls,data):
        query="DELETE FROM ninjas WHERE id=%(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result



