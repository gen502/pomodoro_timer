from udprecv import udprecv
from classf import PostureClassifier

udp = udprecv()  # クラス呼び出し
udp.recv()  # 関数実行

classifier = PostureClassifier()
classifier.train('posture.csv')
predictions = classifier.predict('posture1.csv')
with open('posture1.csv', 'w') as file:
    pass
print(predictions)
