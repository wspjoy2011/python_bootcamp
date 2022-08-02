import hashlib


def convert_string_to_hash(data: str) -> str:

    if not isinstance(data, str):
        raise TypeError('Data must be string.')

    if not data:
        raise ValueError('Data can\'t be empty.')

    hash_object = hashlib.sha512(data.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


if __name__ == '__main__':
    s_data: str = 'Python Bootcamp'
    result = convert_string_to_hash(s_data)
    print(result)
