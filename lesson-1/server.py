from xmlrpc.server import SimpleXMLRPCServer

# Masofaviy chaqiriladigan funksiya
def add_numbers(a, b):
    return a + b

# Server yaratish, lokal portda 8000 orqali ishlash
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add_numbers, "add_numbers")  # Funksiyani serverga ro'yxatdan o'tkazish

print("Server ishga tushdi...")

# Serverni ishga tushirish va kelgan so'rovlarni kutish
server.serve_forever()
