a = input ("Digite algo:")
print (f"O tipo primitivo desse valor é {type(a)}")
print (f"Só tem espaços? {a.isspace()}")
print (f"É um número? {a.isnumeric()}") 
print (f"É alfabético? {a.isalpha()}")
print (f"É alfanúmerico? {a.isalnum()}")
print (f"Ésta em maiúscolas? {a.isupper()}")
print (f"Está em minúsculas? {a.islower()}")
print (f"Está capitalizada? {a.istitle()}")
