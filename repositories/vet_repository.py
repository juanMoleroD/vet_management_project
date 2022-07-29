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
    result = run_sql(sql, values)[0]
    vet = None
    if result:
        vet = Vet(result["name"], result["id"])
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)