CREATE TABLE ff(Fieldid INT NOT NULL AUTO_INCREMENT, Width INT, Height INT, FieldName TEXT, PRIMARY KEY(Fieldid));

CREATE TABLE drone (Droneid VARCHAR(36), x INT, y INT, DroneStatus TEXT, Fieldid INT, PRIMARY KEY(Droneid));