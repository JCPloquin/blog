#!/usr/bin/env python3
import csv
import os
from pathlib import Path
import yaml

def csv_to_hugo_i18n(csv_file):
    """Convertit un fichier CSV en fichiers i18n Hugo (YAML)"""
    
    # Créer le dossier i18n s'il n'existe pas
    i18n_dir = Path("i18n")
    i18n_dir.mkdir(exist_ok=True)
    
    # Dictionnaires pour stocker les traductions
    translations = {"fr": {}, "en": {}}
    
    # Lire le CSV
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row['key'].strip()
            # Ignorer les lignes de commentaires
            if key.startswith('#') or not key:
                continue
            
            translations['fr'][key] = row['fr'].strip()
            translations['en'][key] = row['en'].strip()
    
    # Générer les fichiers YAML avec la bibliothèque yaml
    for lang, trans in translations.items():
        output_file = i18n_dir / f"{lang}.yaml"
        with open(output_file, 'w', encoding='utf-8') as file:
            yaml.dump(trans, file, default_flow_style=False, allow_unicode=True, sort_keys=True)
        
        print(f"Fichier {output_file} généré avec {len(trans)} traductions")

# Utilisation
if __name__ == "__main__":
    csv_to_hugo_i18n("translations.csv")

