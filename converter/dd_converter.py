def dd_to_ddmm(dd):
    deg = int(dd)
    dec = float(dd) - float(deg)

    ddmm = str(deg) + '° ' + str(dec*60) + '\''
    return ddmm


# Tests:
print(dd_to_ddmm(45.50))
