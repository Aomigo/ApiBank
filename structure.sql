

--
-- STRUCTURE, to see the real SQL file, go to data.sql
--


CREATE TABLE user(
    id INT UNSIGNED  AUTO_INCREMENT,
    email VARCHAR(256) NOT NULL UNIQUE,
    pseudo VARCHAR(256) NOT NULL UNIQUE,
    mdp VARCHAR(256) NOT NULL , 
    balance INT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)
CHARACTER SET 'utf8'
ENGINE = INNODB;

INSERT INTO user(id, email, pseudo, mdp, balance, created_at)
VALUES     
    ('1', 'kyky@mail.com', 'Kyky Kyks', 'kykS95@', '0', NOW()),
    ('2', 'jojo@mail.com', 'Jojo Jos', 'jojO95@', '15', NOW()),
    ('3', 'toto@mail.com', 'Toto Tots', 'totO95@', '90', NOW());

CREATE TABLE transaction (
    id INT UNSIGNED AUTO_INCREMENT,
    id_sender INT UNSIGNED NOT NULL,
    id_receiver INT UNSIGNED NOT NULL,
    amount INT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    statut ENUM ('1','2','3') NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_sender) REFERENCES user(id),
    FOREIGN KEY (id_sender) REFERENCES user(id)
)
CHARACTER SET 'utf8'
ENGINE = INNODB;

ALTER TABLE user RENAME TO account;

CREATE TABLE account(
    id INT UNSIGNED  AUTO_INCREMENT,
    pseudo VARCHAR(256) NOT NULL UNIQUE,
    balance INT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)
CHARACTER SET 'utf8'
ENGINE = INNODB;

ALTER TABLE account RENAME TO user;

ALTER TABLE user DROP balance;

ALTER TABLE account
	ADD uuid VARCHAR(256) NOT NULL;


-- id to change (uuid)
CREATE TABLE beneficiary (
    id INT UNSIGNED AUTO_INCREMENT,
    id_beneficiary INT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (id_beneficiary) REFERENCES user(id)
)
CHARACTER SET 'utf8'
ENGINE = INNODB;