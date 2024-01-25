# Analizator sekwencji DNA🧬

## Opis

Projekt "Analizator sekwencji DNA" to narzędzie napisane w języku Python, umożliwiające analizę sekwencji DNA z pliku FASTA. Narzędzie korzysta z biblioteki BioPython do efektywnej manipulacji sekwencjami genetycznymi oraz obliczeń związanych z analizą DNA.

## Instrukcje użycia

1. Sklonuj repozytorium lub pobierz pliki źródłowe.
2. Zainstaluj niezbędne zależności, w tym BioPython.

    ```bash
    pip install biopython
    ```

3. Uruchom skrypt `analyze_dna_sequence.py`, dostarczając jako argument ścieżkę do pliku FASTA z interesującą sekwencją DNA.

    ```bash
    python analyze_dna_sequence.py --file_path /ścieżka/do/pliku.fasta
    ```

## Funkcje

- **`analyze_dna_sequence(file_path)`**
  - Wczytuje sekwencję DNA z pliku FASTA.
  - Oblicza zawartość GC w sekwencji.
  - Znajduje i zwraca otwarte ramki odczytu (ORFs) o długości co najmniej 50 aminokwasów.

## Wyniki

- Zawartość GC w sekwencji (w procentach).
- Liczba znalezionych otwartych ramek odczytu (ORFs).
- Poszczególne ORFs wraz z ich numerem porządkowym.

## Przykład użycia

```bash
python analyze_dna_sequence.py --file_path /ścieżka/do/pliku.fasta
