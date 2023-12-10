from main import summary, visualize
import matplotlib.pyplot as plt
import pandas as pd

"Testing main.py"

df=pd.read_csv('iris.csv')

def test_describe():
    desc_stats = summary(df)
    assert desc_stats['sepal.length']['mean']==5.843333333333334

def test_visualize():
    test_plot = visualize(df)
    assert test_plot == "displayed successfully"


if __name__ == "__main__":
    test_describe()
    test_visualize()