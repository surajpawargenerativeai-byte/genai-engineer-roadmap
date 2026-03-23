import pandas as pd
import torch
from sklearn.model_selection import train_test_split

data = {
    "income": [50000, 30000, 90000, 45000, 70000, 25000, 80000, 52000],
    "age": [29, 45, 35, 50, 31, 40, 28, 38],
    "loan_amount": [10000, 15000, 5000, 12000, 7000, 20000, 6000, 11000],
    "default": [0, 1, 0, 1, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

X = df[["income", "age", "loan_amount"]]
y = df["default"]

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.4, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.long)

print("X_train_tensor:")
print(X_train_tensor)
print("Shape:", X_train_tensor.shape)

print("\ny_train_tensor:")
print(y_train_tensor)
print("Shape:", y_train_tensor.shape)