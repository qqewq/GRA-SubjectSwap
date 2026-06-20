"""Пример с симуляцией (запускает цикл Optimus)."""
import sys
sys.path.insert(0, "src")

from gra_subjectswap.optimus.optimus_swap_loop import run_optimus_subjectswap

if __name__ == "__main__":
    records = run_optimus_subjectswap()
    print(f"Записано шагов: {len(records)}")
