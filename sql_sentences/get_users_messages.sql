SELECT secret_key, encrypted_message, original_message
FROM users_messages
WHERE username = %s 