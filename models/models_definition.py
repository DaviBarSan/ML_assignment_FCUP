from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

class MLModels:
    def __init__(self):
        self.models = {
            "logistic_regression": LogisticRegression(),
            "lda": LinearDiscriminantAnalysis(),
            "qda": QuadraticDiscriminantAnalysis(),
            "decision_tree_no_pruning": DecisionTreeClassifier(),
            "decision_tree_depth_2": DecisionTreeClassifier(max_depth=2),
            "svm_linear": SVC(kernel='linear'),
            "svm_rbf": SVC(kernel='rbf')
        }
    def list_models(self):
        print(self.models.keys())
    
    def get_model(self, model_name):
        return self.models.get(model_name, None)