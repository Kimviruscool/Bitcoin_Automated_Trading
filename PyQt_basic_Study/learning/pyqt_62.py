#웹소켓을 이용한 실시간 시세처리

#asyncio 동기 호출과 비동기 호출 방식

#동기 호출 : 순차적 호출 요청에 대해 완전히 끝낸 후 다음 요청 처리
def sync_fun1():
    print("Hi")

def sync_fun2():
    print("Bye")

sync_fun1()
sync_fun2()