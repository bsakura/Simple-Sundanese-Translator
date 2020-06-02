#Extracting Indo.txt
def extIndoSunda():
    dicti = open("../dict/indonesia.txt", "r")
    indonesia = []
    with dicti as filename:
        for line in filename:
            splitted = tuple(line.strip().split(' = '))
            indonesia.append(splitted)
        return indonesia

#Extracting Sunda.txt
def extSundaIndo():
    sunda = []
    with open("../dict/sunda.txt", "r") as filename:
        for line in filename:
            splitted = tuple(line.strip().split(' = '))
            sunda.append(splitted)
        return sunda
