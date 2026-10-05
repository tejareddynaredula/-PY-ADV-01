import numpy as np


def euclidean_distance(x1, x2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt(np.sum((x1 - x2) ** 2))


def knn_predict_from_scratch(X_train, y_train, X_test, k):
    """
    Predict labels using K-Nearest Neighbors from scratch.

    Parameters:
        X_train: Training features
        y_train: Training labels
        X_test: Test features
        k: Number of nearest neighbors

    Returns:
        NumPy array containing predictions
    """

    if k <= 0:
        raise ValueError("k must be greater than 0")

    if k > len(X_train):
        raise ValueError("k cannot be greater than the number of training samples")

    predictions = []

    for test_point in X_test:

        distances = []

        for train_point, label in zip(X_train, y_train):
            distance = euclidean_distance(test_point, train_point)
            distances.append((distance, label))

        distances.sort(key=lambda item: item[0])

        nearest_neighbors = distances[:k]

        neighbor_labels = [label for _, label in nearest_neighbors]

        unique_labels, counts = np.unique(
            neighbor_labels,
            return_counts=True
        )

        predicted_label = unique_labels[np.argmax(counts)]

        predictions.append(predicted_label)

    return np.array(predictions)


def main():
    # Small example dataset
    X_train = np.array([
        [1, 1],
        [1, 2],
        [2, 1],
        [8, 8],
        [9, 8],
        [8, 9]
    ])

    y_train = np.array([
        0,
        0,
        0,
        1,
        1,
        1
    ])

    X_test = np.array([
        [2, 2],
        [8, 8]
    ])

    predictions = knn_predict_from_scratch(
        X_train,
        y_train,
        X_test,
        k=3
    )

    print("KNN from Scratch")
    print("=" * 40)
    print("Test samples:")
    print(X_test)
    print("\nPredictions:")
    print(predictions)


if __name__ == "__main__":
    main()