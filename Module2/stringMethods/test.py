
# nam = "kannan"
# response = "good Morning {1}, Today you got {0} as a prize money."
# response = "good Morning {}, Today you got {} as a prize money."
response = "good Morning {name}, Today you got {prize} as a prize money."

response = response.format(name="prathab",prize= "100K")
# response = response.encode()
# response = response.decode()


# if response.endswith("."):
#     print("Puntuation is correct")
# else:
#     print("Not correctly puntuated")

# print(response.find("Today"))
# print(response.index("Today"))
# response = "   100   "

# response = response.strip()
# response = response.lstrip()
# response = response.rstrip()

# print(response+"O")

print(response.replace("prathab", "varun"))