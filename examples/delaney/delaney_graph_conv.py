"""
Script that trains graph-conv models on Tox21 dataset.
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import numpy as np

from models import GraphConvTensorGraph

np.random.seed(123)
import tensorflow as tf

tf.set_random_seed(123)
import deepchem as dc
from deepchem.molnet import load_delaney

# Load Delaney dataset
delaney_tasks, delaney_datasets, transformers = load_delaney(
    featurizer='GraphConv', split='index')
train_dataset, valid_dataset, test_dataset = delaney_datasets

# Fit models
metric = dc.metrics.Metric(dc.metrics.pearson_r2_score, np.mean)

# Do setup required for tf/keras models
# Number of features on conv-mols
n_feat = 75
# Batch size of models
batch_size = 128
model = GraphConvTensorGraph(
    len(delaney_tasks), batch_size=batch_size, mode='regression')

# Fit trained model
model.fit(train_dataset, nb_epoch=20)

print("Evaluating model")
train_scores = model.evaluate(train_dataset, [metric], transformers)
valid_scores = model.evaluate(valid_dataset, [metric], transformers)

print("Train scores")
print(train_scores)

print("Validation scores")
print(valid_scores)
