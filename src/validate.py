import pandas as pd
from pathlib import Path

from great_expectations.core import ExpectationSuite, ExpectationConfiguration
from great_expectations.checkpoint import SimpleCheckpoint
from great_expectations.data_context import get_context


def run_validation(csv_path: str, suite_name: str = "churn_suite") -> bool:
    # Load data
    df = pd.read_csv(csv_path)

    # Create or load a local GE context (will scaffold ./great_expectations if missing)
    context = get_context()

    # Define a Pandas datasource and an in-memory dataframe asset
    ds = context.sources.add_or_update_pandas(name="local_pandas")
    asset = ds.add_dataframe_asset(name="churn_df")
    batch_request = asset.build_batch_request(dataframe=df)

    # Build (or update) the expectation suite
    suite = ExpectationSuite(suite_name)
    suite.add_expectation(
        ExpectationConfiguration(
            "expect_table_row_count_to_be_between",
            kwargs={"min_value": 100, "max_value": 1_000_000},
        )
    )

    required_cols = ["age", "tenure_months", "monthly_charges", "num_services", "promo_flag", "churn"]
    for col in required_cols:
        suite.add_expectation(
            ExpectationConfiguration(
                "expect_column_values_to_not_be_null",
                kwargs={"column": col},
            )
        )

    suite.add_expectation(
        ExpectationConfiguration(
            "expect_column_values_to_be_between",
            kwargs={"column": "churn", "min_value": 0, "max_value": 1},
        )
    )

    context.add_or_update_expectation_suite(expectation_suite=suite)

    # Validate using a validator
    validator = context.get_validator(
        batch_request=batch_request, expectation_suite_name=suite_name
    )
    result = validator.validate()

    # Optional: run a checkpoint and build Data Docs
    Path("reports").mkdir(exist_ok=True)  # your own folder (GE docs still go under ./great_expectations)
    checkpoint = SimpleCheckpoint(name="chk", data_context=context)
    checkpoint.run(
        validations=[{"batch_request": batch_request, "expectation_suite_name": suite_name}]
    )
    context.build_data_docs()

    print("Validation success:", bool(result.success))
    return bool(result.success)


if __name__ == "__main__":
    ok = run_validation("data/raw/churn_train.csv")
    if not ok:
        raise SystemExit(1)
