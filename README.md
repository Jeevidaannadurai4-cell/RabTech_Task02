# Customer Churn Prediction using Machine Learning

## Project Overview

This project develops a baseline machine learning model to predict customer churn.

The model uses customer information such as:
- Tenure
- Support tickets
- Monthly spending
- Last login days
- Plan type

## Objective

The objective is to identify customers who are likely to churn so that appropriate retention actions can be considered.

## Machine Learning Model

A Logistic Regression model is used as the baseline classification model.

The dataset is divided into training and testing sets. Categorical data such as plan type is converted using One-Hot Encoding.

## Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall

Recall is important because missing a customer who is actually at risk can reduce the opportunity for timely retention action.

Precision is also considered because unnecessary retention actions can waste business resources.

## Responsible AI Considerations

The project considers:

- Dataset bias
- Data privacy
- Data leakage
- Class imbalance
- False positives
- False negatives
- Incorrect data values

Human review should be considered before taking customer retention actions.

## Risk Management

Potential risks and safeguards are documented in `risk-register.md`.

The responsible data considerations are documented in `responsible-data-card-template.md`.

## Files

- `baseline_model.py` – Baseline churn prediction model
- `customer-churn-training.csv` – Training dataset
- `ml-problem-framing.md` – Problem definition and framing
- `responsible-data-card-template.md` – Responsible AI documentation
- `risk-register.md` – Risk register
- `image.png` – Project-related image

## Conclusion

This project demonstrates a simple baseline approach for customer churn prediction while considering model evaluation, responsible data use, privacy, and potential risks.
