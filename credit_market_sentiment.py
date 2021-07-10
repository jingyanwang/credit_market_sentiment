import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('market_comments', 'rb') as file:
	market_comments = pickle.load(file)

print(market_comments[-1])