class Nullifier:
    def nullify(self, policy, weights, participants):
        # ценностно-ориентированное обнуление
        best_love = -float("inf")
        best_policy = None
        best_weights = None
        for candidate_policy in self._generate_policies(participants):
            for candidate_weights in self._generate_weights():
                love = self._evaluate_love(candidate_policy, candidate_weights, participants)
                if love > best_love:
                    best_love = love
                    best_policy = candidate_policy
                    best_weights = candidate_weights
        return best_policy, best_weights

    def _evaluate_love(self, policy, weights, participants):
        # суммарная ценность (love) системы
        return np.sum([w.love for w in weights])  # упрощённо
