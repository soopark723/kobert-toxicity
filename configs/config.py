# -*- coding: utf-8 -*-
"""config.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H4d-lEfRZc-ene0yTswHTWIOlMPauO31
"""

import torch

# Environment
SEED = 42
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Data
LABEL_COLUMNS = ["gender", "age", "appearance", "individual/group", "cleanness"]
MAX_LENGTH = 128
BATCH_SIZE = 32
NUM_WORKERS = 2
PIN_MEMORY = True

# Model
MODEL_NAME = "skt/kobert-base-v1"
HIDDEN_DIMS = (512, 256)
DROPOUT_RATE = 0.3
NUM_CLASSES = len(LABEL_COLUMNS)

# Training
EPOCHS = 35
LEARNING_RATE = 3e-5
WARMUP_RATIO = 0.1
MAX_GRAD_NORM = 1
LOG_INTERVAL = 200

# Thresholds
THRESHOLD = 0.33
EVAL_THRESHOLD = 0.38