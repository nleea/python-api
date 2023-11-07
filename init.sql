use masiva;

CREATE TABLE test_table
(
    id INT NOT NULL
    AUTO_INCREMENT,
    name VARCHAR
    (100) NOT NULL,
    valid BOOLEAN NOT NULL,
    PRIMARY KEY
    (id)
);

    CREATE TABLE zip_codes
    (
        id INT NOT NULL
        AUTO_INCREMENT,
    zip_code VARCHAR
        (5) NOT NULL,
    valid BOOLEAN NOT NULL,
    city VARCHAR
        (255) NOT NULL,
    state VARCHAR
        (2) NOT NULL,
    county VARCHAR
        (255) NOT NULL,
    timezone VARCHAR
        (255) NOT NULL,
    area_codes JSON NOT NULL,
    country VARCHAR
        (2) NOT NULL,
    lat DECIMAL
        (10, 6) NOT NULL,
    lon DECIMAL
        (10, 6) NOT NULL,
    PRIMARY KEY
        (id)
);


        ALTER TABLE zip_codes
ADD CONSTRAINT unique_zip_code UNIQUE (zip_code);

        INSERT INTO test_table
            (name,valid)
        values
            ("test", 1);
