import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
import pandas as pd

# Load data
train = pd.read_csv('variant_scoring_train.csv')
test = pd.read_csv('variant_scoring_test.csv')

threshold = train['reward_delta'].quantile(0.7)
train['useful'] = (train['reward_delta'] > threshold).astype(int)
test['useful'] = (test['reward_delta'] > threshold).astype(int)

X_train = train[['variant_length','ast_depth','edit_distance','partial_pass_rate']].values
y_train = train['useful'].values

X_test = test[['variant_length','ast_depth','edit_distance','partial_pass_rate']].values
y_test = test['useful'].values

# Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)

X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

# Define MLP
class VariantScorer(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        return self.net(x)

model = VariantScorer()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train
for epoch in range(200):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

model.eval()
with torch.no_grad():
    probs = model(X_test).numpy()
    auc = roc_auc_score(y_test.numpy(), probs)
    print('ROC AUC:', auc)

print('Final training loss:', loss.item())