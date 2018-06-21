
"This is a string."
'This is also a string.'

'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

# title() makes each word's first letter capital, other letters small
name = "ada lovelace"
print(name.title())
name = "ADa LOVElacE"
print(name.title())

print(name.upper())
print(name.lower())

# use + combine string
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

favorite_language = ' python \n\t'
# rstrip(), remove tail blank (space, \n, \t)
print(favorite_language.rstrip())
# lstrip(), remove head blank (space, \n, \t)
print(favorite_language.lstrip())
# strip(), remove head and tail blank (space, \n, \t)
print(favorite_language.strip())
