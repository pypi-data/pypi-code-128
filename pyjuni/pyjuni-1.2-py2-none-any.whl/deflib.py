
JDCODE = 1
JCBOARD = 2
UGLYBOT = 3
JDMISSION = 4
JDCODE_CMD = 5

FRONT = 0
BACK = 1
RIGHT = 2
LEFT = 3


class DefLib:

    @classmethod
    def checksum(self, packet):
        len = packet[4]
        sum = 0
        for n in range(6, len):
            sum += packet[n]
        return sum & 0xFF


    @classmethod
    def _print(self, data):
        for n in range(0, len(data)):
            h = hex(data[n])
            print(h, end=" ")
        print("")


    @classmethod
    def constrain(self, val , max, min):
        if val > max:
            val = max
        if val < min:
            val = min
        return val


    @classmethod
    def comp(self, data):
        data = data&0xFF
        if data < 0:
            return 256 + data
        else:
            return data

    @classmethod
    def toSigned8(self, n):
        n = n & 0xff
        return (n ^ 0x80) - 0x80

    @classmethod
    def toSigned16(self, n):
        n = n & 0xffff
        return (n ^ 0x8000) - 0x8000