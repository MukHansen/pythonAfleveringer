import numpy as np
import networkx as nx

webget.download("https://snap.standford.edu/data/twitter_combined.txt.gz")

with gzip.open('twitter_combined.txt.gz') as f:
    g = nx.read_edgelist(f)
