from hashlib import md5


def get_hash_from_str(string):
    hasher = md5()
    encoded_string = string.encode('utf-8')
    hasher.update(encoded_string)
    return hasher.hexdigest()
