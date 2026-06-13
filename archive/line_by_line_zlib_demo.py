#!/usr/bin/env python3
# line_by_line_zlib_demo.py
# ARCHIVED: Perfectly dumb / pointless experiment.
#
# Attempts per-line zlib "compression" of a hardcoded file.
# - First line written without compression
# - Broken roundtrip in practice for real files
# - No CLI, no real utility (zlib on individual text lines is silly)
# Originally: messy_area/compressDecompressFileLineByLine.py

import zlib

print('---compression---')


originalFile = open('blahblah.txt','r')
compressedFile = open('compressedText.txt','wb')

compressedFile.write(originalFile.readline().encode())


linebreak=b''
for line in originalFile.readlines():
  print(line,zlib.compress(line.encode()))
  compressedFile.write( linebreak + zlib.compress(line.encode()) )
  linebreak=b'\n'
  
originalFile.close()
compressedFile.close()



print('---decompression---')

compressedFile = open('compressedText.txt','rb')
decompressedFile = open('decompressedText.txt','w')

decompressedFile.write(compressedFile.readline().decode())

for line in compressedFile.readlines():
    #print(line,str(zlib.decompress(line)))
    decompressedFile.write(zlib.decompress(line).decode())

compressedFile.close()
decompressedFile.close()
