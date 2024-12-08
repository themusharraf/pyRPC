import grpc
from concurrent import futures
import time

# Protobuf faylidan generatsiya qilingan kodni import qilish
import add_service_pb2
import add_service_pb2_grpc

# RPC funksiyasi
class CalculatorServicer(add_service_pb2_grpc.CalculatorServicer):
    def AddNumbers(self, request, context):
        result = request.num1 + request.num2
        return add_service_pb2.AddResponse(result=result)

# Serverni ishga tushirish
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_service_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server ishga tushdi... port 50051")
    server.start()
    try:
        while True:
            time.sleep(86400)  # Serverni doimiy ishda saqlash
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
