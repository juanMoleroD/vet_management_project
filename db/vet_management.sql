DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_details VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    type VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id),
    treatment_notes TEXT
);