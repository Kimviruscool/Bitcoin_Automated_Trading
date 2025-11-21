# 코루틴

import asyncio

async def async_fun1():
    print('sync_fun1')

# async_fun1()
#호출 방법
# asyncio.run(async_fun1())

# 이벤트 루프 설정
loop = asyncio.get_event_loop() #이벤트 루프를 호출
loop.run_until_complete(async_fun1()) #코루틴 객체가 완료될 때까지 실행
loop.close() #이벤트 루프를 닫기

