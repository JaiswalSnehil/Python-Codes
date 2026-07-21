import pubchempy as pcp

che_name = input("Enter chemical name:")

try:
    compound = pcp.get_compounds(che_name, 'name')[0]
    print(f"IUPAC Name: {compound.iupac_name}")
    print(f"Common Name: {compound.synonyms[0]}")
    print(f"Molecular Weight: {compound.molecular_weight}")
    print(f"Formula: {compound.molecular_formula}")

except IndexError:
    print(f"No information found for {che_name}")