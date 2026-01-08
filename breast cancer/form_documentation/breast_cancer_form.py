# Breast Cancer Wisconsin Dataset Form Structure
# Generated from data.csv

FORM_STRUCTURE = {
  "dataset_name": "Breast Cancer Wisconsin (Diagnostic)",
  "description": "Predict breast cancer diagnosis based on cell features",
  "shape": {
    "rows": 569,
    "columns": 33
  },
  "target_variable": {
    "name": "diagnosis",
    "type": "categorical",
    "values": [
      "M",
      "B"
    ],
    "distribution": {
      "B": 357,
      "M": 212
    }
  },
  "columns": [
    {
      "name": "id",
      "dtype": "int64",
      "null_count": 0,
      "min": 8670.0,
      "max": 911320502.0,
      "mean": 30371831.432337433,
      "std": 125020585.61222365,
      "median": 906024.0,
      "role": "identifier",
      "description": "Sample ID"
    },
    {
      "name": "diagnosis",
      "dtype": "object",
      "null_count": 0,
      "unique_values": 2,
      "sample_values": [
        "M",
        "M",
        "M"
      ],
      "role": "target",
      "description": "Diagnosis (M=Malignant, B=Benign)"
    },
    {
      "name": "radius_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 6.981,
      "max": 28.11,
      "mean": 14.127291739894552,
      "std": 3.5240488262120775,
      "median": 13.37,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "texture_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 9.71,
      "max": 39.28,
      "mean": 19.289648506151142,
      "std": 4.301035768166949,
      "median": 18.84,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "perimeter_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 43.79,
      "max": 188.5,
      "mean": 91.96903339191564,
      "std": 24.298981038754906,
      "median": 86.24,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "area_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 143.5,
      "max": 2501.0,
      "mean": 654.8891036906855,
      "std": 351.914129181653,
      "median": 551.1,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "smoothness_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.05263,
      "max": 0.1634,
      "mean": 0.0963602811950791,
      "std": 0.01406412813767362,
      "median": 0.09587,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "compactness_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.01938,
      "max": 0.3454,
      "mean": 0.10434098418277679,
      "std": 0.052812757932512194,
      "median": 0.09263,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "concavity_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.0,
      "max": 0.4268,
      "mean": 0.0887993158172232,
      "std": 0.07971980870789348,
      "median": 0.06154,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "concave points_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.0,
      "max": 0.2012,
      "mean": 0.04891914586994728,
      "std": 0.038802844859153605,
      "median": 0.0335,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "symmetry_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.106,
      "max": 0.304,
      "mean": 0.18116186291739894,
      "std": 0.027414281336035715,
      "median": 0.1792,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "fractal_dimension_mean",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.04996,
      "max": 0.09744,
      "mean": 0.06279760984182776,
      "std": 0.007060362795084459,
      "median": 0.06154,
      "role": "feature",
      "category": "mean_features"
    },
    {
      "name": "radius_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.1115,
      "max": 2.873,
      "mean": 0.40517205623901575,
      "std": 0.2773127329861039,
      "median": 0.3242,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "texture_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.3602,
      "max": 4.885,
      "mean": 1.2168534270650264,
      "std": 0.5516483926172023,
      "median": 1.108,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "perimeter_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.757,
      "max": 21.98,
      "mean": 2.8660592267135327,
      "std": 2.0218545540421076,
      "median": 2.287,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "area_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 6.802,
      "max": 542.2,
      "mean": 40.337079086116,
      "std": 45.49100551613181,
      "median": 24.53,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "smoothness_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.001713,
      "max": 0.03113,
      "mean": 0.007040978910369069,
      "std": 0.0030025179438390656,
      "median": 0.00638,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "compactness_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.002252,
      "max": 0.1354,
      "mean": 0.025478138840070295,
      "std": 0.017908179325677388,
      "median": 0.02045,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "concavity_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.0,
      "max": 0.396,
      "mean": 0.03189371634446397,
      "std": 0.03018606032298841,
      "median": 0.02589,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "concave points_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.0,
      "max": 0.05279,
      "mean": 0.011796137082601054,
      "std": 0.006170285174046869,
      "median": 0.01093,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "symmetry_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.007882,
      "max": 0.07895,
      "mean": 0.02054229876977153,
      "std": 0.008266371528798399,
      "median": 0.01873,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "fractal_dimension_se",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.0008948,
      "max": 0.02984,
      "mean": 0.0037949038664323374,
      "std": 0.002646070967089195,
      "median": 0.003187,
      "role": "feature",
      "category": "standard_error_features"
    },
    {
      "name": "radius_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 7.93,
      "max": 36.04,
      "mean": 16.269189806678387,
      "std": 4.833241580469323,
      "median": 14.97,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "texture_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 12.02,
      "max": 49.54,
      "mean": 25.677223198594024,
      "std": 6.146257623038319,
      "median": 25.41,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "perimeter_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 50.41,
      "max": 251.2,
      "mean": 107.26121265377857,
      "std": 33.602542269036356,
      "median": 97.66,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "area_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 185.2,
      "max": 4254.0,
      "mean": 880.5831282952548,
      "std": 569.356992669949,
      "median": 686.5,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "smoothness_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.07117,
      "max": 0.2226,
      "mean": 0.13236859402460457,
      "std": 0.022832429404835465,
      "median": 0.1313,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "compactness_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.02729,
      "max": 1.058,
      "mean": 0.25426504393673116,
      "std": 0.157336488913742,
      "median": 0.2119,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "concavity_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.0,
      "max": 1.252,
      "mean": 0.27218848330404216,
      "std": 0.2086242806081323,
      "median": 0.2267,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "concave points_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.0,
      "max": 0.291,
      "mean": 0.11460622319859401,
      "std": 0.06573234119594207,
      "median": 0.09993,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "symmetry_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.1565,
      "max": 0.6638,
      "mean": 0.2900755711775044,
      "std": 0.061867467537518685,
      "median": 0.2822,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "fractal_dimension_worst",
      "dtype": "float64",
      "null_count": 0,
      "min": 0.05504,
      "max": 0.2075,
      "mean": 0.0839458172231986,
      "std": 0.018061267348893986,
      "median": 0.08004,
      "role": "feature",
      "category": "worst_features"
    },
    {
      "name": "Unnamed: 32",
      "dtype": "float64",
      "null_count": 569,
      "min": NaN,
      "max": NaN,
      "mean": NaN,
      "std": NaN,
      "median": NaN,
      "role": "feature"
    }
  ]
}