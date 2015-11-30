pythonMuzyka - beatbox
======================

Repozytorium `pythonMuzyka` zawiera następujące pliki i foldery:
  * `beatbox.py` - główna aplikacja; skrypt tworzący piosenkę, która została podana jako argument,
  * `create_song.py` - moduł z funkcją `create_song` do tworzenia piosenki ze ścieżek,
  * `create_track.py` - moduł z funkcją `create_track` do tworzenia ścieżki,
  * `sample_song` - folder z piosenką stworzoną z sampli,
  * `db_gt_main_opening` - folder z piosenką z głównym motywem openingu anime Dragonball GT,
  * `last_christmas` - folder z piosenką "Last Christmas",
  * `songs` - folder z wygenerowanymi piosenkami.

Ponadto każdy z folderów z piosenkami składa się z:
  * `defs.txt` - plik tekstowy ze słownikiem opisującym konfigurację utworu - zawiera tylko argument `bpm`,
  * `song.txt` - plik tekstowy określający kolejność odgrywanych ścieżek,
  * `trackAB.txt` - pliki tekstowe określające kolejność odgrywania sampli, nutek i instrumentów, gdzie AB to 2 cyfry; jeden wiersz jest odtwarzany na raz. Przykłady zapisu:
     * `01` - odwołanie do sampla `01`,
     * `A-4` - odwołanie do nutki o częstotliwości `A-4`,
  * `sampleXY.wav` - pliki dźwiękowe, gdzie XY to 2 cyfry,


Działanie programu
------------------
   
Program uruchamia się z folderu z programem (katalog bieżący) przy użyciu komendy:

```
./beatbox.py utworX
```

gdzie `utworX` to nazwa katalogu z piosenką lub nazwa pliku w formacie `*.zip`.
Piosenka zostanie utworzona w katalogu bierzącym. 