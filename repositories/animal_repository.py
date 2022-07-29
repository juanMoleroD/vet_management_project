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
        vet = vet_repository.select(result["vet_id"])
        owner = owner_repository.select(result["owner_id"])
        animal = Animal(result["name"], result["date_of_birth"], result["type"], owner, vet, result["treatment_notes"], result["id"])
    return animal

def select_all():
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    animals = []
    for row in results:
        vet = vet_repository.select(row["vet_id"])
        owner = owner_repository.select(row["owner_id"])
        animal = Animal(row["name"], row["date_of_birth"], row["type"], owner, vet, row["treatment_notes"], row["id"])
        animals.append(animal)
    return animals

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)