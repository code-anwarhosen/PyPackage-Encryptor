import os
from cryptography.fernet import Fernet

class ENCRYPTOR:
    def __init__(self):
        #manual prefix and suffix to detect encryption
        self.ENCRYPTION_PREFIX = b"aReY-oUki-DDin-GmEi-AmtH-eBosS-@hErE-and@-ThEr-E"
        self.ENCRYPTION_SUFFIX = b"gEtt-HEf*-*KouT-oFhE-rE_yoUw-iLLn-Otgo-Nnag-EtRi-doFit"

    #generate and return a fernet key
    def generate_key(self, file_path=None) ->str:
        """
        it will just generate a cryptography token key
        and store to the given file file_path
        """

        try:
            key = Fernet.generate_key()
            if file_path:
                if os.path.isfile(file_path) and os.path.exists(file_path):
                    with open(file_path, 'wb') as file:
                        file.write(key)
                    file.close()
                    return True
            else:
                return key
        except Exception as e:
            return False

    def KeyLike(self):
        return b'iDVdwyFn55LCa6JQNJjIjxFdttmGqOIqf7Xrhk3IdOIencryptor'
        
    def read_key(self, key_or_key_file_path=None):
        """
        if its get key_or_key_file_path as txt file path
        than it will read the file and return the key content
        else it just return the key_or_key_file_path key
        """
        try:
            if key_or_key_file_path:
                if os.path.isfile(key_or_key_file_path) and os.path.exists(key_or_key_file_path):
                    with open(key_or_key_file_path, 'rb') as key_file:
                        key = key_file.read()
                    key_file.close()
                    return key
                else:
                    return key_or_key_file_path

            return False
        except Exception as e:
            return False
    
    # check if file is already encrypted
    def is_encrypted(self, txtfile_or_text=None):
        """
        if given parameter is txt file or normal string
        than it will check if the text endswith('==') if true
        then it will return true if false eill return None
        if any error will return False
        Note: just check if given text encrypted with cryptography 
        and suffix prefix given by me
        """
        try:
            if txtfile_or_text:
                if os.path.isfile(txtfile_or_text) and os.path.exists(txtfile_or_text):
                    with open(txtfile_or_text, 'rb') as file:
                        data = file.read()

                    if data.startswith(self.ENCRYPTION_PREFIX) and data.endswith(self.ENCRYPTION_SUFFIX):
                        return True
                    else:
                        return False
                else:
                    if type(txtfile_or_text) != bytes:
                        data = str(txtfile_or_text).encode()
                    else:
                        data = txtfile_or_text
                        
                    if data.startswith(self.ENCRYPTION_PREFIX) and data.endswith(self.ENCRYPTION_SUFFIX):
                        return True
                    return False
            return False
        except Exception as e:
            return False

    def encrypt(self, key_or_key_file_path=None, txtfile_or_text=None):
        """
        take key_or_key_file_path as key file path or
        actual token key and take a file path of the file
        to be encrypted and than it will be encrypted and 
        store the encrypted data to the same file path
        """
        try:
            if not key_or_key_file_path:
                return False
            key = self.read_key(key_or_key_file_path)

            fernet = Fernet(key)
            if txtfile_or_text:
                if os.path.isfile(txtfile_or_text) and os.path.exists(txtfile_or_text):
                    with open(txtfile_or_text, 'rb') as file:
                        data = file.read()
                    file.close()
                    
                    encrypted_data = fernet.encrypt(data)
                    final_encrypted = self.ENCRYPTION_PREFIX + encrypted_data + self.ENCRYPTION_SUFFIX

                    with open(txtfile_or_text, 'wb') as encrypted_file:
                        encrypted_file.write(final_encrypted)
                    encrypted_file.close()
                    return True
                else:
                    if type(txtfile_or_text) != bytes:
                            data = str(txtfile_or_text).encode()
                    else:
                        data = txtfile_or_text
                    encrypted_data = fernet.encrypt(data)
                    final_encrypted = self.ENCRYPTION_PREFIX + encrypted_data + self.ENCRYPTION_SUFFIX
                    return final_encrypted
            return False
        except Exception as e:
            return False

    def decrypt(self, key_or_key_file_path=None, txtfile_or_text=None):
        """
        take key_or_key_file_path as key file path or
        actual token key and take a file path of the file
        to be decrypted and than it will be decrypted and 
        store the decrypted data to the same file path
        """
        try:
            if not key_or_key_file_path:
                return False

            key = self.read_key(key_or_key_file_path)
            fernet = Fernet(key)

            if txtfile_or_text:
                if os.path.isfile(txtfile_or_text) and os.path.exists(txtfile_or_text):
                    with open(txtfile_or_text, 'rb') as file:
                        data = file.read()
                    
                    cut_prefix = data.split(self.ENCRYPTION_PREFIX)[1]
                    cut_suffix = cut_prefix.split(self.ENCRYPTION_SUFFIX)[0]
                    decrypted_data = fernet.decrypt(cut_suffix)

                    with open(txtfile_or_text, 'wb') as decrypted_file:
                        decrypted_file.write(decrypted_data)
                    decrypted_file.close()
                    return True
                else:
                    if type(txtfile_or_text) != bytes:
                        data = str(txtfile_or_text).encode()
                    else:
                        data = txtfile_or_text

                    cut_prefix = data.split(self.ENCRYPTION_PREFIX)[1]
                    cut_suffix = cut_prefix.split(self.ENCRYPTION_SUFFIX)[0]
                    decrypted_data = fernet.decrypt(cut_suffix)
                    return decrypted_data.decode()
        except Exception as e:
            return False

Encryptor = ENCRYPTOR()