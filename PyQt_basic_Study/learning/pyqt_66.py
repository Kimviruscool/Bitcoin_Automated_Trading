# 웹소켓
import websockets
import asyncio
import json

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws" #빗썸 거래소의 웹소켓 서버 주소

    async with websockets.connect(uri) as websocket: #빗썸 웹소켓 서버에 연결
        greeting = await websocket.recv() #서버로부터 데이터 호출
        print(greeting) #서버로부터 받은 데이터 출력 확인

        subscribe_fmt = {"type":"ticker","symbol":["BTC_KRW"],"tickTypes":["1H"]} #구독 요청 형식을 파이썬 딕셔너리로 표현
        # type : ticekr(현재가), 체결내역(transaction), 호가(orderbookdepth)
        # symbol : 구독할 코인의 티커지정
        # tickTypes : 데이터 기준점 설정 (30M, 1H, 12H, 24H, MID 가능)

        subscribe_data = json.dumps(subscribe_fmt) #json 타입으로 변환
        await websocket.send(subscribe_data) #구독요청을 서버에 전송

        # 반복적으로 데이터받기
        while True :
            data = await websocket.recv() #빗썸데이터 받아오기
            data = json.loads(data) #전달받은 json타입 딕셔너리타입으로 변환
            print(data) #화면출력

async def main():
    await bithumb_ws_client()

asyncio.run(main())
