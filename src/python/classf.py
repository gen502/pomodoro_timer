import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class PostureClassifier:
    def __init__(self, n_estimators=100, random_state=42):
        self.clf = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)

    def train(self, filename):
        with open(filename, 'r') as file:
            data = []
            self.y = []
            reader = csv.reader(file)
            for row in reader:
                data.append(row[1:7] + row[71:84])
                self.y.append(int(row[0]))

        self.X = []
        for sub_list in data:
            rounded_list = [round(float(num), 2) for num in sub_list]
            self.X.append(rounded_list)

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.1, random_state=42)
        self.clf.fit(X_train, y_train)

        y_pred = self.clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

    def predict(self, filename):
        with open(filename, 'r') as file:
            data = []
            reader = csv.reader(file)
            for row in reader:
                data.append(row[1:7] + row[71:84])

        X = []
        for sub_list in data:
            rounded_list = [round(float(num), 2) for num in sub_list]
            X.append(rounded_list)

        y_pred = self.clf.predict(X)
        return y_pred






