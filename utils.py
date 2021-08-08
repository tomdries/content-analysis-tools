import pandas as pd

flatten = lambda t: [item for sublist in t for item in sublist]

def value_counts(li, ascending = False):
    counts = pd.DataFrame({'counted values': li})['counted values'].value_counts(ascending=ascending)
    n_unique = len(counts)
    return counts