from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str
@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    validation_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str

@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str

@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str

# -------------------- Summary Notes --------------------

# ✅ This class is used to store the output of the data ingestion step.

# ✅ It keeps track of:
#    - trained_file_path: location of the training dataset file
#    - test_file_path: location of the testing dataset file

# ✅ Since it's a @dataclass, we don't need to write an __init__ method — it’s created automatically!

# ✅ The idea is to pass around this object between different pipeline steps easily.

# ✅ This helps keep code clean and makes debugging and logging easier.
