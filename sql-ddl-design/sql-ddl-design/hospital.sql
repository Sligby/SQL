DROP DATABASE if EXISTS hospital;

CREATE DATABASE hospital;

-- doctors
Create TABLE doctors(
    id SERIAL PRIMARY KEY,
    names TEXT NOT NULL,
    contact_info varchar 
);
-- patients
Create TABLE patients(
    id SERIAL PRIMARY KEY,
    patient_name TEXT NOT NULL,
    contact_info TEXT

);

-- visits
CREATE TABLE visits(
    visit_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients ON DELETE CASCADE,
    doctor_id INTEGER REFERENCES doctors ON DELETE CASCADE,
    diagnosis TEXT NOT NULL

);