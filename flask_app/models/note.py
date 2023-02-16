from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Note:
    db_name = 'users'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.location = db_data['notestaken']
        self.date_of_sight = db_data['date_of_note']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO notes (notestaken, date_of_note, user_id) VALUES (%(notestaken)s,%(date_of_note)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_users = []
        for row in results:
            print(row['notestaken'])
            all_users.append( cls(row) )
        return all_users
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET notestaken=%(notestaken)s, date_of_note=%(date_of_note)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_note(note):
        is_valid = True
        if len(note['notestaken']) < 1:
            is_valid = False
            flash("Notes must be at least 3 characters","note")
        if len(note['date_of_note']) == "":
            is_valid = False
            flash("Please enter a date","note")
        return is_valid
