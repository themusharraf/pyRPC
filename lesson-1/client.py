import xmlrpc.client

# Serverga ulanish
server = xmlrpc.client.ServerProxy("http://localhost:8000")

# Serverdagi funksiyani chaqirish
result = server.add_numbers(5, 3)

# Natijani chiqarish
print("Natija:", result)
