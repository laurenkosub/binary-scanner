import sys
filein = bytearray(open(sys.argv[1], 'rb').read())
size = len(filein);
xor_byte_array = bytearray(size)
for i in range(size):
    xor_byte_array[i] = filein[i] ^ 0x53
open(sys.argv[2], 'wb').write(xor_byte_array)