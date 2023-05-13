cypher_option = {"SHA": "SHA selected", "MD5": "MD5 Selected", "MD2": "MD2 Selected"}
print(f"Please choose a cypher option  {cypher_option.keys()}")
chypher_option = input()
print(cypher_option.get(chypher_option, "Your option is invalid."))