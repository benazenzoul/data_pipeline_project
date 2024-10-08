from src.data_ingestion import load_data
from src.data_transformation import transform_data
from src.data_aggregation import generate_output_json
from src.analysis import journal_with_most_drug_mentions, find_related_drugs

def main():
    # Charger et transformer les données
    drugs, pubmed, clinical_trials = load_data()
    mentions = transform_data(drugs, pubmed, clinical_trials)
    
    # Générer le fichier JSON de sortie
    output_file = 'output/output.json'
    generate_output_json(mentions, output_file)
    
    # Appeler les fonctions d'analyse
    # 1. Trouver le journal avec le plus de mentions de médicaments
    journal_name, mention_count = journal_with_most_drug_mentions(output_file)
    print(f"Journal avec le plus de mentions de médicaments : {journal_name} ({mention_count} mentions)")
    
    # 2. Trouver les médicaments associés dans les mêmes journaux pour un médicament donné
    drug_name = 'aspirin'  # Exemple de médicament à analyser
    related_drugs = find_related_drugs(drug_name, output_file)
    print(f"Médicaments mentionnés dans les mêmes journaux que '{drug_name}' (hors Clinical Trials) : {related_drugs}")

if __name__ == "__main__":
    main()
