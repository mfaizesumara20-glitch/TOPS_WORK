# Predicting 7-9 PM Restaurant-Zone Demand: Data Science Lifecycle

## 1. Problem Definition

The business goal is to identify restaurant delivery zones likely to experience **peak order demand between 7:00 and 9:00 PM**. Operations can use the prediction to pre-position delivery partners, guide restaurant staffing and stock planning, and target customer promotions.

The team should define the target before analysing data: for each zone and evening, predict either (a) the expected number of completed orders from 7-9 PM, or (b) whether the zone will exceed a defined peak threshold, such as its historical 80th-percentile order volume. The prediction horizon should also be agreed--for example, a forecast produced by 4 PM for the same evening.

**Concrete deliverable:** A problem-definition brief containing the target variable, unit of prediction (zone x date), forecast horizon, users and decisions supported, success metrics (for example, recall of peak zones and forecast error), and constraints such as data availability and operational capacity.

## 2. Data Collection

Gather the two years of order spreadsheets and create a data inventory. Useful fields include order ID, order timestamp, restaurant ID, restaurant zone, delivery zone, order status, order value, cancellation reason, promised and actual delivery times, and customer location where permitted. Add external or operational data that is available at prediction time, such as day of week, public holidays, local events, weather, restaurant opening hours, active promotions, and delivery-partner availability.

Data should be collected at the most detailed safe level, then aggregated later. The team must also document which source owns each field, refresh frequency, time zone, and whether the field is known before 7 PM; this prevents data leakage.

**Concrete deliverable:** A versioned, consolidated raw dataset (or data extract) plus a data dictionary and source/lineage inventory.

## 3. Data Preparation

Standardise column names, date formats and zone labels across spreadsheets; remove duplicate orders; resolve or flag missing values; and exclude invalid test records. Convert timestamps into local time and derive the 7-9 PM order counts for every zone-date, including zero-order combinations where appropriate.

Create model-ready features known before the forecast cutoff: recent demand (for example, prior 7-day average), demand on the same weekday in recent weeks, day of week, month, holiday/event indicators, weather forecast, promotion flag, restaurant availability, and available courier supply. Create the target label--order volume or the peak/not-peak flag--using only the actual 7-9 PM outcome. Split data chronologically into training, validation and held-out test periods.

**Concrete deliverable:** A documented, reproducible cleaned analytical table / feature dataset, target definition, and time-based train-validation-test split.

## 4. Exploration

Profile demand by zone, weekday, month, weather, events and promotions. Plot 7-9 PM order volume over time, map high-demand zones, inspect missingness and outliers, and compare peak-zone patterns with normal evenings. Check whether a small number of zones dominate orders, whether demand changes by season, and whether key data fields are sufficiently complete and reliable.

The exploration should also establish simple benchmarks, such as "use last week's same weekday volume" or "use the recent four-week average." These are essential comparators for a model.

**Concrete deliverable:** An exploratory-data-analysis report or dashboard containing validated findings, data-quality issues, demand visualisations, and baseline forecast performance.

## 5. Modelling

Start with the baseline forecast from exploration. Then train suitable models on the prepared features: a regression model for expected order count (for example, regularised regression, random forest, or gradient boosting) and/or a classification model for peak-zone probability. Use time-aware cross-validation and tune models on the validation period. Ensure all features would genuinely be available at the 4 PM forecast cutoff.

Choose a decision threshold with operations: for example, alert zones whose predicted peak probability exceeds a level that matches the number of couriers the company can reposition. Produce interpretable outputs such as predicted order volume, peak probability, and the leading drivers for each zone.

**Concrete deliverable:** A versioned trained model (including feature pipeline and configuration), a baseline comparison, and a daily zone-level prediction output or prototype forecast service.

## 6. Evaluation

Evaluate on the untouched, most recent test period and compare with the baseline. For volume forecasts, use MAE or WAPE; for peak-zone classification, use precision, recall, F1 score, and a confusion matrix. Because a missed peak zone can cause long delivery times, recall may deserve more weight than precision--but this trade-off should be agreed with operations.

Break results down by zone, weekday, season, promotion status and restaurant density to find weak segments. Confirm that the model improves an operational measure, such as reduced late deliveries or better courier utilisation, through a pilot or A/B test. Define post-launch monitoring for accuracy, data quality and demand drift, with a retraining and human-override process.

**Concrete deliverable:** A signed-off evaluation report with test metrics, segment/fairness checks, comparison to baseline, go/no-go recommendation, and monitoring plan.

## Where Generative AI Can Accelerate the Work

| Stage | Useful generative-AI assistance | Risk without human review |
| --- | --- | --- |
| **Data Preparation** | Generate draft SQL/Python to standardise spreadsheets, parse inconsistent timestamps, flag duplicates, and document feature-engineering logic. It can also propose validation checks for missing or impossible values. | AI-generated transformation code may silently misinterpret a field, time zone, or status code, creating incorrect labels or data leakage. An analyst must test outputs against known records and confirm every feature is available before the forecast cutoff. |
| **Exploration** | Summarise exploratory results, suggest relevant plots and hypotheses, and help draft a dashboard narrative from approved aggregates. This speeds the first pass through a large set of zone, time, and promotion combinations. | AI can state correlations as causes, invent unsupported explanations, or overlook data-quality caveats. An analyst must verify every claim against the source data and distinguish observed patterns from business assumptions. |

Generative AI is therefore a productivity aid, not the decision-maker: the data team remains accountable for data definitions, validation, modelling choices, and operational recommendations.
