"""
Centralize all configuration settings that other components will use.

- Paths configuration
- Model settings 
- training parameters
- class information
- etc.
"""

import os
from pathlib import Path

## TODO: Project structure
PROJECT_ROOT = Path(__file__).resolve().parents[0]
DATA_DIR = PROJECT_ROOT / 'Data'
LOGS_DIR = PROJECT_ROOT / 'Logs'
MODELS_DIR = PROJECT_ROOT / 'Models'

## TODO: Create the directories if they don't exist
for directory in [DATA_DIR, LOGS_DIR, MODELS_DIR]:
    os.makedirs(directory, exist_ok=True)

## TODO: Dataset paths
TRAIN_DIR = DATA_DIR / 'train.csv'
TEST_DIR = DATA_DIR / 'test.csv'

## TODO: Image parameters
IMG_SIZE = 224
IMG_CHANNELS = 3 # RGB

## TODO: Training parameters
BATCH_SIZE = 32
EPOCHS = 30
LEARNING_RATE = 2e-5  # Very low learning rate for fine-tuning
VALIDATION_SPLIT = 0.15

## TODO: Model parameters
MODEL_NAME = "densenet201"
CHECKPOINT_FORMAT = os.path.join(MODELS_DIR, "Checkpoints\{}_checkpoint_{{epoch:02d}}_{{val_accuracy:.4f}}.keras") # example: densenet201_checkpoint_01_0.9876.keras
BEST_MODEL_PATH = os.path.join(MODELS_DIR, "best_model.keras")

## TODO: Class information
# Original class mapping and descriptions
CLASS_MAPPING = {
    0: 'AD',   # Alzheimer's Disease
    1: 'CN',   # Cognitive Normal
    2: 'EMCI', # Early Mild Cognitive Impairment 
    3: 'LMCI'  # Late Mild Cognitive Impairment
}

CLASS_DESCRIPTIONS = {
    'AD': 'Alzheimer\'s Disease',
    'CN': 'Cognitive Normal',
    'EMCI': 'Early Mild Cognitive Impairment',
    'LMCI': 'Late Mild Cognitive Impairment'
}

# User-friendly class names mapping
USER_FRIENDLY_CLASSES = {
    'AD': 'Moderate Impairment',
    'CN': 'No Impairment',
    'EMCI': 'Very Mild Impairment',
    'LMCI': 'Mild Impairment'
}


## TODO: Training callbacks configuration
EARLY_STOPPING_PATIENCE = 10 # stop training if no improvement after 10 epochs
REDUCE_LR_PATIENCE = 5 # reduce the learning rate if no improvement after 5 epochs
REDUCE_LR_FACTOR = 0.1 # reduce the learning rate by a factor of 0.1
MIN_LR = 1e-8 # minimum learning rate

## TODO: Data augmentation parameters
ROTATION_RANGE = 15 
WIDTH_SHIFT_RANGE = 0.1
HEIGHT_SHIFT_RANGE = 0.1
SHEAR_RANGE = 0.2
ZOOM_RANGE = 0.2
HORIZONTAL_FLIP = True
FILL_MODE = 'nearest'

# test the paths configuration 
if __name__ == "__main__":
    print(f"PROJECT_ROOT: {PROJECT_ROOT}")
    print(f"DATA_DIR: {DATA_DIR}")
    print(f"LOGS_DIR: {LOGS_DIR}")
    print(f"MODELS_DIR: {MODELS_DIR}")
    
    print(f"TRAIN_DIR: {TRAIN_DIR}")
    print(f"TEST_DIR: {TEST_DIR}")
    
    print(f"CHECKPOINT_FORMAT: {CHECKPOINT_FORMAT}")
    print(f"BEST_MODEL_PATH: {BEST_MODEL_PATH}")