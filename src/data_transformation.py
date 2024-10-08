def find_drug_mentions(drug, title):
    # Vérifie que le titre n'est pas None
    if title is not None:
        return drug.lower() in title.lower()
    return False  # Retourne False si le titre est None

def transform_data(drugs, pubmed, clinical_trials):
    mentions = []
    
    # Rechercher les mentions dans PubMed
    for drug_row in drugs:
        drug = drug_row['drug']
        atccode = drug_row['atccode']
        
        # Parcourir les publications PubMed
        for pubmed_row in pubmed:
            if find_drug_mentions(drug, pubmed_row['title']):
                mentions.append({
                    'drug': drug,
                    'atccode': atccode,
                    'source': 'PubMed',
                    'journal': pubmed_row['journal'],
                    'date': pubmed_row['date']
                })
        
        # Parcourir les essais cliniques
        for clinical_row in clinical_trials:
            if find_drug_mentions(drug, clinical_row['scientific_title']):
                mentions.append({
                    'drug': drug,
                    'atccode': atccode,
                    'source': 'Clinical Trials',
                    'journal': clinical_row['journal'],
                    'date': clinical_row['date']
                })
    
    return mentions
