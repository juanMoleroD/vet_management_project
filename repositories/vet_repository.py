from optparse import Values
import pdb
from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING id"
    values = [vet.name]
    result = run_sql(sql, values)
    vet.id = result[0]["id"]

def select(id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    vet = None
    if results:
        result = results[0]
        vet = Vet(result["name"], result["id"])
    return vet

def select_all():
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    vets = []
    for row in results:
        vet = Vet(row["name"], row["id"])
        vets.append(vet)
    return vets

def update(vet):
    sql = "UPDATE vets SET name = %s WHERE id = %s"
    values = [vet.name, vet.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def get_patients_from_vet_id(id):
    sql = '''SELECT vets.* 
                FROM vets INNER JOIN animals ON vets.id = animals.vet_id
                WHERE animals.vet_id = %s'''
    values = [id]
    results = run_sql(sql, values)