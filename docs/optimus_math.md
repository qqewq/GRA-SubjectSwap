# Формализм Optimus SubjectSwap

## Переменные
- \( \theta \) – параметры политики робота.
- \( W = (w_{self}, w_{human}, w_{swap}, w_{role}, w_{value}, w_{love}) \) – веса субъектности.
- \( S_t \) – оператор свапа в момент \( t \).

## Шаг обучения
При фазе «Optimus‑субъект»:
\[
\theta \leftarrow \theta + \alpha \nabla_\theta \mathcal{L}_{IL}(demo, \pi_\theta(s))
\]
где демонстрации даёт человек-инструмент.

При свапе:
\[
W_{t+1} = \mathcal{N}(W_t, h_t, a^H_t, a^A_t)
\]
где \( \mathcal{N} \) – GRA-обнулёнка.

## Обнуление
\[
\mathcal{N}(W) = \arg\max_{W' \in \mathcal{C}(W)} \sum_j L_j(W'_j)
\]
при ограничениях ценности.
