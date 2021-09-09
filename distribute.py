from zinc_sampler import ZincDistributor

if __name__=="__main__":
    distributor = ZincDistributor('../zinc-dataset/')
    distributor.save_bins('../zinc-dataset-bins.yaml')