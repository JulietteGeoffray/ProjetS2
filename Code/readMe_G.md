
#Andalusian mapping

## Formulaire :

### Your inputs :

Cette partie permet de renseigner les fichiers fondamentale pour  l'analyse ainsi que son nom.

#### Nom de l'analyse :

Ce champs permet de nommer l'analyse que l'on souhaite réaliser. Cela permettra entre autre de recharger le formulaire si l'on veux réaliser une analyse similaire, ou l'on ne devra changer que quelque champs pour éviter de devoir tout remplir à nouveau.

#### Génome de référence :

Ce champs permet de charger le génome de référence qui servira pour l'analyse.

A l'aide du bouton "..." on peut accéder au gestionnaire de fichier afin de retrouver le fichier. Il est aussi possible d'écrire directement le chemin absolu du fichier dans le champs.

#### Read :

Ces champs permets de renseigner les fichier de lecture necéssaire a l'analyse. Il devrons être renseigner par paire, deux fichier consécutif devrons correspond au deux fichiers pared-end. Si plusieurs fichier de read sont disponnible on peut cliquer sur "+" pour ajouter des champs supplémentaire. Il s'ajouterons par deux. Le bouton "-" permet de réduire le nombre de champs. Il devrai y avoir au minimum deux fichier renseigner et le formulaire accèpte au maximum 8 fichiers.

A l'aide du bouton "..." on peut accéder au gestionnaire de fichier afin de retrouver le fichier. Il est aussi possible d'écrire directement le chemin absolu du fichier dans le champs.

### BGI :

Cette section permet de préciser différente information sur les lecture (Notament pour la meilleur utilisation de GATk).

#### Plateforme :

Ce champs permet d'indiquer la plateforme utilisé pour produire les lectures (ex: ILLUMINA)

#### Sample :

Ce champs permet de renseigner le nom de l'échantillon utilisé pour l'analyse.

#### Library :
#### RGID :
#### RGPU

### Design of the population for the cartographie :

Cette section permet de renseigner les différente informatiion concernant la cartographie.

#### Background strain ID :

Ce champs permet de renseigner l'identifiant de la back ground utilisé.

#### Referenced :

Indique si le background strain est un génome de référence ou non.

#### Mapping strain ID :

It should be the same as RGSM appearing in the $Mapping_gVCF (determine with &quot;Read Group&quot; information during analysis)

#### dbSNP :

Ce champs permet de renseigner le fichier de variant entre la background et la mapping avant la mutation de la mapping. Ainsi ces variants serons retirer de la liste de variant probable pour la mutation rechercher (évite les faut positif).

###Additionnal files

Ces fichiers serons optionnel, si les champs sont vide cela ne sera pas relever en erreur.

#### Liste of scaffolds ID and their size :



Cette liste pourra être générer automatique si aucun fichier n'est renseigner. Ce n'est pas encore le cas.
