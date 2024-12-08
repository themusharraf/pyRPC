# gRPC Misol: Ikki sonni qo'shish

Ushbu loyiha gRPC yordamida oddiy server va mijozni yaratish misolini ko'rsatadi. Server `AddNumbers` RPC usulini taqdim etadi, bu esa ikki butun sonni qo'shadi.

---

## **Talablar**

1. Python 3.7 yoki undan yuqori versiya
2. Python kutubxonalarini o'rnating:
```bash
   pip install grpcio grpcio-tools
```
1. Protobuf faylini yaratish

   `add_service.proto` nomli faylni quyidagi mazmun bilan yarating:
```typescript
syntax = "proto3";

service Calculator {
  rpc AddNumbers (AddRequest) returns (AddResponse);
}

message AddRequest {
  int32 num1 = 1;
  int32 num2 = 2;
}

message AddResponse {
  int32 result = 1;
}
```
Bu faylda:
- **Xizmat**: `Calculator` nomli xizmat `AddNumbers` RPC usuliga ega.
- **Xabarlar**: 
  - `AddRequest` (kiritish ma'lumoti) 
  - `AddResponse` (chiqarish ma'lumoti)

2. ### gRPC Python kodini generatsiya qilish.

   Quyidagi buyruqni bajarib, Python kodini generatsiya qiling:
   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. add_service.proto
   ```
Bu buyruq quyidagi fayllarni yaratadi:
   - `add_service_pb2.py`
   - `add_service_pb2_grpc.py`
3. ### gRPC serverni amalga oshirish

    - `server.py` nomli faylni yarating va serverni quyidagicha amalga oshiring:
```python
import grpc
from concurrent import futures
import time

import add_service_pb2
import add_service_pb2_grpc

class CalculatorServicer(add_service_pb2_grpc.CalculatorServicer):
    def AddNumbers(self, request, context):
        result = request.num1 + request.num2
        return add_service_pb2.AddResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_service_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server 50051 portida ishlamoqda...")
    server.start()
    try:
        while True:
            time.sleep(86400)  # Serverni uzluksiz ishlashga qo'yish
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
```
4. ### gRPC mijozni amalga oshirish

    - `client.py` nomli faylni yarating va mijozni quyidagicha amalga oshiring:
```python
import grpc
import add_service_pb2
import add_service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = add_service_pb2_grpc.CalculatorStub(channel)

    response = stub.AddNumbers(add_service_pb2.AddRequest(num1=5, num2=3))
    print(f"Natija: {response.result}")

if __name__ == '__main__':
    run()
```
5. ### Loyihani ishga tushirish

- Serverni ishga tushirish
Serverni birinchi terminalda ishga tushiring:
```python
python server.py
```
Mijozni ishga tushirish
- Mijozni ikkinchi terminalda ishga tushiring:
```python
python client.py
```
Kutilgan natija
- Mijozni ishga tushirgandan so'ng quyidagi natijani ko'rishingiz kerak:
```markdown
Natija: 8
```
Loyiha tuzilmasi

- Quyidagi tuzilma loyihangizda bo'lishi kerak:
```markdown
├── add_service.proto
├── add_service_pb2.py
├── add_service_pb2_grpc.py
├── client.py
└── server.py
```

### Eslatma
`grpcio` va `grpcio-tools` kutubxonalari o'rnatilganligiga ishonch hosil qiling.
Agar Protobuf generatsiyasi bilan bog'liq muammo yuzaga kelsa, terminalda yuqoridagi
buyruqlarni qayta ishlating va virtual muhitni faollashtirganingizni tekshiring.





