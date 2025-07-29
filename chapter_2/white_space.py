language_stack = "Languages To be Used :\n\t\t\tPython\n\t\t\tJava\n\t\t\tJavascript\n\t\t\tC\n\t\t\tC++"
print(language_stack)

right_space = "py  "
left_space = "  py"
both_side = " py "

print(right_space.rstrip()) #doesn't change the original value
print(right_space)
print(left_space.lstrip())
print(left_space)
print(both_side.strip())

sample_url  = "https://www.youtube.com/watch?v=ZMsTMuyH7w8"
domain = sample_url.removeprefix('https://')
domain = domain.removesuffix('/watch?v=ZMsTMuyH7w8')

print(domain)
