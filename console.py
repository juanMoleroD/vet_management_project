import pdb
from datetime import datetime, date
from models.vet import Vet
from models.owner import Owner
from models.animal import Animal

from repositories import animal_repository, owner_repository, vet_repository

animal_repository.delete_all()
owner_repository.delete_all()
vet_repository.delete_all()

vet_1 = Vet("Ace Ventura")
vet_repository.save(vet_1)

vet_2 = Vet("Dr Dolitle")
vet_repository.save(vet_2)

owner_1 = Owner("Mike Tyson", "077-6453-89766") #077-MIKE-TYSON
owner_repository.save(owner_1)

animal_1 = Animal("Tony The Tiger", datetime(2010,6,24), "tiger", owner_1, vet_1, "All meat diet forever, doesn't like light")
animal_repository.save(animal_1)

#pdb.set_trace()

print(animal_repository.select_all())

