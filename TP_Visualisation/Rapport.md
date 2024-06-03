# Rapport TP Visualisation

Enzo Demeulenaere enzo.demeulenaere.etu@univ-lille.fr

## Questions du TP

**Etape 5 : Toujours pas de points à l'écran ? C'est normal ! Pourquoi ?**

Il semblerait déjà que x et y ne soient pas des listes mais des int, je remplace donc x et y par xList et yList ce qui me permets de compiler le code.

**Etape 6 : Observez les valeurs correspondant aux coordonnées x et y de vos villes. Que pouvez-vous en déduire ?**

Nous remarquons que dans le fichier les coordoonées de chaque villes ont des valeurs entre -1 et 1, ce qui fait que nous dessinons les points sur un mauvais réferentiel

En prenant en compte le fait qu'en informatique graphique le référentiel Y est inversé, nous implémentons la fonction mapY de telle manière :

```java
float mapY(float y) {
 return map(y, minY, maxY, 800, 0);
}
```
## En quoi consiste ce TP 

L'objectif était de faire une visualisation de données en étudiant différents choix de visualisation et leur influence sur notre compréhension des données.

Nous travaillons avec des données sur les villes de France avec des informations sur entre autres la population, la surface, l'altitude de chaque ville.

Nous devions alors placer un point à l'emplacement de chaque ville, formant donc une carte de France, notre but était dès lors de changer quelques variables visuelles pour comprendre certaines informations sur les villes.

Une partie supplémentaire suggérait l'implémentation d'une visualisation dynamique avec un slider permettant de filtrer certaines villes selon une variable choisie

## Choix de visualisation

Personellement j'ai choisi de me concentrer sur la population et la densité de population (calculée grâce à la surface).

La population est représentée par la taille du cercle choisi pour représenter la ville, un cercle plus grand correspond à une population plus grande, en revanche la taille du cercle a été choisie selon un seuillage et non une normalisation logarithmique des données.

La densité de population est représentée à l'aide de la luminance des points de chaque ville. La couleur choisie étant du rouge, une ville à densité basse aura une couleur rouge pale tandis qu'une ville à densité haute aura pour couleur un rouge très vif.
La valeur choisie pour la luminance a également était seuillée, car sinon les différences ne seraient que peu visibles à l'oeil nu

Ces choix amènent tout de même à une certaine limite qui est que compte tenu du nombre très grand de villes, il serait illisible de représenter chaque ville par un cercle, ainsi le seuillage choisi pour la donnée de population fait que les villes les moins peuplées et par conséquent la grande majorité des villes, sont représentées par un simple point et non un cercle.
Ce point constitue un problème pour la visualisation de la densité car cette donnée ne peut donc pas y être représentée.

Ainsi notre visualisation permets d'obtenir des informations sur la densité uniquement pour les villes ayant une population assez grande pour être visualisée. Ce qui pourrait être une très mauvaise visualisation si la densité était la variable la plus importante, or ici l'on se concentrait principalement sur la population

Lors de la partie intéraction du TP, il nous était demandé de pouvoir selectionner des villes en cliquant dessus et que la visualisation se voit changée. 
J'ai pour cela choisi de changer la couleur d'une ville selectionnée de rouge à verte, ce choix me permettait de garder la visualisation de la densitée car la variable de luminance pouvait toujours être exprimée.


## Etat du TP 

Je me suis arrété à l'étape 8 de la partie intéraction, j'ai implémenté un slider simple mais n'ai pas reussi à implementer une manière d'"étaloner" la plage de données sur le slider.


