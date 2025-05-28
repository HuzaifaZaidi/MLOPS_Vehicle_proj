from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str


# -------------------- Summary Notes --------------------

# ✅ This class is used to store the output of the data ingestion step.

# ✅ It keeps track of:
#    - trained_file_path: location of the training dataset file
#    - test_file_path: location of the testing dataset file

# ✅ Since it's a @dataclass, we don't need to write an __init__ method — it’s created automatically!

# ✅ The idea is to pass around this object between different pipeline steps easily.

# ✅ This helps keep code clean and makes debugging and logging easier.
