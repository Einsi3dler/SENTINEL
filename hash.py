from werkzeug.security import generate_password_hash, check_password_hash

# Test hashing and checking
test_password = "1234"
hashed_password = generate_password_hash(test_password)
print("Hashed:", hashed_password)
print(len(hashed_password))
assert check_password_hash(hashed_password, test_password), "Hash check failed!"

