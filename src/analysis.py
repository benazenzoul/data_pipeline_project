import json
from collections import Counter

def journal_with_most_drug_mentions(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    journal_drug_count = Counter()
    
    for drug, mentions in data.items():
        for mention in mentions:
            journal = mention['journal']
            journal_drug_count[journal] += 1
    
    # Trouve le journal avec le plus de mentions
    most_mentioned_journal = journal_drug_count.most_common(1)[0]
    return most_mentioned_journal[0], most_mentioned_journal[1]

def find_related_drugs(drug_name, json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    related_drugs = set()
    target_journals = set()
    
    # Récupère tous les journaux où le médicament donné est mentionné (PubMed uniquement)
    for mention in data.get(drug_name, []):
        if mention['source'] == 'PubMed':
            target_journals.add(mention['journal'])
    
    # Parcourt les autres médicaments pour trouver ceux mentionnés dans les mêmes journaux
    for drug, mentions in data.items():
        if drug != drug_name:
            for mention in mentions:
                if mention['journal'] in target_journals and mention['source'] == 'PubMed':
                    related_drugs.add(drug)
    
    return list(related_drugs)
