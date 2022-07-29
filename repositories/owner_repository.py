from db.run_sql import run_sql
from models.owner import Owner

def save(owner):
    sql = "INSERT INTO owners (name, contact_details) VALUES (%s, %s) RETURNING id"
    values = [owner.name, owner.contact_details]
    result = run_sql(sql, values)
    owner.id = result[0]["id"]

def select(id):
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    owner = None
    if result:
        owner = Owner(result["name"], result["contact_details"])
    return owner

def select_all():
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    owners = []
    for row in results:
        owner = Owner(row["name"], row["contact_details"], row["id"])
        owners.append(owner)
    return owners

def update(owner):
    sql = "UPDATE owners SET (name, contact_details) = (%s, %s) WHERE id = %s"
    values = [owner.name, owner.contact_details, owner.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)