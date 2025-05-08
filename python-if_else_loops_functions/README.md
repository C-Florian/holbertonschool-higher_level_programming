# Python - if/else, loops, functions

## Objectif

Ce projet vise à approfondir les notions suivantes en Python :
- Les structures conditionnelles (`if`, `elif`, `else`)
- Les boucles (`for`, `while`)
- L'utilisation des fonctions
- Les opérations sur les caractères et les nombres
- Les bases de la programmation en C pour interagir avec Python

---

## Fichiers et description

| Fichier | Description |
|--------|-------------|
| `0-positive_or_negative.py` | Affiche si un nombre est positif, négatif ou nul. |
| `1-last_digit.py` | Affiche le dernier chiffre d’un nombre aléatoire et donne un message selon sa valeur. |
| `2-print_alphabet.py` | Affiche l’alphabet en minuscules, sans sauter de lettres. |
| `3-print_alphabt.py` | Affiche l’alphabet sauf les lettres `q` et `e`. |
| `4-print_hexa.py` | Affiche les nombres de 0 à 98 en décimal et en hexadécimal. |
| `5-print_comb2.py` | Affiche toutes les combinaisons possibles de deux chiffres (00 à 99). |
| `6-print_comb3.py` | Affiche toutes les combinaisons de deux chiffres sans répétition ni inversion (ex : 01, 12, ...). |
| `7-islower.py` | Fonction qui vérifie si un caractère est en minuscule. |
| `8-uppercase.py` | Fonction qui affiche une chaîne en majuscules sans modifier les caractères non alphabétiques. |
| `9-print_last_digit.py` | Fonction qui affiche et retourne le dernier chiffre d’un nombre. |
| `10-add.py` | Fonction qui retourne la somme de deux entiers. |
| `11-pow.py` | Fonction qui retourne la puissance d’un nombre (`a ** b`). |
| `12-fizzbuzz.py` | Fonction qui imprime les nombres de 1 à 100 en remplaçant certains par Fizz, Buzz ou FizzBuzz selon les règles. |
| `13-insert_number.c` | Fonction en C qui insère un nombre dans une liste simplement chaînée triée. |
| `lists.h` | Fichier d'en-tête associé au fichier C avec la structure de la liste et la déclaration de la fonction. |

---

## Compilation C

Pour compiler le fichier C :

```bash
gcc -Wall -Werror -Wextra -pedantic 13-insert_number.c main.c -o insert -std=gnu89

