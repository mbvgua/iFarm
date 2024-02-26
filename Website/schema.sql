CREATE TABLE login(
	email TEXT,
	password TEXT,
	login_id INTEGER, 
	FOREIGN KEY(login_id) REFERENCES users(id)
);

CREATE TABLE register(
	username TEXT,
	email TEXT,
	password TEXT,
	register_id INTEGER,
	FOREIGN KEY(register_id) REFERENCES users(id)
);

CREATE TABLE users(
	id INTEGER,
	email TEXT,
	username TEXT,
	PRIMARY KEY(id)
);

CREATE TABLE device(
	id INTEGER,
	password TEXT
);

CREATE TABLE report(
	prediction TEXT
);




