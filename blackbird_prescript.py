import os
import base64
import hashlib
import datetime

USERNAME = 'WS1FSFCT'
url = 'https://nodeD1.production.webservices.amadeus.com/1ASIWFCT1FS'

with open('api_password.txt', 'r') as f:
    apiPassword = f.read().strip()

def generateNonce():
    nonce = os.urandom(8)
    return base64.b64encode(nonce).decode('utf-8')

def generateAmadeusSOAPPassword():
    nonce = generateNonce()
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    passwordBytes = base64.b64decode(nonce) + timestamp.encode('utf-8') + hashlib.sha1(apiPassword.encode('utf-8')).digest()
    passwordHash = hashlib.sha1(passwordBytes).digest()
    secret = base64.b64encode(passwordHash).decode('utf-8')
    return secret, nonce, timestamp
