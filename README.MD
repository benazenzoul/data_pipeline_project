Pour ce projet, j'ai mis en place un pipeline de données structuré pour traiter et analyser des mentions de médicaments dans des publications scientifiques. 
Voici les étapes que j'ai suivies et le raisonnement derrière chacune :

1. Création de l'Architecture du Projet
J'ai structuré ce projet avec différents dossiers pour organiser le code et les données :

data/ : J'y ai placé les fichiers sources, comme drugs.csv, pubmed.csv, clinical_trials.csv, et pubmed.json.
output/ : Ce dossier stocke les fichiers de sortie, incluant le fichier final output.json.
src/ : C'est ici que j'ai créé des modules séparés pour chaque étape du pipeline.
main.py : Le script principal qui orchestre tout le pipeline de bout en bout.
Cette architecture me permet de garder un code bien organisé, facile à maintenir et à étendre pour des besoins futurs.

2. Développement des Modules Python
J'ai ensuite créé des modules spécifiques pour chaque étape du pipeline :

data_ingestion.py : Ce module charge les fichiers CSV et JSON en utilisant des listes de dictionnaires, rendant les données prêtes pour la transformation.
data_transformation.py : Ici, j'ai défini la logique pour repérer les mentions de médicaments dans les titres d'articles. La fonction find_drug_mentions recherche chaque médicament dans les titres pour identifier les mentions pertinentes.
data_aggregation.py : Ce module génère le fichier JSON final, où chaque médicament est lié aux journaux dans lesquels il est mentionné, avec la date et la source (PubMed ou Clinical Trials).
analysis.py : Ce module additionnel contient des analyses bonus, comme :
Trouver le journal avec le plus de mentions de médicaments.
Trouver les médicaments mentionnés dans les mêmes journaux que le médicament cible (hors Clinical Trials pour les sources PubMed uniquement).

3. Exécution et Sauvegarde des Résultats
J'ai orchestré toutes les étapes du pipeline dans main.py : de l'ingestion des données à la création du fichier JSON de sortie. Après la génération du fichier JSON, j'ai aussi exécuté les fonctions d'analyse et sauvegardé les résultats dans la console.

4. Raisonnement pour le Pipeline
L'objectif principal de ce pipeline est de créer une structure de données qui relie les médicaments à leurs mentions dans différents journaux, via les publications scientifiques. Chaque module du pipeline est conçu pour accomplir une tâche spécifique : chargement, transformation, agrégation, et analyse. Cette organisation modulaire rend le pipeline plus simple à comprendre et à adapter pour d’autres projets ou futures améliorations.

5. Pour que mon code puisse gérer de grandes quantités de données, voici ce que j’envisagerais :

Formats optimisés : J’utiliserais des formats comme Parquet ou Avro pour la compression et des lectures plus rapides.
Traitement distribué avec GCP : J’utiliserais Dataflow pour traiter les données en parallèle et répartir la charge efficacement.
Stockage distribué : J’opterais pour Cloud Storage ou BigQuery, avec du partitionnement pour améliorer l'accès aux données et réduire les coûts.
Chargement en flux : Pour éviter de surcharger la mémoire, je mettrais en place un traitement en streaming ou par lots avec Dataflow.
Optimisation des requêtes : J’optimiserais les requêtes et transformations pour limiter les opérations lourdes et accélérer les traitements.