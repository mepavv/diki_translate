# diki_translate
Moduł Python'a pozwalający na tłumaczenie z polskiego słownika [diki.pl](https://diki.pl).

## Instalacja
```
pip install diki_translate
```

## Opis funkcji

Moduł zawiera klasę `Diki` z funkcją `diki.translation(word, exact_word = 1)`

`word`, akceptuje string, który masz zamiar przetłumaczyć.\
`exact_word`, opcjonalny argument akceptujący int (domyślnie 1), określający czy funkcja ma zwrócić dokładne tłumaczenie słowa, np. czy dla słowa 'used' mają zostać wyświetlone tłumaczenia słowa 'use'.


## Przykłady użycia
Wszystkie operacje są zaimplementowane w klasie `Diki`.     
Wymaga ona podania języka, na który masz zamiar tłumaczyć.

```python
from diki_translate import Diki

diki = Diki("english")
```
Wszystkie dozwolone języki to:
"english", "german", "spanish", "italian", "french".


* Przykłady tłumaczenia:


```python
>>> list(diki.translation('used'))
['używany', 'przyzwyczajony', 'przywykły']
```

```python
>>> list(diki.translation('used', 0))
['używany', 'przyzwyczajony', 'przywykły', 'używać', 'korzystać (np. z telefonu, toalety)', 'zużywać', 'wykorzystywać (np. kogoś do swoich celów)',...]
```
\
Funkcja zwraca iterator by nie żądać więcej wyników niż trzeba.


