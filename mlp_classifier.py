from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from extract_features import get_features
import torch
import torch.nn as nn
import torch.optim as optim

# ==============================
# MODEL DEFINITION
# ==============================
class VariantScorer(nn.Module):
    def __init__(self, input_dim):
        super().__init__()

        # Simple feedforward neural network
        self.net = nn.Sequential(
            nn.Linear(input_dim, 32),  # input → hidden layer
            nn.ReLU(),
            nn.Linear(32, 16),         # hidden → smaller hidden
            nn.ReLU(),
            nn.Linear(16, 1),          # output layer
            nn.Sigmoid()               # convert to probability (0–1)
        )

    def forward(self, x):
        return self.net(x)


# ==============================
# TRAINING FUNCTION
# ==============================
def train_mlp(df, epochs=200, lr=0.001):
    """
    Trains the MLP model on the given dataframe.

    Returns:
        model   : trained neural network
        scaler  : fitted StandardScaler (needed for inference)
        test_data : (X_test, y_test) tensors for evaluation
    """

    # Split features and labels
    X = df.drop(columns=['useful']).values
    y = df['useful'].values

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    # Normalize features (VERY important for neural nets)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Convert to PyTorch tensors
    X_train = torch.tensor(X_train, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)

    X_test = torch.tensor(X_test, dtype=torch.float32)
    y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

    # Initialize model
    model = VariantScorer(X_train.shape[1])

    # Loss + optimizer
    criterion = nn.BCELoss()  # binary classification loss
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # Training loop
    for epoch in range(epochs):
        model.train()

        optimizer.zero_grad()               # reset gradients
        outputs = model(X_train)            # forward pass
        loss = criterion(outputs, y_train)  # compute error
        loss.backward()                     # backpropagation
        optimizer.step()                    # update weights

        if epoch % 20 == 0:
            print(f'Epoch {epoch:03d} | Loss: {loss.item():.4f}')

    return model, scaler, (X_test, y_test)


# ==============================
# EVALUATION FUNCTION
# ==============================
def evaluate_model(model, X_test, y_test):
    """
    Evaluates model performance.

    Returns:
        accuracy : classification accuracy
        auc      : ROC AUC score
    """

    model.eval()

    with torch.no_grad():
        probs = model(X_test)                 # predicted probabilities
        preds = (probs > 0.5).float()         # convert to 0/1

        accuracy = (preds == y_test).float().mean().item()
        auc = roc_auc_score(y_test.numpy(), probs.numpy())

    return accuracy, auc


# ==============================
# PREDICTION FUNCTION (FOR PIPELINE USE)
# ==============================
def predict(model, scaler, X_raw):
    """
    Makes predictions on new raw feature data.

    Args:
        model  : trained model
        scaler : fitted scaler
        X_raw  : raw feature array (not normalized)

    Returns:
        probs  : probabilities
        preds  : binary predictions
    """

    X_scaled = scaler.transform(X_raw)
    X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

    model.eval()
    with torch.no_grad():
        probs = model(X_tensor)
        preds = (probs > 0.5).float()

    return probs.numpy(), preds.numpy()


# ==============================
# FULL PIPELINE FUNCTION
# ==============================
def run_pipeline():
    """
    End-to-end pipeline:
    - load features
    - train model
    - evaluate model

    Returns:
        dict with model + metrics
    """

    df = get_features()

    print('\n===== DATASET SUMMARY =====')
    print('Total samples:', len(df))
    print(df['useful'].value_counts())
    print('===========================\n')

    model, scaler, (X_test, y_test) = train_mlp(df)

    accuracy, auc = evaluate_model(model, X_test, y_test)

    print('\n===== EVALUATION =====')
    print('Accuracy:', accuracy)
    print('ROC AUC:', auc)
    print('======================\n')

    return {
        'model': model,
        'scaler': scaler,
        'accuracy': accuracy,
        'auc': auc
    }

# ==============================
# MAIN (ONLY RUNS IF FILE EXECUTED DIRECTLY)
# ==============================
if __name__ == "__main__":
    results = run_pipeline()