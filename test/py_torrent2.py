from bencode import bdecode
import hashlib

data =open('test2.torrent','rb').read()
torrent = bdecode(data)
print(torrent)