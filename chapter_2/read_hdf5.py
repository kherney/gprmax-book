import h5py, sys
filename = sys.argv[1]
print(str(filename))
def bold(str_object):
    str_object = str(str_object)
    str_bolded = '\033[1m' + str_object + '\033[0m'
    return str_bolded


with h5py.File(filename, 'r') as f:
    name = str(f.values())
    name = name[name.index('<'):name.index('>')+1]
    print("\nNombre del archivo {}\n\n".format(name))
    attr = f.attrs
    print("\tLista de atributos")
    for i, j in attr.items():
        print("\t\t{}:\t{}".format(bold(i), j))

    # List all groups
    print("\n\tLista de grupos")
    for i, j in f.items():
        print("\t\tGrupo {}".format(bold(i)))
        for i2 , j2 in j.items():
            if len(i2) ==0:
                break
            print("\t\t\t Grupo {}".format(bold(i2)))
            attr_2 = j2.attrs
            for name, value in attr_2.items():
                print("\t\t\t\tAtributo {}:\t{}".format(
                                                        bold(name),
                                                        value))
            for i3, j3 in j2.items():
                if len(i3) == 0:
                    break
                print("\t\t\t\tDataset {} = Tamaño: {}, Tipo de dato: {}".format(
                                                                        bold(i3),
                                                                        j3.shape,
                                                                        j3.dtype))
print("\n\t{}\n".format(bold('END')))