# save_breast_cancer_form.py
import json
import yaml
import pandas as pd
import numpy as np
from pathlib import Path

# Custom JSON encoder to handle NumPy types
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer, np.int64, np.int32, np.int16, np.int8)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float64, np.float32, np.float16)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)

# Load your data
df = pd.read_csv('data.csv')

# Create form structure
form_structure = {
    "dataset_name": "Breast Cancer Wisconsin (Diagnostic)",
    "description": "Predict breast cancer diagnosis based on cell features",
    "shape": {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1])
    },
    "target_variable": {
        "name": "diagnosis",
        "type": "categorical",
        "values": ["M", "B"],
        "distribution": {
            "B": int(df[df['diagnosis'] == 'B'].shape[0]),
            "M": int(df[df['diagnosis'] == 'M'].shape[0])
        }
    },
    "columns": []
}

# Add column information
for col in df.columns:
    col_info = {
        "name": col,
        "dtype": str(df[col].dtype),
        "null_count": int(df[col].isnull().sum())
    }
    
    # Handle different data types
    if df[col].dtype == 'object':
        col_info["unique_values"] = int(df[col].nunique())
        col_info["sample_values"] = df[col].head(3).tolist()
    elif pd.api.types.is_numeric_dtype(df[col]):
        col_info.update({
            "min": float(df[col].min()),
            "max": float(df[col].max()),
            "mean": float(df[col].mean()),
            "std": float(df[col].std()),
            "median": float(df[col].median())
        })
    
    # Assign roles
    if col == 'diagnosis':
        col_info["role"] = "target"
        col_info["description"] = "Diagnosis (M=Malignant, B=Benign)"
    elif col == 'id':
        col_info["role"] = "identifier"
        col_info["description"] = "Sample ID"
    else:
        col_info["role"] = "feature"
        # Add feature descriptions
        if "_mean" in col:
            col_info["category"] = "mean_features"
        elif "_se" in col:
            col_info["category"] = "standard_error_features"
        elif "_worst" in col:
            col_info["category"] = "worst_features"
    
    form_structure["columns"].append(col_info)

# Create output directory
output_dir = Path("form_documentation")
output_dir.mkdir(exist_ok=True)

# Save in different formats using custom encoder
try:
    # JSON
    with open(output_dir / 'breast_cancer_form.json', 'w') as f:
        json.dump(form_structure, f, indent=2, cls=NumpyEncoder)
    
    # YAML (handles NumPy types better)
    with open(output_dir / 'breast_cancer_form.yaml', 'w') as f:
        # Convert all NumPy types to Python native types first
        def convert_to_python_types(obj):
            if isinstance(obj, dict):
                return {k: convert_to_python_types(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_to_python_types(v) for v in obj]
            elif isinstance(obj, (np.integer, np.int64, np.int32, np.int16, np.int8)):
                return int(obj)
            elif isinstance(obj, (np.floating, np.float64, np.float32, np.float16)):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, np.bool_):
                return bool(obj)
            else:
                return obj
        
        yaml_data = convert_to_python_types(form_structure)
        yaml.dump(yaml_data, f, default_flow_style=False)
    
    # Python
    with open(output_dir / 'breast_cancer_form.py', 'w') as f:
        f.write("# Breast Cancer Wisconsin Dataset Form Structure\n")
        f.write("# Generated from data.csv\n\n")
        f.write(f"FORM_STRUCTURE = {json.dumps(form_structure, indent=2, cls=NumpyEncoder)}")
    
    # Also create a simple CSV summary
    summary_data = []
    for col in form_structure["columns"]:
        if col["role"] == "feature":
            summary_data.append({
                "feature_name": col["name"],
                "category": col.get("category", "unknown"),
                "dtype": col["dtype"],
                "min": col.get("min", "N/A"),
                "max": col.get("max", "N/A"),
                "mean": col.get("mean", "N/A"),
                "null_count": col["null_count"]
            })
    
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_csv(output_dir / 'feature_summary.csv', index=False)
    
    # Create a simple README
    with open(output_dir / 'README.md', 'w') as f:
        f.write(f"""# Breast Cancer Wisconsin Dataset Documentation

## Dataset Information
- **Name**: Breast Cancer Wisconsin (Diagnostic)
- **Rows**: {form_structure['shape']['rows']}
- **Columns**: {form_structure['shape']['columns']}
- **Target Variable**: diagnosis
- **Classes**: 
  - B (Benign): {form_structure['target_variable']['distribution']['B']} samples
  - M (Malignant): {form_structure['target_variable']['distribution']['M']} samples

## Feature Categories
1. **Mean Features** (10): Features ending with '_mean'
2. **Standard Error Features** (10): Features ending with '_se'
3. **Worst Features** (10): Features ending with '_worst'

## Generated Files
- `breast_cancer_form.json` - Complete form structure in JSON
- `breast_cancer_form.yaml` - Complete form structure in YAML
- `breast_cancer_form.py` - Form structure as Python dictionary
- `feature_summary.csv` - Summary of all features
- `README.md` - This file

## Usage
This form documentation can be used for:
- Data validation
- Feature engineering
- Model training
- Dataset documentation
""")
    
    print("="*60)
    print("FORM DOCUMENTATION CREATED SUCCESSFULLY!")
    print("="*60)
    print(f"\nDataset Information:")
    print(f"  - Rows: {form_structure['shape']['rows']}")
    print(f"  - Columns: {form_structure['shape']['columns']}")
    print(f"  - Target variable: 'diagnosis'")
    print(f"  - Class distribution: B={form_structure['target_variable']['distribution']['B']}, M={form_structure['target_variable']['distribution']['M']}")
    
    print(f"\nGenerated files in '{output_dir}/' directory:")
    print("  1. breast_cancer_form.json")
    print("  2. breast_cancer_form.yaml")
    print("  3. breast_cancer_form.py")
    print("  4. feature_summary.csv")
    print("  5. README.md")
    
    print(f"\nFirst few rows of data:")
    print(df.head())
    
except Exception as e:
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e)}")