class Swarm:
    def __init__(self, participants):
        self.participants = participants  # Agent или Human
        self.policy = Policy(self._initial_mapping())
        self.weights = Weights()
        self.dialog_history = []

    def step(self):
        for p in self.participants:
            p.set_policy(self.policy)
        # каждый действует в соответствии с ролью
        actions = [p.act(self.dialog_history) for p in self.participants]
        # диалог
        self.dialog_history.append(actions)
        # обновляем веса
        self.weights = optimize_weights(self.weights, self.policy, self.participants, self.dialog_history)
        # смена политики (свап ролей)
        self.policy = self.policy.swap()
        # проверка обнулёнки
        if self._should_nullify():
            self.nullify()

    def nullify(self):
        nullifier = Nullifier()
        self.policy, self.weights = nullifier.nullify(self.policy, self.weights, self.participants)
