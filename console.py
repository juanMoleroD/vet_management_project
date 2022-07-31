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

vet_3 = Vet("Dr Hamster")
vet_repository.save(vet_3)

vet_4 = Vet("Hershel Greene")
vet_repository.save(vet_4)

owner_1 = Owner("Mike Tyson", "077-6453-89766") #077-MIKE-TYSON
owner_repository.save(owner_1)

owner_2 = Owner("Taylor Swift", "0700-TAYLOR")
owner_repository.save(owner_2)

owner_3 = Owner("Harry Potter", "07914-914-914")
owner_repository.save(owner_3)

animal_1 = Animal("Kenya", date(2010,6,24), "tiger", owner_1, vet_1, "All meat diet forever, keep your arms safe!")
animal_repository.save(animal_1)

animal_2 = Animal("Meredith", date(2011,1,1), "Cat", owner_2, vet_3, "Only eats salmon")
animal_repository.save(animal_2)

animal_3 = Animal("Olivia", date(2014,1,1), "Cat", owner_2, vet_3, "Mrs Swift spoils her rotten")
animal_repository.save(animal_3)

animal_4 = Animal("Hedwig", date(1997,1,1), "Snowy Owl", owner_3, vet_4, "Seems magical sometimes...")
animal_repository.save(animal_4)

#pdb.set_trace()