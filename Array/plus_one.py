def plusOne(digits):
        if digits[len(digits) - 1] == 9:
            temp_string = ""
            for i in digits:
                    temp_string += str(i)
            num = int(temp_string) + 1
            digits = []
            for i in range(len(str(num))):
                    digits.append(int(str(num)[i]))
            return digits
        else:
            digits[len(digits) - 1] += 1
            return digits
        
print(plusOne([9, 9, 9]))

#[1, 9, 0]