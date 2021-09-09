# Zinc Sampler
Zinc sampler takes a list of SMILES as input, then samples from the Zinc dataset to get a set of random molecules with the same molecular weight distribution

## Usage
Before using the sampler, we need to pre-process the Zinc dataset and distribute the SMILES into 9 bins. The intervals of molecular weights are the same the [Zinc tranches](https://zinc.docking.org/tranches/home/#).
```python
from zinc_sampler import ZincDistributor

# zinc-dataset contains tranch folders such as BA BB BC...
distributor = ZincDistributor('../zinc-dataset/')

# the distributed SMILES will be saved in a new yaml file
distributor.save_bins('../zinc-dataset-bins.yaml')
```

After the SMILES are correctly distributed, we can use the sampler to sample from the dataset for a similar molecular weight distribution as the input SMILES list.
```python

```