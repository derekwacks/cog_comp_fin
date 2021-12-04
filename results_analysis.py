"""
results_analysis.py
"""

import numpy as np
import pandas as pd

def compute_means():
    path1 = "paper/Results/5_runs_mask_train_mask_test/5_runs_mask_train_mask_test.tsv"
    path2 = "paper/Results/5_runs_mask_train_nomask_test/5_runs_mask_train_nomask_test.tsv"
    path3 = "paper/Results/5_runs_nomask_train_mask_test/5_runs_nomask_train_mask_test.csv"
    path4 = "paper/Results/5_runs_nomask_train_nomask_test/5_runs_nomask_train_nomask_test.csv"

    df1 = pd.read_csv(path1, sep="\t")
    df2 = pd.read_csv(path2, sep="\t")
    df3 = pd.read_csv(path3, sep=",")
    df4 = pd.read_csv(path4, sep=",")

    sets = ["masked training-masked testing", "masked training-unmasked testing",
            "unmasked training-masked testing", "unmasked training-unmasked testing"]
    means = [df1["#PctCor"].mean(), df2["#PctCor"].mean(),
             df3["#PctCor"].mean(), df4["#PctCor"].mean()]

    np_array_means = np.array(means)
    means = np.around(np_array_means, 5)  # rounding to 5 digits

    dat = {}
    dat["Training/Testing sets"] = sets
    dat["Percent correct mean"] = means
    column_names = ["Training/Testing sets", "Percent correct mean"]
    dataframe = pd.DataFrame(columns=column_names, data=dat)
    write_csv(dataframe)
    return

def write_csv(data):
    """
    :param data: dataframe
    :return:
    """
    name = "paper/Results/pct_corr_means.csv"
    data.to_csv(name, index=False, sep=',')
    return


if __name__ == '__main__':
    compute_means()