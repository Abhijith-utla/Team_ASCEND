import json
import pandas as pd

def get_features():
    with open('ascend_variants.json') as f:
        data = json.load(f)

    problems = data['problems']

    difficulty_map = {
        'Easy' : 0,
        'Easy-Medium' : 1,
        'Medium' : 2,
    }

    delta_map = {
        'much_easier' : -2,
        'easier' : -1,
        'equivalent' : 0
    }

    simplification_types = [
        'dimension_reduction',
        'constraint_relaxation',
        'edge_case_removal',
        'domain_swap',
        'technique_decomposition'
    ]

    rows = []

    for p in problems:
        if p['depth'] == 0:
            continue

        features = {}
        
        features['depth'] = p['depth']
        features['difficulty'] = difficulty_map.get(p.get('difficulty'), 0)
        features['difficulty_delta'] = delta_map.get(p.get('difficulty_delta'), 0)
        features['num_constraints'] = len(p.get('constraints', []))
        features['description_length'] = len(p.get('description', '').split())

        for s in simplification_types:
            features[f'simp_{s}'] = int(p.get('simplification_type') == s)

        useful = 1 if (
            p.get('difficulty_delta') == 'easier' and
            p.get('simplification_type') in ['dimension_reduction', 'technique_decomposition']
        ) else 0

        features['useful'] = useful
        rows.append(features)

    df = pd.DataFrame(rows)
    return df