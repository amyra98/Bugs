def decimalToBinary(num, k_prec) :  
    # usually k_prec we take 3
    binary = ""
    intpart = int(num)
    fracpart = num - intpart
    while (intpart) :
        rem = intpart % 2
        binary += str(rem);
        intpart //= 2
    binary = binary[ : : -1]
    binary += '.'
    while (k_prec) :
        fracpart *= 2
        fract_bit = int(fracpart)
        if (fract_bit == 1) :
            fracpart -= fract_bit
            binary += '1'   
        else :
            binary += '0'
        k_prec -= 1
    return binary
 

 
