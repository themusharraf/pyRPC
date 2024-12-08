import grpc

# Protobuf faylidan generatsiya qilingan kodni import qilish
import add_service_pb2
import add_service_pb2_grpc

# Serverga ulanish
def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = add_service_pb2_grpc.CalculatorStub(channel)

    # AddNumbers RPC chaqiruvi
    response = stub.AddNumbers(add_service_pb2.AddRequest(num1=5, num2=3))
    print(f"Natija: {response.result}")

if __name__ == '__main__':
    run()
