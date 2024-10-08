import csv
import json

def load_csv_as_dict(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            rows.append(row)
        return rows

def load_data():
    drugs = load_csv_as_dict('data/drugs.csv')
    pubmed_csv = load_csv_as_dict('data/pubmed.csv')
    clinical_trials = load_csv_as_dict('data/clinical_trials.csv')
    
    # Charger le fichier JSON
    with open('data/pubmed.json', 'r') as f:
        pubmed_json = json.load(f)
        
    # Fusionner les données PubMed des deux sources
    pubmed = pubmed_csv + pubmed_json
    
    return drugs, pubmed, clinical_trials
