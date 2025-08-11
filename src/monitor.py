import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset # Corrected import for Evidently 0.4.x
from pathlib import Path
import json
import subprocess
import sys

REF = "data/raw/churn_train.csv"
NEW = "data/raw/churn_new_batch.csv"
OUT = Path("reports/drift_report.html")
OUT.parent.mkdir(exist_ok=True)

def compute_drift(reference_csv=REF, new_csv=NEW) -> float:
    ref = pd.read_csv(reference_csv)
    cur = pd.read_csv(new_csv)
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=cur)
    report.save_html(str(OUT))
    
    # Get numerical share of drifted features
    as_json = report.as_dict()
    
    # Safely access the 'share_of_drifted_features'
    # The structure might be slightly different in your Evidently version 0.4.33
    # We will navigate through the 'metrics' list, find the DataDriftPreset result,
    # and then extract the share of drifted features.
    
    share = 0.0 # Default value in case the key isn't found
    try:
        # Iterate through metrics to find the DataDriftPreset result
        for metric in as_json.get("metrics", []):
            if metric.get("metric_class") == "DataDriftPreset": # Check for the correct metric class
                result = metric.get("result")
                if result and "dataset_drift" in result:
                    share = result["dataset_drift"].get("share_of_drifted_features", 0.0)
                    break # Found the metric, no need to continue
    except Exception as e:
        print(f"Error extracting drift share: {e}")
        # If an error occurs, share remains 0.0 or you could raise it, depending on desired behavior.

    return float(share)

if __name__ == "__main__":
    share = compute_drift()
    print(f"Drift share: {share:.3f}")
    THRESHOLD = 0.3
    if share >= THRESHOLD:
        print("⚠️ Drift above threshold → triggering retrain…")
        # call retrain script
        ret = subprocess.call([sys.executable, "src/retrain.py"])
        sys.exit(ret)
    else:
        print("Drift within acceptable range; no action.")