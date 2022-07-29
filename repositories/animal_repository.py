import pdb
from db.run_sql import run_sql
from repositories import owner_repository, vet_repository
from models.animal import Animal

def save(animal):
    sql = '''INSERT INTO animals (name, date_of_birth, type, owner_id, vet_id, treatment_notes) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id'''
    values = [animal.name, animal.date_of_birth.strftime('%Y-%m-%d'), animal.type, animal.owner.id, animal.vet.id, animal.treatment_notes]
    result = run_sql(sql, values) 
    animal.id = result[0]["id"]

def select(id):
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    animal = None
    if results:
        result = results[0]
        #pdb.set_trace()
        vet = vet_repository.select(result["vet_id"])
        owner = owner_repository.select(result["owner_id"])
        animal = Animal(result["name"], result["date_of_birth"], result["type"], owner, vet, result["treatment_notes"], result["id"])
    return animal

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)