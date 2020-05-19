class Return(object):
    def __init__(self, status='off'):
        self.status = status
        self.experience = 0

    def fit(self):
        if self.status == 'off':
            self.status = 'on'
            self.experience += 100

    def exit_game(self):
        self.status = 'off'
        return self


gamer_01 = Return()
gamer_01.fit()
print(
    gamer_01.status,
    gamer_01.experience
)
gamer_01 = gamer_01.exit_game()
print(
    gamer_01.status,
    gamer_01.experience
)