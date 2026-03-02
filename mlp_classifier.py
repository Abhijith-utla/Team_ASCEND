from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from extract_features import get_features
import torch
import torch.nn as nn
import torch.optim as optim

df = get_features()

print('\n===== DATASET SUMMARY =====')
print('Total samples:', len(df))
print('Class distribution:')
print(df['useful'].value_counts())
print('Class distribution (percent):')
print(df['useful'].value_counts(normalize=True))
print('===========================\n')

X = df.drop(columns=['useful']).values
y = df['useful'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)

X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

class VariantScorer(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)

model = VariantScorer(X_train.shape[1])
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print('\n===== MODEL ARCHITECTURE =====')
print(model)
print('Number of parameters:', sum(p.numel() for p in model.parameters()))
print('==============================\n')

for epoch in range(200):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

    if epoch % 20 == 0:
        print(f'Epoch {epoch:03d} | Loss: {loss.item():.4f}')

model.eval()
with torch.no_grad():
    probs = model(X_test)
    preds = (probs > 0.5).float()

    accuracy = (preds == y_test).float().mean()
    print('\n===== EVALUATION =====')
    print('Test Accuracy:', accuracy.item())

    auc = roc_auc_score(y_test.numpy(), probs.numpy())
    print('Test ROC AUC:', auc)
    print('======================\n')
print('Final training loss:', loss.item())