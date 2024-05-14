-- Crea la tabla de usuarios

CREATE TABLE users (

    username varchar(16) NOT NULL, -- username / nombre de usuario
    passcode varchar(20) NOT NULL, -- passcode / contraseña
    PRIMARY KEY (username)
);

CREATE TABLE users_Messages (

    username VARCHAR(16) NOT NULL, -- username / nombre de usuario
    secret_key TEXT NOT NULL, -- secret_key / clave secreta
    encrypted_message TEXT NOT NULL, -- encrypted_message / mensaje encriptado
    original_message TEXT NOT NULL -- original_message / mensaje original
    
);