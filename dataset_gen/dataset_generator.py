from sklearn.datasets import make_classification

class DatasetGenerator():
    def __init__(self, dict_params):
        self.params = dict_params
        self.catalog = None
        
        # Set possible values for each parameter as instance attributes
        self.possible_shape_of_border = list(self.params.get("shape_of_border", {}).keys())
        self.possible_overlap = list(self.params.get("level_of_overlap", {}).keys())
        self.possible_dataset_size = list(self.params.get("dataset_size", {}).keys())
        self.possible_balance = list(self.params.get("classes_balance", {}).keys())
        self.possible_noise = list(self.params.get("noise_of_classes", {}).keys())
    
    
    def generate_dataset(self, shape_of_border, n_classes, overlap, dataset_size, balance, noise) -> tuple:
        # Get variable parameters from mappings
        dict_shape_of_border = self.params.get("shape_of_border", None)
        dict_overlap         = self.params.get("level_of_overlap", None)
        dict_dataset_size    = self.params.get("dataset_size", None)
        dict_balance         = self.params.get("classes_balance", None)
        dict_noise           = self.params.get("noise_of_classes", None)
        
        # Set fixed parameters
        n_features           = 2
        n_informative        = 2
        n_repeated           = 0
        n_redundant          = 0
        n_clusters_per_class = 1  # Number of clusters per class
        
        
        X, y = make_classification(
                    random_state            = dict_shape_of_border.get(shape_of_border),
                    n_samples               = dict_dataset_size.get(dataset_size),
                    weights                 = dict_balance.get(balance),
                    flip_y                  = dict_noise.get(noise),
                    class_sep               = dict_overlap.get(overlap),
                    n_classes               = n_classes,
                    n_features              = n_features,
                    n_informative           = n_informative,
                    n_redundant             = n_redundant,
                    n_repeated              = n_repeated,
                    n_clusters_per_class    = n_clusters_per_class
                    )
        return X, y
    
    def generate_id(self, shape_of_border, n_classes, overlap, dataset_size, balance, noise):
        concat_id = f"{shape_of_border}SHP_{n_classes}CLSS_{overlap}OVL_{dataset_size}SIZE_{balance}BAL_{noise}NOISE"
        return concat_id
    
    def generate_catalog(self):
        self.catalog = {}
        for shape_of_border in self.possible_shape_of_border:
            for overlap in self.possible_overlap:
                for dataset_size in self.possible_dataset_size:
                    for balance in self.possible_balance:
                        for noise in self.possible_noise:
                            for n_classes in [2, 3]:
                                id = self.generate_id(shape_of_border, n_classes, overlap, dataset_size, balance, noise)
                                self.catalog[id] = self.generate_dataset(shape_of_border, n_classes, overlap, dataset_size, balance, noise)
        return self.catalog