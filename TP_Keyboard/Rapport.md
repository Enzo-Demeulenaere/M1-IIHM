# Rapport TP Keyboard

Enzo Demeulenaere enzo.demeulenaere.etu@univ-lille.fr

## Etat du TP

Tout a été fait et cela fonctionne, le clavier nous permets d'afficher des suggestions de mots et de les selectionner pour les écrire dans le QLineEdit.

## Difficultés rencontrées

L'algorithme DTW semble fonctionner correctement à l'exception peut-être de quelques mots avec une double lettre comme le cas du mot "abeille" qui n'est pas toujours parmi les suggestions lorsqu'on tente de l'écrire.

Pour la représentation du tracé, j'ai utilisé la méthode drawLine entre chaque couple de point du tracé, cela donne un affichage suffisant mais qui peut provoquer de l'opacité plus importante par moment. Afficher le tracé avec la méthode drawPath semble pouvoir éviter ce problème mais je n'ai pas reussi à l'implementer et donc me contente de cet affichage.

Egalement je n'ai pas implémenté le comportement des touches n'étant pas des lettres étant donné leur nature facultative pour ce TP