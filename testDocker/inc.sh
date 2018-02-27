#!/bin/bash

echo "docker" > /home/etudiant/Bureau/Projet/ProjetS2/testDocker/files.txt

for number in {1..10}
do
echo "Etape $number" > /home/etudiant/Bureau/Projet/ProjetS2/testDocker/files.txt
sleep 4
echo "en cours"
done
exit 0
