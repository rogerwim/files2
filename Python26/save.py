import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def seal(key, filename):
    chunksize = 64*1024
    outputFile = "(dicht)"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new.read(16)

    encryptor = AES.new(key, AES_MODE_CBC, IV)

    with open(filename, 'rb' as infile
              with open(outputFile, 'wb') as outfile
                    outfile.write(filesize.encode('UTF-8')
                    outfile.write(IV)

                    while True:
                            chunk = infile.read(chunksize
                            if len(chunk) == 0
                                    break


seal()
