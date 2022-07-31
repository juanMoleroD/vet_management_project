from db.run_sql import run_sql
from models.owner import Owner

def save(owner):
    sql = "INSERT INTO owners (name, contact_details, registered) VALUES (%s, %s, %s) RETURNING id"
    values = [owner.name, owner.contact_details, owner.registered]
    result = run_sql(sql, values)
    owner.id = result[0]["id"]

def select(id):
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    owner = None
    if results:
        result = results[0]
        owner = Owner(result["name"], result["contact_details"], result["registered"], result["id"]) # ATTENTION: may need to encapsulate registered
    return owner

def select_all():
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    owners = []
    for row in results:
        owner = Owner(row["name"], row["contact_details"], row["registered"], row["id"]) # another registered property 
        owners.append(owner)
    return owners

def update(owner):
    sql = "UPDATE owners SET (name, contact_details, registered) = (%s, %s, %s) WHERE id = %s" #as per above comment
    values = [owner.name, owner.contact_details, owner.registered, owner.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)