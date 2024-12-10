def create_codon_dict(file_path):
    path = "data/codons.txt"
    file = open(path)
    rows=file.readlines()
    file.close()
    codon_amino_dict={}
    for row in rows:
        cells=row.strip().split('\t') 
        codon=cells[0]
        amino_acid=cells[2]
        codon_amino_dict[codon]=[amino_acid]
    return codon_amino_dict

