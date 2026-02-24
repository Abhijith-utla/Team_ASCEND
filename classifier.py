import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

train = pd.read_csv('variant_scoring_train.csv')
test = pd.read_csv('variant_scoring_test.csv')

threshold = train['reward_delta'].quantile(0.7)
train['useful'] = (train['reward_delta'] > threshold).astype(int)
test['useful'] = (test['reward_delta'] > threshold).astype(int)

X_train = train[['variant_length', 'ast_depth', 'edit_distance', 'partial_pass_rate']]
y_train = train['useful']

X_test = test[['variant_length', 'ast_depth', 'edit_distance', 'partial_pass_rate']]
y_test = test['useful']

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

preds = model.predict(X_test)

print(classification_report(y_test, preds))