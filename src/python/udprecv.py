from socket import *
import struct
import csv


# UDP受信クラス

class udprecv:
    def __init__(self):

        SrcIP = "10.229.40.198"  # 受信元IP
        #SrcIP = "172.20.10.3"
        SrcPort = 5002  # 受信元ポート番号
        self.SrcAddr = (SrcIP, SrcPort)  # アドレスをtupleに格納

        self.BUFSIZE = 2048  # バッファサイズ指定

        self.udpServSock = socket(AF_INET, SOCK_DGRAM)  # ソケット作成
        self.udpServSock.bind(self.SrcAddr)  # 受信元アドレスでバインド

    def recv(self):
        count = 1
        with open('posture1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            while True:  # 常に受信待ち

                data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
                # print(type(data))
                # print(len(data))
                target = b'bnid'
                dataArray = data.split(target)
                # print(dataArray)
                # print(4)
                print(len(data))
                if len(data) == 1591:
                    # print(5)
                    pose = [2]  # ラベル0:良い姿勢、 1:猫背 2:腰に悪い姿勢
                    for index, item in enumerate(dataArray):
                        # 1個目の配列は基本情報でtranが入ってないので除外
                        if index != 0:
                            # ボーンのidを確認
                            id = int.from_bytes(item[0:1], 'little')
                            # print('id:' + str(id))
                            # print(1)
                            # tran以下のデータとそれ以前を分解
                            key = b'tran'
                            trans = item.split(key)

                            for index2, item2 in enumerate(trans):
                                # print('index:' + str(index2))
                                if index2 != 0:
                                    # バイナリ書き出し
                                    # print(item2)
                                    # print(2)
                                    # 28バイトぶん切り取り
                                    dat = item2[0:4 * 7]
                                    # 4byteのFloat7個としてデコード
                                    vals = struct.unpack('<fffffff', dat)

                                    # print('tran:' + str(vals))
                                    # print(3)
                                    for i in range(7):
                                        pose.append(vals[i])
                                        # print(pose)

                                    # 結果を書き込み
                                    # op('table2')[0, index] = vals[0]
                                    # op('table2')[1, index] = vals[1]
                                    # op('table2')[2, index] = vals[2]
                                    # op('table2')[3, index] = vals[3]
                                    # op('table2')[4, index] = vals[4]
                                    # op('table2')[5, index] = vals[5]
                                    # op('table2')[6, index] = vals[6]
                                    # print(vals)
                    # csvに書き込み
                    writer.writerow(pose)
                    count += 1
                    # print(count)
                    if count > 1:
                        break
                        # 受信
                # print(data, addr)                  # 受信データと送信アドレス表示



