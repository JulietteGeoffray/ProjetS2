#!/bin/bash

echo "Etape 1_Etape 2_Etape 3_Etape 4_Etape 5_FIN" > /home/etudiant/Bureau/Projet/ProjetS2/testDocker/files.txt

for number in {1..5}
do
echo "Etape $number" >> /home/etudiant/Bureau/Projet/ProjetS2/testDocker/files.txt
sleep 4
done
exit 0
