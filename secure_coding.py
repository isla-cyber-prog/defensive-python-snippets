import sqlite3
import re

# =====================================================================
# 1. SQL INJECTION PREVENTION (GCSE Database Concepts & OWASP Top 10)
# =====================================================================

def vulnerable_login(username, password):
    """
    INSECURE: Uses string concatenation. 
    An attacker can input: ' OR '1'='1 as the username to bypass login.
    """
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return query

def secure_login(username, password):
    """
    SECURE: Uses parameterized queries (Prepared Statements).
    The database treats input strictly as data, neutralizing SQL injection.
    """
    # Example using standard Python sqlite3 syntax
    # conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return "SELECT * FROM users WHERE username = ? AND password = ?"


# =====================================================================
# 2. INPUT VALIDATION & SANITISATION (GCSE OCR Component 2.2)
# =====================================================================

def validate_user_input(user_input):
    """
    SECURE: Enforces strict length restriction and type validation.
    Prevents buffer issues or unexpected processing anomalies.
    """
    # Check length constraint
    if len(user_input) > 20 or len(user_input) == 0:
        return False, "Error: Input must be between 1 and 20 characters."
    
    # Allow-list approach: Only alphanumeric characters allowed
    if not user_input.isalnum():
        return False, "Error: Special characters are not permitted."
    
    return True, "Input is valid and safe."

# Quick local tests to verify functionality
if _name_ == "_main_":
    print("--- Testing SQL Injection Vulnerability ---")
    bad_user = "' OR '1'='1"
    print(f"Vulnerable Query: {vulnerable_login(bad_user, 'password123')}")
    print(f"Secure Query (Placeholders used): {secure_login(bad_user, 'password123')}")
    
    print("\n--- Testing Input Validation ---")
    print(validate_user_input("Isla123"))      # Valid
    print(validate_user_input("Isla!@#"))
