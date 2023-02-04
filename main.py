from encryption import Encryption
from decryption import Decryption
from generation_key.creation_key import CreationKeys
import generation_key.utils as utils


def write_key(public_key, private_key):
    utils.write_text_to_file("data/keys/public_key", public_key)
    utils.write_text_to_file("data/keys/private_key", private_key)


def write_encrypted_text(text):
    utils.write_text_to_file("data/output/output1", text)


def get_text():
    return utils.get_text_from_file("data/input/text1")


if __name__ == '__main__':
    public_key, private_key = CreationKeys().get_keys()
    write_key(public_key, private_key)
    en = Encryption(get_text(), public_key)
    de = Decryption(en.encryption_text, private_key)
    write_encrypted_text(en.encryption_text)
    print(f"Initial text: {en.text}")
    print(f"Text to list number: {utils.text_to_list_of_number(en.text)}")
    print(f"Encrypted text: {en.encryption_text}")
    print(f"Decrypted text (digital form): {de.decryption_text}")
    print(f"Decrypted text: {utils.list_of_number_to_text(de.decryption_text)}")

