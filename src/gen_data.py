import numpy as np, pandas as pd
from pathlib import Path

def make_dataset(n=5000, seed=42, shift=0.0):
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 80, n)
    tenure = rng.integers(1, 72, n)
    monthly = rng.uniform(20, 120, n) + shift
    service = rng.integers(1, 5, n)
    promo = rng.integers(0, 2, n)

    logit = -3.0 + 0.02*monthly - 0.03*tenure + 0.2*service + 0.5*promo
    prob = 1/(1+np.exp(-logit))
    churn = rng.binomial(1, prob)

    return pd.DataFrame({
        "age": age,
        "tenure_months": tenure,
        "monthly_charges": monthly.round(2),
        "num_services": service,
        "promo_flag": promo,
        "churn": churn
    })

if __name__ == "__main__":
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    df = make_dataset()
    df.to_csv("data/raw/churn_train.csv", index=False)
    # create a "new batch" with slight distribution shift (for drift demo)
    df2 = make_dataset(n=1000, seed=123, shift=+8.0)
    df2.to_csv("data/raw/churn_new_batch.csv", index=False)
    print("wrote data/raw/churn_train.csv and data/raw/churn_new_batch.csv")
