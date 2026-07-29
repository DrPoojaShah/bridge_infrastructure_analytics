"""
Prepare the bridge infrastructure dataset for Power BI.

This script reproduces the core data-selection and cleaning logic used in
the Databricks/PySpark notebook without changing the analytical methodology.

Input:
    data/raw/PS1.csv

Output:
    data/processed/bridge_powerbi_data.csv
"""

from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "PS1.csv"
OUTPUT_DIRECTORY = (
    PROJECT_ROOT / "data" / "processed" / "bridge_powerbi_data_temp"
)

FINAL_OUTPUT_FILE = (
    PROJECT_ROOT / "data" / "processed" / "bridge_powerbi_data.csv"
)


def create_spark_session() -> SparkSession:
    """Create a local Spark session."""

    return (
        SparkSession.builder
        .appName("BridgePowerBIDataPreparation")
        .master("local[*]")
        .getOrCreate()
    )


def load_raw_data(spark: SparkSession):
    """Load the source bridge CSV using its original quoting format."""

    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("multiLine", True)
        .option("quote", "'")
        .option("escape", "'")
        .option("sep", ",")
        .csv(str(INPUT_FILE))
    )


def select_project_columns(raw_df):
    """Select and rename the fields used by the project."""

    return raw_df.select(
        F.col("Year0").alias("year"),
        F.col("11").alias("state_code"),
        F.col("-2").alias("state_name"),
        F.col("State3").alias("structure_id_seq"),
        F.col("Code4").alias("structure_number_raw"),
        F.col("15").alias("owner_agency"),
        F.col("-6").alias("owner_agency_code"),
        F.col("State7").alias("county_name"),
        F.col("Name8").alias("year_built"),
        F.col("8").alias("main_span_material"),
        F.col("-10").alias("main_span_design"),
        F.col("Structure11").alias("deck_area_sqft"),
        F.col("Number12").alias("deck_condition_rating"),
        F.col("2025").alias("latitude"),
        F.col("NBI").alias("longitude"),
        F.col("Structure15").alias("adt"),
        F.col("Number16").alias("bridge_age"),
        F.col("22").alias("freeze_thaw_cycles"),
    )


def clean_bridge_data(bridges_df):
    """Clean identifiers, text values, and the deck-condition rating."""

    clean_df = (
        bridges_df
        .withColumn(
            "structure_number",
            F.regexp_replace("structure_number_raw", r"[^0-9]", ""),
        )
        .withColumn(
            "owner_agency",
            F.trim(F.regexp_replace("owner_agency", ",", " ")),
        )
        .withColumn(
            "county_name",
            F.trim(F.regexp_replace("county_name", ",", " ")),
        )
        .withColumn(
            "main_span_material",
            F.trim(F.regexp_replace("main_span_material", ",", " ")),
        )
        .withColumn(
            "main_span_design",
            F.trim(F.regexp_replace("main_span_design", ",", " ")),
        )
        .withColumn(
            "deck_condition_rating_clean",
            F.when(
                (F.col("deck_condition_rating") == "NULL")
                | (F.col("deck_condition_rating") == "")
                | F.col("deck_condition_rating").isNull(),
                None,
            ).otherwise(F.col("deck_condition_rating")),
        )
        .withColumn(
            "deck_condition_rating_digits",
            F.regexp_extract(
                "deck_condition_rating_clean",
                r"([0-9]+)",
                1,
            ),
        )
        .withColumn(
            "deck_condition_rating_digits",
            F.when(
                F.col("deck_condition_rating_digits") == "",
                None,
            ).otherwise(F.col("deck_condition_rating_digits")),
        )
        .withColumn(
            "deck_condition_rating_int",
            F.expr(
                "try_cast(deck_condition_rating_digits AS INT)"
            ),
        )
    )

    return (
        clean_df
        .drop(
            "structure_number_raw",
            "deck_condition_rating",
            "deck_condition_rating_clean",
            "deck_condition_rating_digits",
        )
        .withColumnRenamed(
            "deck_condition_rating_int",
            "deck_condition_rating",
        )
    )


def filter_invalid_values(clean_df):
    """Apply the same validity filters used in the analysis notebook."""

    return (
        clean_df
        .filter(
            (F.col("latitude") >= 24)
            & (F.col("latitude") <= 50)
        )
        .filter(
            (F.col("longitude") >= -125)
            & (F.col("longitude") <= -66)
        )
        .filter(F.col("bridge_age") > 0)
        .filter(F.col("deck_area_sqft") < 200000)
        .filter(F.col("deck_condition_rating").isNotNull())
        .filter(F.col("freeze_thaw_cycles").isNotNull())
    )


def add_dashboard_categories(filtered_df):
    """Add categorical fields used by Power BI visuals and slicers."""

    return (
        filtered_df
        .withColumn(
            "freeze_thaw_zone",
            F.when(
                F.col("freeze_thaw_cycles") < 20,
                "Low (0-20)",
            )
            .when(
                F.col("freeze_thaw_cycles") < 50,
                "Moderate (20-50)",
            )
            .when(
                F.col("freeze_thaw_cycles") < 80,
                "High (50-80)",
            )
            .otherwise("Extreme (80+)"),
        )
        .withColumn(
            "freeze_thaw_sort",
            F.when(F.col("freeze_thaw_cycles") < 20, 1)
            .when(F.col("freeze_thaw_cycles") < 50, 2)
            .when(F.col("freeze_thaw_cycles") < 80, 3)
            .otherwise(4),
        )
        .withColumn(
            "traffic_level",
            F.when(F.col("adt") < 500, "Very Low")
            .when(F.col("adt") < 2000, "Low")
            .when(F.col("adt") < 10000, "Medium")
            .when(F.col("adt") < 30000, "High")
            .otherwise("Very High"),
        )
        .withColumn(
            "traffic_sort",
            F.when(F.col("adt") < 500, 1)
            .when(F.col("adt") < 2000, 2)
            .when(F.col("adt") < 10000, 3)
            .when(F.col("adt") < 30000, 4)
            .otherwise(5),
        )
        .withColumn(
            "age_group",
            F.when(F.col("bridge_age") < 20, "Under 20 Years")
            .when(F.col("bridge_age") < 40, "20-39 Years")
            .when(F.col("bridge_age") < 60, "40-59 Years")
            .when(F.col("bridge_age") < 80, "60-79 Years")
            .otherwise("80+ Years"),
        )
        .withColumn(
            "age_group_sort",
            F.when(F.col("bridge_age") < 20, 1)
            .when(F.col("bridge_age") < 40, 2)
            .when(F.col("bridge_age") < 60, 3)
            .when(F.col("bridge_age") < 80, 4)
            .otherwise(5),
        )
        .withColumn(
            "condition_category",
            F.when(
                F.col("deck_condition_rating") >= 7,
                "Good",
            )
            .when(
                F.col("deck_condition_rating") >= 5,
                "Fair",
            )
            .otherwise("Poor"),
        )
        .withColumn(
            "condition_sort",
            F.when(F.col("deck_condition_rating") >= 7, 1)
            .when(F.col("deck_condition_rating") >= 5, 2)
            .otherwise(3),
        )
        .withColumn(
            "maintenance_risk",
            F.when(
                (F.col("deck_condition_rating") < 5)
                | (
                    (F.col("bridge_age") >= 60)
                    & (F.col("freeze_thaw_cycles") >= 80)
                )
                | (
                    (F.col("bridge_age") >= 60)
                    & (F.col("adt") >= 30000)
                ),
                "High Risk",
            )
            .when(
                (F.col("deck_condition_rating") < 7)
                | (F.col("bridge_age") >= 40)
                | (F.col("freeze_thaw_cycles") >= 50),
                "Moderate Risk",
            )
            .otherwise("Lower Risk"),
        )
        .withColumn(
            "maintenance_risk_sort",
            F.when(F.col("maintenance_risk") == "High Risk", 1)
            .when(F.col("maintenance_risk") == "Moderate Risk", 2)
            .otherwise(3),
        )
    )


def export_single_csv(powerbi_df):
    """Write a single CSV file for import into Power BI."""

    OUTPUT_DIRECTORY.parent.mkdir(parents=True, exist_ok=True)

    (
        powerbi_df
        .coalesce(1)
        .write
        .mode("overwrite")
        .option("header", True)
        .csv(str(OUTPUT_DIRECTORY))
    )

    part_files = list(OUTPUT_DIRECTORY.glob("part-*.csv"))

    if len(part_files) != 1:
        raise RuntimeError(
            "Expected one Spark output CSV, "
            f"but found {len(part_files)}."
        )

    if FINAL_OUTPUT_FILE.exists():
        FINAL_OUTPUT_FILE.unlink()

    part_files[0].replace(FINAL_OUTPUT_FILE)

    for remaining_file in OUTPUT_DIRECTORY.iterdir():
        remaining_file.unlink()

    OUTPUT_DIRECTORY.rmdir()


def main() -> None:
    """Run the complete Power BI data-preparation pipeline."""

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Source dataset not found: {INPUT_FILE}"
        )

    spark = create_spark_session()

    try:
        raw_df = load_raw_data(spark)
        bridges_df = select_project_columns(raw_df)
        clean_df = clean_bridge_data(bridges_df)
        filtered_df = filter_invalid_values(clean_df)
        powerbi_df = add_dashboard_categories(filtered_df)

        selected_columns = [
            "year",
            "state_code",
            "state_name",
            "structure_id_seq",
            "structure_number",
            "owner_agency",
            "owner_agency_code",
            "county_name",
            "year_built",
            "main_span_material",
            "main_span_design",
            "deck_area_sqft",
            "deck_condition_rating",
            "latitude",
            "longitude",
            "adt",
            "bridge_age",
            "freeze_thaw_cycles",
            "freeze_thaw_zone",
            "freeze_thaw_sort",
            "traffic_level",
            "traffic_sort",
            "age_group",
            "age_group_sort",
            "condition_category",
            "condition_sort",
            "maintenance_risk",
            "maintenance_risk_sort",
        ]

        final_df = powerbi_df.select(selected_columns)

        print(f"Raw rows: {raw_df.count():,}")
        print(f"Power BI rows: {final_df.count():,}")

        export_single_csv(final_df)

        print(
            "Power BI dataset created successfully:\n"
            f"{FINAL_OUTPUT_FILE}"
        )

    finally:
        spark.stop()


if __name__ == "__main__":
    main()