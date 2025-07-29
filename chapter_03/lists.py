names = ["white haired Alex" , "Laal Bal wala Lukky" , "Jodur bro Kodu" , "Michael Modhu Sudon"]

print(f"Wassup {names[0]}")
print(f'kya haal chaal {names[1]}')
print(f'Yoo {names[2]}')
print(f'Kimon asen {names[3]}')

transports = [
  'I like train journey . Alllloottt !!!',
  "Bus journey is also great if it's on mountain side "
]

print(transports[0])
print(transports[1])

transports.append("Boat journey is also great (specially if it's in your hometown river)")

print(transports)

print(transports.pop())

print(transports)

names.sort()

print(names)

names.sort(reverse=True)

print(names)

print(sorted(transports))

print(transports) #doesn't manipulates the main array