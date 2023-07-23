'''Echoサーバの実装'''
import asyncio
import websockets
import json
from suggest_func import dec_stretch
import time



concerns = [0, 0, 0, 0, 1]
work_time = 1
break_time = 1
set_count = 1
start = False
suggested_list=[[0,0,0,0],[0,0],[0,0,0],[0,0,0],[0,0]]
suggest = [0,0]
count = 0
fin = False


# この関数に通信しているときに行う処理を書く。
# クライアントが接続している間は下の関数が常に回っている
async def handler(websocket):
    global concerns, worktime, breaktime, setcount, start
    # クライアントからのメッセージを取り出してそのまま送り返す（Echo）
    async for message in websocket:
        print(message)
        print(json.loads(message))
        data = json.loads(message)
        option = data['option']
        if option == 'setting':
            concerns = data['concerns']
            work_time = data['work_time']
            break_time = data['break_time']
            set_count = data['set_count']
            start = True
        elif option == 'stretch':
            print("stretch")
            await websocket.send("/neko.mov")
        
        # print(type(data['break_time']))
        # print(type(data['set_count']))
        print(concerns)

async def other_task():
    global suggested_list, suggest, count, start, fin
    # ここに別の非同期処理を記述する
    while True:
        print("別の処理を実行中...")
        if start:
            #姿勢の評価を集計、一番多かった結果を最終結果とし変数workに格納
            if not fin:
                start_time = time.time()
                while(time.time() - start_time < 1):
                    None
                
                None
                work = 2
            fin = True
            print("aaa")
            if fin:
                #print(suggested_list)
                #suggest = dec_stretch(concerns,work,suggested_list)
                #print(suggest)
                #if sum(concerns) > break_time: #ストレッチが必要な部位が休憩回数よりも多い時
                #    suggested_list[suggest[0]] = [1]*len(suggest[0])#その部位は選ばれない
                #else:
                #    suggested_list[suggest[0]][suggest[1]] = 1 #そのストレッチは選ばれない

                #提案するストレッチの情報をアプリ側に渡す
                None
                print(2)

                count += 1
                if count >= break_time:
                    start = False
                await asyncio.sleep(3)

        await asyncio.sleep(1)

# async def main():
#     async with websockets.serve(handler, "localhost", 8001):
#         await asyncio.Future()  # run forever

# asyncio.run(main())
async def main():
    # WebSocket サーバーを起動して接続を待ち受ける
    server = await websockets.serve(handler, "localhost", 8001)

    # 別の非同期処理を開始する
    asyncio.create_task(other_task())

    # サーバーが終了するまで待機する
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
