import pandas as pd
import numpy as np
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset, DataLoader
from dataset_utils import describe_split, describe_batch


class CreditDataset(Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]


np.random.seed(42)

df = pd.DataFrame({
    "income": np.random.randint(25000, 100000, size=20),
    "age": np.random.randint(21, 60, size=20),
    "loan_amount": np.random.randint(3000, 25000, size=20),
    "late_payments": np.random.randint(0, 6, size=20),
    "default": np.random.randint(0, 2, size=20)
})

X = df[["income", "age", "loan_amount", "late_payments"]]
y = df["default"]

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.4, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
X_val_tensor = torch.tensor(X_val.values, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test.values, dtype=torch.float32)

y_train_tensor = torch.tensor(y_train.values, dtype=torch.long)
y_val_tensor = torch.tensor(y_val.values, dtype=torch.long)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.long)

describe_split("Train", X_train_tensor, y_train_tensor)
describe_split("Validation", X_val_tensor, y_val_tensor)
describe_split("Test", X_test_tensor, y_test_tensor)

train_dataset = CreditDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)

for batch_X, batch_y in train_loader:
    describe_batch(batch_X, batch_y)
    break