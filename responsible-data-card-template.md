# Responsible Data Card

## Dataset purpose

This dataset is used to support a customer churn prediction problem.

The dataset may help identify customers who could be at risk of churn so that appropriate retention actions can be considered.

The model must not automatically make decisions about customers. Predictions should support human review.

## Provenance and permission

The dataset was provided as part of the RabTech Academy internship task for training and baseline modelling.

The available task materials do not document the original real-world source, individual consent records, or external licensing restrictions.

Therefore, the dataset should be used only for the intended internship learning and modelling purpose unless additional permission is provided.

## Population and representation

The dataset contains 12 customer records.

The represented customer attributes include tenure, support tickets, monthly spending, recent login activity, and plan type.

The small dataset size limits its ability to represent a wider customer population.

The dataset contains 5 churned customers and 7 non-churned customers, so the target classes are not perfectly balanced.

No demographic or sensitive personal attributes are included in the provided features.

## Features and target

### Features

- `tenure_months` — number of months the customer has been associated with the service.
- `support_tickets` — number of support tickets associated with the customer.
- `monthly_spend_inr` — customer's monthly spending in INR.
- `last_login_days` — number of days since the customer's last login.
- `plan_type` — customer's subscription plan, such as Basic, Standard, or Pro.

### Target

- `churned` — target label.
- `1` means the customer churned.
- `0` means the customer did not churn.

### Customer ID

`customer_id` is an identifier and should not be used as a predictive feature.

### Possible leakage and proxies

Features should only use information that would have been available before the prediction decision.

Post-churn information must not be included.

Plan type and spending may reflect customer behaviour or business segmentation, so their influence should be checked during error analysis.

## Quality checks

The dataset should be checked for:

- Missing values
- Duplicate records
- Invalid values
- Outliers
- Target-class balance
- Correct data types
- Separation of training and testing data

The provided dataset contains 12 records and no missing values or duplicate rows were observed during the initial inspection.

The target contains 5 churned records and 7 non-churned records.

Because the dataset is very small, train/test results may be unstable and should not be treated as evidence of real-world performance.

## Risks and safeguards

### Bias and representation risk

The dataset is very small and may not represent the broader customer population.

**Safeguard:** Test the model on additional representative data before real-world use.

### Privacy risk

Customer-level information should be handled carefully.

**Safeguard:** Do not expose customer identifiers or personal information unnecessarily.

### False-positive risk

A customer may be predicted as likely to churn even though they would not churn.

**Safeguard:** Use human review before taking retention actions.

### False-negative risk

A customer who is actually at risk may be predicted as not likely to churn.

**Safeguard:** Monitor recall and review missed churn cases.

### Misuse risk

Predictions could be incorrectly treated as certain outcomes.

**Safeguard:** Treat model output as a risk signal rather than a confirmed prediction of customer behaviour.

## Intended evaluation

The baseline should first be compared with the machine-learning model.

Evaluation should include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Recall is important for identifying as many actual churn cases as possible.

Precision is important for reducing unnecessary retention actions.

Error analysis should review false positives and false negatives.

The model should also be checked for calibration and stability when more representative data becomes available.

Fairness analysis should be performed if sensitive or demographic attributes are introduced in a future dataset.

The model should not be deployed based only on performance from this small training dataset.