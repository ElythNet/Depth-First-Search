# Depth-First-Search
Implémentation d'un algorithme de parcours en profondeur récursif en Python dans le cadre du jeu de Goban


L'objectif est d'écrire une fonction is_taken qui prend en paramètre x, y et qui retourne vrai si la pierre à la position x, y est prise et faux sinon. Pour faire cette fonction on se base sur une fonction get_status(x, y) qui retourne :

Status.BLACK : quand la pierre à la position x, y est noire
Status.WHITE : quand la pierre à la position x, y est blanche
Status.EMPTY : quand il n'y a pas de pierre à la position x, y
Status.OUT : quand la position x, y est hors du goban
Complétez la méthode Goban.is_taken avec votre solution (vous pouvez ajouter des paramètres à la méthode si besoin). Celle-ci doit respecter les bonnes pratiques du Python. Vous pouvez tester votre solution à tout moment avec py.test (les tests sont dans le fichier test_goban.py).


Pour commencer et lancer les tests :

$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ pytest .


Exemples :

# = noir
o = blanc
. = vide


.#.
#o#    <= o est prise parce qu'elle n'a pas de liberté, elle n'a aucun espace vide adjacent
.#.


...
#o#    <= o n'est pas prise parce qu'elle a une liberté au dessus
.#.


o#    <= o est prise parce qu'elle n'a pas de liberté (le haut et la gauche sont hors du goban donc ce ne sont pas des libertés)
#.


oo.
##o    <= la forme # est prise parce qu'elle n'a pas de liberté
o#o
.o.


oo.
##.   <= la forme # n'est pas prise parce qu'elle a une liberté en x=2, y=1 (0, 0 en haut à gauche)
o#o
.o.
