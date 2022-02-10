import numpy as np
import panda as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
#Data collection and analysis
#loading the diabetes dataset to a pandas DataFrame
diabetes_dataset=pd.read_csv("")