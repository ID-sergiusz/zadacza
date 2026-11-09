#!/usr/bin/env python3
"""Niezależne testowanie HAK: uruchom 'python3 test_hak.py ./hak'."""
from collections import deque
from pathlib import Path
import random
import subprocess
import sys


def input_for(target, current):
    def lines(towers):
        return '\n'.join(
            str(len(t)) + ((' ' + ' '.join(map(str, t))) if t else '')
            for t in towers
        )

    return f'{len(target)}\n{lines(target)}\n{lines(current)}\n'


def check_case(binary, target, current):
    source = input_for(target, current)
    result = subprocess.run(
        [str(binary)], input=source, capture_output=True, text=True, check=True
    )
    lines = result.stdout.splitlines()
    if not lines:
        raise AssertionError('Brak danych na wyjsciu')
    m = int(lines[0])
    if m != len(lines) - 1 or not (0 <= m <= 4_000_000):
        raise AssertionError('Bledna liczba ruchow')

    towers = [deque(t) for t in current]
    for i, line in enumerate(lines[1:], 1):
        a, b = map(int, line.split())
        if not (1 <= a <= len(towers) and 1 <= b <= len(towers)):
            raise AssertionError(f'Ruch {i}: niedozwolony numer wiezy')
        if not towers[a - 1]:
            raise AssertionError(f'Ruch {i}: pusta wieza zrodlowa')
        disk = towers[a - 1].popleft()
        towers[b - 1].append(disk)

    if [list(t) for t in towers] != target:
        raise AssertionError('Konfiguracja koncowa nie zgadza sie z celem')
    return m


def random_configuration(rng, n, k):
    disks = list(range(1, n + 1))
    rng.shuffle(disks)
    towers = [[] for _ in range(k)]
    for disk in disks:
        towers[rng.randrange(k)].append(disk)
    return towers


def main():
    if len(sys.argv) != 2:
        print('Uzycie: python3 test_hak.py ./hak')
        return 2
    binary = Path(sys.argv[1]).resolve()
    if not binary.is_file():
        print(f'Nie znaleziono pliku wykonywalnego: {binary}')
        return 2
    rng = random.Random(20261109)
    total = 350
    for i in range(total):
        k = rng.randint(2, 5)
        n = rng.randint(1, 100)
        target = random_configuration(rng, n, k)
        current = random_configuration(rng, n, k)
        check_case(binary, target, current)
    print(f'OK: {total} losowych testow przeszlo pomyslnie')
    return 0


if __name__ == '__main__':
    sys.exit(main())
