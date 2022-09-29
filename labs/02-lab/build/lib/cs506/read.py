import pandas as pd
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    # raise NotImplementedError()
    df = pd.DataFrame(csv_file_path)
    
    matrix = df.to_numpy()
    return matrix