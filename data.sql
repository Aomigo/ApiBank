PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

-- User table
CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  pseudo TEXT NOT NULL UNIQUE,
  mdp TEXT NOT NULL,
  beneficiaries TEXT NOT NULL DEFAULT '[]', -- Json array of beneficiaries
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- initial data for user table
INSERT INTO user (id, email, pseudo, mdp, beneficiaries, created_at, updated_at) VALUES
(1, 'kyky@mail.com', 'Kyky Kyks', 'kykS95@', '[]', '2026-09-30 15:10:24', '2026-09-30 15:10:24'),
(2, 'jojo@mail.com', 'Jojo Jos', 'jojO95@', '[]', '2026-09-30 15:10:24', '2026-09-30 15:10:24'),
(3, 'toto@mail.com', 'Toto Tots', 'totO95@', '[]', '2026-09-30 15:10:24', '2026-09-30 15:10:24');

-- Account table
CREATE TABLE IF NOT EXISTS account (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pseudo TEXT NOT NULL UNIQUE,
  balance INTEGER NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  uuid TEXT NOT NULL
);

-- Transaction table
CREATE TABLE IF NOT EXISTS "transaction" (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_sender INTEGER NOT NULL,
  id_receiver INTEGER NOT NULL,
  amount INTEGER NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  statut TEXT NOT NULL CHECK (statut IN ('1', '2', '3')),
  FOREIGN KEY (id_sender) REFERENCES user (id)
);

CREATE INDEX IF NOT EXISTS idx_transaction_id_sender ON "transaction"(id_sender);

COMMIT;
