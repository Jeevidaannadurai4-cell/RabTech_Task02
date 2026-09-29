# Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| False negatives | High | Monitor recall and review customers who were actually at risk but were predicted as non-churned. |
| False positives | Medium | Monitor precision and review unnecessary retention actions. |
| Dataset bias | High | Check representation across customer groups and collect more representative data. |
| Data privacy | High | Restrict access to customer data and avoid unnecessary exposure of customer identifiers. |
| Data leakage | High | Ensure that information available only after churn is not used as a model feature. |
| Small dataset | Medium | Validate the model on additional data before using it for real-world decisions. |
| Class imbalance | Medium | Monitor the distribution of churned and non-churned customers and use suitable evaluation metrics. |
| Incorrect data values | Medium | Check missing values, duplicates, invalid values, and outliers before training. |