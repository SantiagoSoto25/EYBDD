romano = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000}

numero = 'mmmdclxxvii'

def conv_romano_to_dec(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    else:
        if romano[numero_romano[0]] >= romano[numero_romano[1]]:
            return romano[numero_romano[0]] + conv_romano_to_dec(numero_romano[1:])
        else:
            return romano[numero_romano[0]] + conv_romano_to_dec(numero_romano[1:])
print(conv_romano_to_dec(numero))