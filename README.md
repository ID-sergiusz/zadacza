# HAK — Hanoj kontratakuje

**Bezpłatny kurs algorytmiki od podstaw, w języku polskim**, oparty na zadaniu HAK z XXXIV Olimpiady Informatycznej (etap I, 2026).

Materiały są dostępne jako osobne pliki, bez konieczności pobierania i rozpakowywania archiwum ZIP.

## Materiały

- 📘 [Podręcznik PDF (22 strony)](docs/HAK_kurs_algorytmow_od_podstaw_PL.pdf) — lekcje od podstaw algebry do pełnego rozwiązania.
- 📖 [Podręcznik Markdown](docs/HAK_podrecznik_PL.md) — można czytać bezpośrednio na GitHubie.
- 💻 [Rozwiązanie C++17](src/hak.cpp) — pełny kod zadania.
- 🧪 [Testy automatyczne](tests/test_hak.py) — 350 losowych przypadków i symulator ruchów.
- 📥 [Przykładowe wejście](examples/przyklad_wejscie.txt) i [przykładowe wyjście](examples/przyklad_wyjscie.txt) — 27 ruchów.

## Uruchomienie na Linux / macOS

W katalogu głównym repozytorium:

```bash
g++ -std=c++17 -O2 -Wall -Wextra src/hak.cpp -o hak
./hak < examples/przyklad_wejscie.txt > wynik.txt
python3 tests/test_hak.py ./hak
```

Porównanie przykładu:

```bash
diff -u examples/przyklad_wyjscie.txt wynik.txt
```

## Proponowana kolejność nauki

1. Podstawy matematyki: zmienne, potęgi, system binarny.
2. Tablice, pętle, kolejki FIFO.
3. Stabilny podział i sortowanie Radix Sort.
4. Dowód poprawności i złożoność algorytmu.
5. Pełny program C++17 oraz testowanie.

**Uwaga:** Jest to niezależne opracowanie edukacyjne, a nie oficjalne rozwiązanie organizatorów OI.
