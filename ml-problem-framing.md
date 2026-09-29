# ML Problem Framing

## Decision

The business wants to identify customers who are at risk of churn so that
timely customer retention actions can be considered.

The model output should support human decision-making and should not be the
only factor used for retention decisions.

## Prediction target

The prediction target is `churned`.

- `1` = customer churned
- `0` = customer did not churn

The model predicts whether a customer is likely to churn based on the
available customer information.

## Unit of observation

The unit of observation is one customer record.

Each row in the dataset represents an individual customer.

## Action window

The prediction should be made early enough to allow the business to take
timely retention action before the customer leaves.

The exact operational action window is not specified in the available
dataset.

## Non-ML baseline

A simple rule-based baseline is used instead of a machine-learning model.

A customer is predicted as likely to churn when:

- `last_login_days >= 15`, OR
- `support_tickets >= 3`

Otherwise, the customer is predicted as not likely to churn.

This baseline provides a simple reference point for evaluating future
machine-learning models.

## Success metrics

The baseline and future models should be evaluated using:

- Accuracy
- Precision
- Recall

Recall is important because missing a customer who is actually at risk of
churn can reduce the opportunity for timely retention action.

Precision is also important because unnecessary retention actions can waste
business resources.