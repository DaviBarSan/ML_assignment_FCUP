# combinaçoes de parametros:
# {
# shape_of_border: |, X, O, -;
# n classes: 2,3;
# level of overlap: high, low;
# n rows: 1000,  100000;
# classes_balance: balanced, imblanced;
# noise_of_classes: high, low
# }

mappings = {
    "shape_of_border": {
        "vertical":     1,
        "horizontal":   44,
        "cross":        7,
        "circle":       6
    },
    "level_of_overlap": {
        "high":         0.5,
        "low":          0.05
    },
    "dataset_size": {
        "small":        1000,
        "big":          100000
    },
    "classes_balance": {
        "balanced":     [0.5, 0.5],
        "imbalanced":   [0.8, 0.2]
    },
    "noise_of_classes": {
        "high":         0.5,
        "low":          0.05
    },
}