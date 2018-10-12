class Card():
    def __init__(self, cardID, password, money, lock=False):
        self.cardID = cardID
        self.password = password
        self.money = money
        # 当值为False，代表未锁定。
        self.lock = lock