# Opis zadań ***astmatyk*** oraz ***koleje***

## Wstęp
Zadania zostały znalezione na platformie [Szkopuł] i wykonane w języku python.

Celem zadań jest przygotowanie do olimpiady informatycznej oraz poznanie różnych struktur danych.

## Zadanie Astmatyk 
`Link do zadania:` [Astmatyk]

### ***Treść zadania***

Bajtazar jest miłośnikiem wycieczek górskich. Niestety cierpi na astmę i gdy wejdzie na zbyt dużą wysokość to zaczyna się dusić. Z tego powodu musi bardzo dokładnie planować swoje wyprawy. Jednak nie jest to proste. Bajtazar posiada bardzo dokładne mapy gór z dziesiątkami tysięcy szlaków, każdy szlak zaczyna się na pewnej wysokości i na jakiejś kończy. Nasz bohater ustalił miejsce skąd wyrusza i dokąd się kieruje jednak przytłoczony ilością informacji za bardzo sobie nie radzi z ułożeniem optymalnej trasy.

***Autor:*** Piotr Cerobski

### ***Zadanie***

Pomóż Bajtazarowi w ułożeniu wycieczki. Napisz program który wczyta opis gór (punkty na różnych wysokościach połączone szlakami) i powie na jaką minimalną wysokość musi wejść Bajtazar aby dojść do wyznaczonego miejsca.

### ***Problematyka zadania***

W zadaniu stosujemy strukturę danych jaką są grafy, w pythonie według mnie najłatwiej jest to zrobić na słownikach więc takim sposobem wykonałam to zadanie.

W zadaniu musimy też mieć na uwadze wagi (w tym przypadku wysokoości szczytów), konieczne więc jest zastosowanie algorytmu djikstry. 

## Zadanie Koleje
`Link do zadania:` [Koleje]

### ***Treść zadania***
Bajtocja nowo powstały kraj stanął przed problemem komunikacji. W państwie znajduje się n miast.
Obecny stan Bajtockich kolei jest zły. Krół postanowił wydać dekret o polepszeniu komunikacji.
Zgodnie z nim BKP musi stworzyć nowe połączenia pomiędzy miastami, tak aby każde miasto było
połączone z minimum dwoma innymi (w razie uszkodzenia jednej drogi, miasto nie może zostać bez
dostępu do świata). Połączenie to dwukierunkowe tory pomiędzy jakimiś dwoma miastami. Zarząd
firmy bez dłuższego namysłu chce wybudować minimalną liczbę nowych połączeń. Ty, jako młody
pracownik z ambicjami na prezesa firmy chcesz rozwiązać problem.

***Autor:*** Kacper Omieliańczyk

### ***Problematyka zadania***

W tym zadaniu również stosujemy grafy w podobny sposób jak w poprzednim zadaniu. To zadanie nie potrzebuje jakiegoś szczególnego algorytmu.





[//]: # (Referencje i odnośniki)
[Szkopuł]: <https://szkopul.edu.pl/>
[Astmatyk]: <https://szkopul.edu.pl/problemset/problem/3vy4TMf5rs5dDc3309nJZCSm/site/?key=statement>
[Koleje]: <https://szkopul.edu.pl/problemset/problem/bkp/site/?key=statement>