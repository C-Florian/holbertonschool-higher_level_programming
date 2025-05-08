# 0x02. Python - import & modules

## Description

Ce projet fait partie du cursus **Higher Level Programming** de Holberton School.  
Il porte sur l'utilisation des **imports**, la création de **modules**, l'utilisation de **fonctions intégrées (`dir()`, `__name__`, etc.)** et la gestion des **arguments en ligne de commande**.

---

## Apprentissage

- Comment importer des fonctions ou des variables à partir d’un fichier ou d’un module.
- La différence entre l’exécution directe et l’import d’un fichier Python.
- Comment utiliser `__name__ == "__main__"` dans un script Python.
- Comment utiliser la bibliothèque standard de Python.
- Comment parcourir et utiliser des arguments avec `sys.argv`.

---

## Fichiers

| Fichier                   | Description |
|--------------------------|-------------|
| `0-add.py`               | Importe la fonction `add` et affiche le résultat de `1 + 2`. |
| `1-calculation.py`       | Importe 4 fonctions et affiche leurs résultats avec `a = 10` et `b = 5`. |
| `2-args.py`              | Affiche le nombre et la liste des arguments passés au script. |
| `3-infinite_add.py`      | Fait la somme de tous les arguments numériques passés en ligne de commande. |
| `/tmp/4-hidden_discovery.py` | Liste les noms définis dans le module `hidden_4`, sauf ceux qui commencent par `__`. |
| `5-variable_load.py`     | Importe la variable `a` du module `variable_load_5.py` et l’affiche. |

---

## Exécution

Chaque fichier Python peut être exécuté individuellement avec :

```bash
$ ./<nom_du_fichier.py> [arguments]

