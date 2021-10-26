import base64

def encode(password):
    message_bytes = password.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    output = base64_bytes.decode('ascii')
    return output

def decode(password):
    base64_bytes = password.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    output = message_bytes.decode('ascii')
    return output

