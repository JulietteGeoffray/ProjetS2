# Cahier des charges

<!-- Version brouillon hésiter pas a la modifier ou a mettre des commentaires pour qu'on en discute :) -->

## Présentation du projet

### Contexte

La mutagenèse est un processus par lequel l'information génétique d'un organisme donc de son ADN est modifiée, ce qui entraîne une mutation.

L'apparition des mutants dans une population est un phénomene rare avec une très faible probabilité. Afin d'augmenter cette probabilité, les organismes peuvent être traiter par des agents mutagènes qui vont introduire des mutations (remplacement, modification ou endommagement) sur l'organisme de manière aléatoire. Les agents mutagènes peuvent être de nature chimique comme EMS (_Méthanesulfonate d'éthyle_),de nature physique comme la lumière ultraviolette et les radiations ionisantes ou de nature bactérienne pathogenique qui contienne des plasmides (ex _T DNA_) capable de s'integrer au génome de l'hôte.

Provoquer des mutations dans un organisme d’intérêt permet de localiser les gènes d’intérêts, de les cartographier et d'en déduire des informations sur le rôle des gènes. Identification des mutations responsables du phénotype du mutant constitue le principe base de la "génétique classique". La méthode utilisée pour identifier la mutation recherchée est celle du clonage positionnel.

C'est une méthode utilisée dans les cas où on ne connaît pas ni la séquence, ni la fonction du gène mais dont la mutation est supposé être à l'origine d'un caractere phénotypique. Un croisement avec une lignée génétiquement différente qui n’a pas le phénotype mutant est réalisé. Suite au croisement il est necessaire de génotyper un grand nombre d'individu et cela est un facteur fastidieux et qui prend beaucoup de temps. La révolution dans les nouvelles technologies de séquençage et d'assemblage du génome a facilité la tâche. Aujourd'hui on peut sequencer plusieurs mutants en même temps et analyser les variations génomique sur tout le génome en une seule fois.

Toutefois c'est une analyse bioinformatique qui requiert de nombreuses étapes et l'utilisation de plusieurs programmes et logiciels distincts. La plupart des programmes utilisés sont adaptés à un organisme modèle ou à un « design » génétique et dépendent de
serveurs distants. Afin de faciliter l'étape de cartographie et l'identification des mutations un pipeline appelé "_Andalusian_Mapping_" a été devloppé. Ce pipeline permet de travailler avec differentes espèces et souches de cartographie.




<!--Dans cette analyse nous utiliserons des plantes qui sont capable de se reproduire avec elle même (selfing ou self-fertilization). Ce qui va nous être très être très utiles.

La question principale que l'on se pose est comme trouver la position de la mutation que l'on cherche? Par exemple on cherche le ou les gènes résponsable de la couleurs des feuilles. On va muter un grand nombre de plantes et si par chanche on se rend compte que l'un des pénotype a une couleur de feuille différente on a toucher ce ou ces gènes d'intéret. On va alors procéder par croissement pour esayer de retrouer le locus de notre mutation.

Les croisements :

+ **M0** : ligné sauvage de l'organisme d'interet.
+ **M1** : On va dans un premier temps générer des mutations dans des organismes d'interet M0. Avec des agent chimique, des onde ou des bactérie TDNA.
+ **M2** : La première génération obetnu par auto reproduction. Elle regroupe le fardeau mutationnel de son parent. A cete étpa on ne va pas voir les mutation recessive puique l'on a que des organisme hétérozygote.

+ **F1** : On va ensuite croiser les mutant créer en M2 avec une génération M0 sauvage. La génération obtenu nous indique si notre gène d'interet est dominant ou recessif, si on voit le phéntotipe le gène est dominant sinon il est recessif. Toute cette génération est hétérozygote.
+ **F2** : On obtient cette génération par retro reproduction de la génération F1. A cette étape on calcul les proportion de mutant/sauvage que l'ont obtient. Si l'on est proche des proportion medelienne on sais que le ou les mutations qui génère notre phétotipe sont proche l'une de l'autre. On est dans le cadre d'une ségrégation 3-1.
+ **F3** :

Le ségrégation c'est la séparation des phénotype grâce a une descendance, on sépare les trait récessif des parents.
-->
### Objectifs

L’objectif principale de ce projets consiste à créer une interface pour le remplissage d'un formulaire nécessaire au lancement du pipeline développer et d'une interface permettant un affichage claire des résultats de sortie.

On cherchera dans un premier temps a fournir un formulaire simple ou l'on devra renseigner tout les champs puis on vise l'implémentation, dans la mesure du possible, le remplissage automatique de certain champs si l'utilisateur le souhaite. Certain champs pourrons être remplis via des scripts développer par le maîtrise d’œuvre.

Il sera aussi appréciable, mais optionnel, d’apporter des conseils sur l’amélioration du pipeline en lui même. Comme facilité l’installation et des dépendance lié au logiciels utilisé.

### Description de l'existant

description du pipeline du guars.

### Critère d'acceptabilité du produit

Afin de répondre a la problématique une interface graphique sera développer. Elle devra permettre la rédaction du formulaire en entrée de pipeline, l’exécution du pipeline et enfin la visualisation des résultats de sorties.

Le logiciel doit être facile d'utilisation et informatif.

## Expression des besoins

### Besoins fonctionnels

Fonctionnalité du code :

Les fonctionnalité que doit remplir le code permettant la rédaction du fichier d'entrée du pipeline :

+ remplir les champs du fichier source (configuration du pipeline)
+ Dans un second temps on pourra prévoir un remplissage de certain champs automatiquement via des pipelines développer par le maîtrise d'ouvrage.

Les fonctionnalité que doit remplir le code permettant la sortie des résultats :

+ Visualisation claire des graphique d’intérêts.

### besoins non fonctionnels

L'interface développer est réaliser sous le système d'exploitation Linux, il comprendra des parties en Shell, python et on utilisera une librairie graphique python.

Le

## Contraintes

### Délais

Le projet s'organise sur une période de 4 semaines. Il débutera le lundi 5 février et prendra fin le vendredi 2 mars. Le projet pourra être continué durant une période de cours allant du 5 au 29 mars.

Un cahier des charges définitif devra être présenter le lundi 12 février.

Le délivrable final devra être rendu le 29 mars 2018.

### Autres contraintes

## Déroulement du projet

### Planification

Ajouter l'image du diagramme de Gantt.

### Plan d'assurance qualité

Le contrôle qualité de l'interface développée sera sa bonne exécution, sans erreur et en étant le plus facile et agréable à utiliser.

* Le logiciel sera tester par des membres de differents équipes.
* Validation par _Dr Besnard_
* Utilisation du logiciel par des utilisateurs non initiés en informatique

## Responsabilités

### Maîtrise d'ouvrage

Ce projet nous a été proposé par Fabrice Besnard, biologiste rattaché a l’École normale supérieur de Lyon (ENS), travaillant dans le Laboratoire Reproduction et Développement des Plantes (RDP).

### Maître d’œuvre

Pour réaliser ce projet nous serons trois étudiants en Master 1 de Bio-informatique a Lyon 1 : Juliette Geoffray, Hermes Paraqindes et Eric Cumunnel.
