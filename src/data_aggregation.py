import json

def generate_output_json(mentions, output_file):
    output = {}
    
    for row in mentions:
        drug = row['drug']
        journal = row['journal']
        date = row['date']
        
        if drug not in output:
            output[drug] = []
        
        output[drug].append({
            'journal': journal,
            'date': date,
            'source': row['source']
        })
    
    # Écrire dans le fichier JSON
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=4)
