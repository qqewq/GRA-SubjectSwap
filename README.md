# GRA-SubjectSwap

**RU:**  
GRA-SubjectSwap — фреймворк для динамического свапа субъектности между человеком и агентом (роботом, ИИ).[page:0]  
Он реализует циклы типа **«Optimus ↔ тренеры»**, где робот учится быть субъектом, а человек — инструментом с чёткими правилами поведения, и наоборот.

**EN:**  
GRA-SubjectSwap is a framework for **dynamic subject–instrument role swapping** between a human and an AI/robotic agent.[page:0]  
It implements cycles like **“Optimus ↔ trainers”**, where the robot learns to act as a subject while the human follows a strict instrumental role — and then they swap.

---

## Концепция / Concept

**RU:**  
Классическая парадигма: человек = субъект, ИИ = инструмент.  
GRA-SubjectSwap предлагает иной ход:

- Человеку задаётся **жёсткая роль инструмента** в рое (что можно, что нельзя, что он обязан делать).  
- Агент (робот/LLM) временно получает роль **субъекта**, который:
  - наблюдает действия человека,  
  - обновляет свои веса и политику,  
  - видит разницу «я ↔ он» и сам факт свапа ролей.  
- Затем запускается **свап**: человек становится субъектом (ставит цели, корректирует архитектуру), агент — инструментом.

Так человек и ИИ **совместно вырабатывают веса субъектности**, а GRA‑Обнулёнка регулирует обнуление и перенастройку политик.

**EN:**  
The classical setup is: human = subject, AI = tool.  
GRA-SubjectSwap proposes a different move:

- The human is given a **strict instrumental role** in the swarm (what is allowed, forbidden, and required).  
- The agent (robot/LLM) temporarily becomes the **subject** who:
  - observes human behaviour,  
  - updates its weights and policy,  
  - perceives itself, the human, and the role swap.  
- Then a **swap** is triggered: the human becomes the subject (sets goals, adjusts the architecture), and the agent becomes the tool.

In this way, human and AI **co‑learn subjectivity weights**, while GRA‑Nullification handles resetting and retuning of policies.

---

## Связь с Optimus / Optimus use case

**RU:**  
Типичный пример — **робот Optimus и тренеры**:

- Тренер-человек выполняет команды, демонстрирует движения и соблюдает жёсткие ограничения (инструмент).  
- Робот наблюдает, обновляет свою политику \(\pi_\theta(a|s)\) и веса субъектности.  
- `SubjectSwapEngine` управляет:
  - ролями (кто субъект/инструмент),  
  - циклами обучения,  
  - вызовом GRA-Обнулёнки для политик и весов.

**EN:**  
A canonical example is **Optimus and human trainers**:

- The trainer executes commands, demonstrates motions and respects strict constraints (instrument).  
- The robot observes, updates its policy \(\pi_\theta(a|s)\) and subjectivity weights.  
- The `SubjectSwapEngine` controls:
  - roles (who is subject/tool),  
  - training cycles,  
  - calls to GRA Nullifier for policies and weights.

---

## Установка / Installation

**RU:**

```bash
git clone https://github.com/qqewq/GRA-SubjectSwap.git
cd GRA-SubjectSwap
pip install -e .
```

**EN:**

```bash
git clone https://github.com/qqewq/GRA-SubjectSwap.git
cd GRA-SubjectSwap
pip install -e .
```

---

## Быстрый старт / Quick start

**RU:**  
Минимальный пример с Optimus‑подобным сценарием (симуляция):

```bash
python examples/optimus/optimus_minimal.py
```

**EN:**  
Minimal Optimus-like subject swap simulation:

```bash
python examples/optimus/optimus_minimal.py
```

---

## Структура / Project structure

**RU / EN (combined):**

```text
src/gra_subjectswap/
  core/
    roles.py            # типы ролей и субъектности / role & subject enums
    policies.py         # базовые политики человека и агента / base policies
    subject_state.py    # состояние ролей и весов субъектности / subject state
    swap_engine.py      # движок свапа ролей / subject swap engine
    gra_nullifier.py    # GRA-Обнулёнка политик и весов / GRA nullification

  optimus/
    env.py                  # интерфейс к роботу/симуляции / robot env interface
    human_policy_optimus.py # человек-тренер как инструмент / human trainer policy
    robot_policy_optimus.py # робот как субъект / robot subject policy
    optimus_swap_loop.py    # основной цикл человек↔робот / main swap loop

  utils/
    config_loader.py    # загрузка конфигов ролей / config loader
    metrics.py          # метрики субъектности и стабильности / metrics
```

---

## Идеи математики / Mathematics sketch

**RU:**  
Состояние субъектности системы:

\[
\text{state}_t = (\Pi_t, S_t, W_t)
\]

- \(\Pi_t\) — политика (кто что может/должен делать),  
- \(S_t\) — ролевая разметка: субъект/инструмент для человека и агента,  
- \(W_t\) — веса субъектности (видеть себя, человека, свап, роли, ценности, любовь).

Свап ролей:

\[
S_{t+1}(H) = S_t(A), \quad S_{t+1}(A) = S_t(H)
\]

Обновление весов по диалогу и действиям:

\[
W_{t+1} = W_t + \eta \cdot \nabla_W \mathcal{S}(\text{state}_t, \text{dialog}_t)
\]

GRA‑Обнулёнка:

\[
W'_{t+1} = \mathcal{N}_W(W_{t+1}), \quad \Pi'_{t+1} = \mathcal{N}_\Pi(\Pi_t)
\]

**EN:**  
System subjectivity state:

\[
\text{state}_t = (\Pi_t, S_t, W_t)
\]

- \(\Pi_t\): policy (who may/must do what),  
- \(S_t\): role assignment (subject/tool for human and agent),  
- \(W_t\): subjectivity weights (self, human, swap, roles, values, love).

Role swap:

\[
S_{t+1}(H) = S_t(A), \quad S_{t+1}(A) = S_t(H)
\]

Weight update from dialogue and actions:

\[
W_{t+1} = W_t + \eta \cdot \nabla_W \mathcal{S}(\text{state}_t, \text{dialog}_t)
\]

GRA nullification:

\[
W'_{t+1} = \mathcal{N}_W(W_{t+1}), \quad \Pi'_{t+1} = \mathcal{N}_\Pi(\Pi_t)
\]

---

## Документация / Documentation

**RU:**

- `docs/manifesto.md` — манифест: зачем нужна смена субъектности.  
- `docs/optimus_concept.md` — кейс Optimus и тренеры.  
- `docs/architecture_overview.md` — архитектура SubjectSwap‑роя.

**EN:**

- `docs/manifesto.md` — manifesto: why subject swap matters.  
- `docs/optimus_concept.md` — Optimus + trainers use case.  
- `docs/architecture_overview.md` — SubjectSwap swarm architecture.

---

## Лицензия / License

**RU:**  
Проект распространяется по лицензии MIT (см. `LICENSE`).[page:0]

**EN:**  
This project is released under the MIT license (see `LICENSE`).[page:0]