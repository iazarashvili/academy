import hashlib

externalOrderId = ''
orderStatus = ''
expressSigninConfig = 'ec736719a3434060bb74fa34f4009395'


def create_md5(input_str):
    input_bytes = input_str.encode('ascii')

    md5_hash = hashlib.md5()
    md5_hash.update(input_bytes)

    return md5_hash.hexdigest()


input_string = "example_input"
result = create_md5(input_string)
print(result)
