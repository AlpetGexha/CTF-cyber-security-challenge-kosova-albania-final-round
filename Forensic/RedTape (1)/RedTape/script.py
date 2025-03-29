import zipfile

# Function to try opening the zip file with different passwords
def try_zip_password(zip_file, password):
    try:
        with zipfile.ZipFile(zip_file) as zf:
            zf.testzip()  # Check if password works
            print(f"Password found: {password}")
            return True
    except:
        return False

# Password base key from bureaucracy.txt
base_key = 'nCpF4n3Jr1'

# List of potential modifications (based on your clues)
potential_passwords = [
    base_key + '300',          # Try appending '300'
    '300' + base_key,          # Try prepending '300'
    base_key + str(300),       # Try appending '300' as a string
    base_key[::-1] + str(300), # Try reversed base key with '300'
]

# Path to the ZIP file
zip_path = 'redtape.zip'

# Try all possible passwords
for password in potential_passwords:
    if try_zip_password(zip_path, password):
        break
