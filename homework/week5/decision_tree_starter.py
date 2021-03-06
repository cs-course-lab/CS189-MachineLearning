"""
This is the starter code and some suggested architecture we provide you with. 
But feel free to do any modifications as you wish or just completely ignore 
all of them and have your own implementations.
"""
from collections import Counter

import numpy as np
from numpy import genfromtxt
import scipy.io
from scipy import stats

import random


class Node:
    def __init__(self, left=None, right=None, label=label,split_rule=split_rule):
        self.left = left
        self.right = right
        self.label = label
        self.split_rule = split_rule
        

class DecisionTree:

    def __init__(self,max_depth = 10):
        """
        TODO: initialization of a decision tree
        """
        self.max_depth = max_depth
        
    @staticmethod
    def entropy(y):
        _, counts = np.unique(y, return_counts=True)
        entropy_ = stats.entropy(counts, base=2)
        return entropy_

    @staticmethod
    def information_gain(y,left,right):

        entropy0 = DecisionTree.entropy(y)
        Sl = len(left)
        Sr = len(right)
        entropy1 = (Sl * DecisionTree.entropy(left) + Sr * DecisionTree.entropy(right))/(Sl + Sr)

        return entropy0 - entropy1

    def split(self, X, y, idx, thresh):
        left_filter = np.where(X[:,idx] > thresh)[0]
        right_filter = np.where(X[:,idx] <= thresh)[0]
        return X[left_filter], y[left_filter], X[right_filter], y[right_filter]
    
    def segmenter(self, X, y):
        """
        TODO: compute entropy gain for all single-dimension splits,
        return the feature and the threshold for the split that
        has maximum gain
        """
        return 0
    
    
    def fit(self, X, y):
        """
        TODO: fit the model to a training set. Think about what would be 
        your stopping criteria
        """
        return 0

    def predict(self, X):
        """
        TODO: predict the labels for input data 
        """
        return 0

    def __repr__(self):
        """
        TODO: one way to visualize the decision tree is to write out a __repr__ method
        that returns the string representation of a tree. Think about how to visualize 
        a tree structure. You might have seen this before in CS61A.
        """
        return 0


class RandomForest():
    
    def __init__(self):
        """
        TODO: initialization of a random forest
        """

    def fit(self, X, y):
        """
        TODO: fit the model to a training set.
        """
        return 0
    
    def predict(self, X):
        """
        TODO: predict the labels for input data 
        """
        return 0
    
if __name__ == "__main__":
    # dataset = "titanic"
    dataset = "spam"

    if dataset == "titanic":
        # Load titanic data       
        path_train = 'datasets/titanic/titanic_training.csv'
        data = genfromtxt(path_train, delimiter=',', dtype=None)
        path_test = 'datasets/titanic/titanic_testing_data.csv'
        test_data = genfromtxt(path_test, delimiter=',', dtype=None)
        y = data[1:, 0]  # label = survived
        class_names = ["Died", "Survived"]
        
        # TODO: preprocess titanic dataset
        # Notes: 
        # 1. Some data points are missing their labels
        # 2. Some features are not numerical but categorical
        # 3. Some values are missing for some features
        
    elif dataset == "spam":
        features = [
            "pain", "private", "bank", "money", "drug", "spam", "prescription",
            "creative", "height", "featured", "differ", "width", "other",
            "energy", "business", "message", "volumes", "revision", "path",
            "meter", "memo", "planning", "pleased", "record", "out",
            "semicolon", "dollar", "sharp", "exclamation", "parenthesis",
            "square_bracket", "ampersand"
        ]
        assert len(features) == 32

        # Load spam data
        path_train = 'datasets/spam-dataset/spam_data.mat'
        data = scipy.io.loadmat(path_train)
        X = data['training_data']
        y = np.squeeze(data['training_labels'])
        Z = data['test_data']
        class_names = ["Ham", "Spam"]
         
    else:
        raise NotImplementedError("Dataset %s not handled" % dataset)
    
    """
    TODO: train decision tree/random forest on different datasets and perform the tasks 
    in the problem
    """