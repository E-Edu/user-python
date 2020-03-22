CREATE TABLE IF NOT EXISTS
User_Users (
    uuid VARCHAR(64) NOT NULL,
    email VARCHAR(255),
    password VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    status INT,
    role INT,
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (uuid)
);

CREATE TABLE IF NOT EXISTS
User_Teachers (
    user_uuid VARCHAR(64) NOT NULL,
    schoolDomain VARCHAR(255),
    token VARCHAR(64),
    PRIMARY KEY (token)
);

CREATE TABLE IF NOT EXISTS
User_Verification (
    user_uuid VARCHAR(64) NOT NULL,
    verification_code VARCHAR(255),
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (user_uuid)
);