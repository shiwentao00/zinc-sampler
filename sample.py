from zinc_sampler import ZincSampler
from zinc_sampler import smiles_to_weights, count_mol_weights

if __name__=="__main__":
    sampler = ZincSampler('../zinc-dataset-bins.pickle')
    
    # SMILES for testing 
    in_smiles = [
        'Nc1cc(N2CCCCC2)nc(N)[n+]1[O-]',
        'C[C@H](C(=O)O)c1ccc2c(c1)Cc1cccnc1O2',
        'CCCC(=O)Oc1cc(C)c(OC(=O)CCC)c2ccccc12',
        'OC[C@@H](O)[C@@H](O)[C@H](O)[C@@H]1NC(=S)N(c2ccccc2Cl)[C@H]1O',
        'C[C@@H]1CCCN(S(=O)(=O)c2ccc3[nH]c(=O)cc(C(=O)O)c3c2)C1',
        'CC(=O)CNC(=O)Cc1c(-c2ccc(Cl)cc2)nc2ccc(Cl)cn12',
        'CC(=O)O[C@@]1(C(C)=O)CC[C@H]2[C@@H]3C=C(Cl)C4=CC(=O)NC[C@]4(C)[C@H]3CC[C@@]21C',
        'CC[C@H](C)[C@H](NC(=O)CN)C(=O)OC[C@@H]1O[C@H](n2cc(F)c(=O)[nH]c2=O)[C@@H](O)[C@H]1O',
        'COC(=O)[C@H]1Cc2cc(C[C@H](C)NC[C@H](O)c3cccc(Cl)c3)ccc2N1C(=O)c1ccccc1',
        'O[C@@H]1C=C2CCN3Cc4cc5c(cc4[C@H]([C@H]1O)[C@H]23)OCO5',
    ]

    # counts for test input
    test_counts = count_mol_weights(smiles_to_weights(in_smiles))
    print('test input counts:')
    print(test_counts)

    # sample output
    sampled = sampler.sample_mols(in_smiles)
    out_counts = count_mol_weights(smiles_to_weights(sampled))
    print('output counts:')
    print(out_counts)
    print(sampled)
