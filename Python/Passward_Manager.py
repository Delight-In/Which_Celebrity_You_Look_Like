import json
import os
from cryptography.fernet import Fernet
from getpass import getpass

class SecurePasswordManager:
    def __init__(self, storage_file='passwords.json', key_file='secret.key'):
        self.storage_file = storage_file
        self.key_file = key_file
        self.key = self.load_or_generate_key()
        self.cipher_suite = Fernet(self.key)
        self.password_data = self.load_password_data()

    def load_or_generate_key(self):
        """Load the encryption key from a file, or generate one if it doesn't exist."""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key

    def load_password_data(self):
        """Load password data from the storage file (if it exists)."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_password_data(self):
        """Save the encrypted password data to the storage file."""
        with open(self.storage_file, 'w') as f:
            json.dump(self.password_data, f, indent=4)

    def encrypt_password(self, password):
        """Encrypt a password using the Fernet encryption system."""
        return self.cipher_suite.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        """Decrypt an encrypted password."""
        return self.cipher_suite.decrypt(encrypted_password.encode()).decode()

    def add_password(self, service_name, password):
        """Add a new service password to the storage."""
        encrypted_password = self.encrypt_password(password)
        self.password_data[service_name] = encrypted_password
        self.save_password_data()
        print(f"Password for {service_name} has been stored securely.")

    def get_password(self, service_name):
        """Retrieve and decrypt the password for a service."""
        if service_name in self.password_data:
            encrypted_password = self.password_data[service_name]
            return self.decrypt_password(encrypted_password)
        else:
            return f"No password found for {service_name}."

    def list_services(self):
        """List all services stored in the password manager."""
        if self.password_data:
            print("Stored services:")
            for service in self.password_data:
                print(service)
        else:
            print("No services stored.")

    def delete_password(self, service_name):
        """Delete the password entry for a given service."""
        if service_name in self.password_data:
            del self.password_data[service_name]
            self.save_password_data()
            print(f"Password for {service_name} has been deleted.")
        else:
            print(f"No password found for {service_name}.")

    def change_password(self, service_name):
        """Change the password for an existing service."""
        if service_name in self.password_data:
            new_password = getpass(f"Enter new password for {service_name}: ")
            self.add_password(service_name, new_password)
            print(f"Password for {service_name} has been updated.")
        else:
            print(f"No password found for {service_name}.")

def main():
    manager = SecurePasswordManager()

    while True:
        print("\nSecure Password Manager")
        print("1. Add a new password")
        print("2. Get a password")
        print("3. List all services")
        print("4. Delete a password")
        print("5. Change a password")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            service_name = input("Enter the service name: ")
            password = getpass("Enter the password: ")
            manager.add_password(service_name, password)
        elif choice == '2':
            service_name = input("Enter the service name: ")
            print(f"Password for {service_name}: {manager.get_password(service_name)}")
        elif choice == '3':
            manager.list_services()
        elif choice == '4':
            service_name = input("Enter the service name to delete: ")
            manager.delete_password(service_name)
        elif choice == '5':
            service_name = input("Enter the service name to change the password: ")
            manager.change_password(service_name)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
