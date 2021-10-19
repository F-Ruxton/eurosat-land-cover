import logging
import os
import pathlib
import typing as t

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


EUROSAT_CLASSES = {
    'AnnualCrop': 0,
    'Forest': 1,
    'HerbaceousVegetation': 2,
    'Highway': 3,
    'Industrial': 4,
    'Pasture': 5,
    'PermanentCrop': 6,
    'Residential': 7,
    'River': 8,
    'SeaLake': 9, 
}


def load_eurosat_data(
    logger: logging.Logger,
    data_dir: pathlib.Path,
    samples_per_class: int = 2000,
) -> t.Tuple[np.ndarray, np.ndarray]:
    images = []
    labels = []

    for filepath in sorted(data_dir.glob('*/data.npy')):
        logger.info(f'Loading {samples_per_class} images from {filepath}')

        label_class = os.path.split(os.path.split(filepath)[0])[1]

        encoding = np.zeros(10)
        encoding[EUROSAT_CLASSES[label_class]] = 1
        class_labels = np.tile(encoding, (samples_per_class, 1))

        with open(filepath, 'rb') as f:
            class_images = np.load(f)[samples_per_class, :, :, :]

        images.append(class_images)
        labels.append(class_labels)

    return np.asarray(images), np.asarray(labels)


def plot_confusion_matrix(df):
    plt.figure(figsize=(10, 10))
    sns.heatmap(df, annot=True, fmt='d', cmap=plt.cm.Blues)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
