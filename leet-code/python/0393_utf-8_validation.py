class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        #return self.no_bit_manipulation(data)
        return self.bit_manipulation(data)

    def bit_manipulation(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            b = data[i] & 0xFF
            checked = False

            checks = [(7, 0), (5, 0b110), (4, 0b1110), (3, 0b11110)]
            for qtt, check in enumerate(checks):
                shift, cond = check
                if (b >> shift) == cond and i + qtt < len(data):
                    checked = True
                    for j in range(i + 1, i + qtt + 1):
                        checked = checked and (data[j] >> 6) == 0b10

                    i += qtt + 1
                    break
                    
            if not checked:
                return False
        
        return True   

    def no_bit_manipulation(self, data: List[int]) -> bool:
        sequence = []
        for d in data:
            sequence.append("{0:08b}".format(d))
        
        i = 0
        while i < len(data):
            checks = [('0', 1), ('110', 2), ('1110', 3), ('11110', 4)]
            checked = False
            for check in checks:
                end = i + check[1] - 1
                if sequence[i].startswith(check[0]) and end < len(data):
                    checked = True
                    for j in range(i, end):
                        checked = checked and sequence[j + 1][:2] == '10'
                    
                    if checked:
                        i += check[1]
                        break

            if not checked:
                return False
        
        return True