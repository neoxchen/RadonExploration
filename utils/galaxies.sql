CREATE TABLE galaxies
(
    id              SERIAL PRIMARY KEY NOT NULL,
    source_id       VARCHAR            NOT NULL UNIQUE,
    ra              DECIMAL(25, 20)    NOT NULL,
    dec             DECIMAL(25, 20)    NOT NULL,
    gal_prob        DECIMAL(25, 20)    NOT NULL,
    bin             SMALLINT           NOT NULL,
    status          VARCHAR            NOT NULL DEFAULT 'Pending',
    failed_attempts SMALLINT           NOT NULL DEFAULT 0
);

CREATE TABLE fits_data
(
    source_id  VARCHAR PRIMARY KEY REFERENCES galaxies (source_id),
    rotation_g FLOAT NULL,
    rotation_r FLOAT NULL,
    rotation_i FLOAT NULL,
    rotation_z FLOAT NULL
);

SELECT status, COUNT(*) FROM galaxies GROUP BY status;

SELECT * FROM galaxies WHERE status='Fetched' LIMIT 100;

SELECT * FROM fits_data;

DELETE FROM fits_data;

UPDATE galaxies SET status = 'Fetched' WHERE status = 'Transformed';

SELECT * FROM galaxies, fits_data WHERE galaxies.source_id=fits_data.source_id;