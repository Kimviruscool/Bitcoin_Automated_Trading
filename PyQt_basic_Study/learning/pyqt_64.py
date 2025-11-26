# 코루틴2 #p.339

import asyncio

async def make_americano():
    print('Americano Start')
    await asyncio.sleep(3)
    print('Americano End')

async def make_latte():
    print('Latte Start')
    await asyncio.sleep(5)
    print('Latte End')

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    result = await asyncio.gather(coro1, coro2)
    print(result)

print("Main Start")
asyncio.run(main())
print("Main End")

# 결과
# Main Start
# Americano Start #start 동시시작
# Latte Start
# Americano End #3초후 아메리카노 종료
# Latte End #5초후 라떼 종료
# Main End #이벤트 종료후 메인 종료