# Baseline model for customer churn prediction
# Pure Python version - no sklearn/scipy required

import csv

# Load dataset
with open("customer-churn-training.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Simple baseline rule:
# Customer is predicted as churned if:
# last_login_days >= 15 OR support_tickets >= 3

y_true = []
y_pred = []

for row in data:
    actual = int(row["churned"])

    last_login_days = int(row["last_login_days"])
    support_tickets = int(row["support_tickets"])

    if last_login_days >= 15 or support_tickets >= 3:
        predicted = 1
    else:
        predicted = 0

    y_true.append(actual)
    y_pred.append(predicted)

# Calculate metrics
correct = 0
true_positive = 0
false_positive = 0
false_negative = 0

for actual, predicted in zip(y_true, y_pred):

    if actual == predicted:
        correct += 1

    if predicted == 1 and actual == 1:
        true_positive += 1

    if predicted == 1 and actual == 0:
        false_positive += 1

    if predicted == 0 and actual == 1:
        false_negative += 1

accuracy = correct / len(y_true)

if true_positive + false_positive == 0:
    precision = 0
else:
    precision = true_positive / (true_positive + false_positive)

if true_positive + false_negative == 0:
    recall = 0
else:
    recall = true_positive / (true_positive + false_negative)

print("Baseline Customer Churn Model")
print("-----------------------------")
print(f"Accuracy : {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall   : {recall:.2f}")