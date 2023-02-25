from typing import List
import matplotlib.pyplot as plt
import numpy as np
# class ThresholdClassifier:
#     def __init__(self, threshold: float):
#         self.threshold = threshold
#     def classify(self, data: List[float]):
#         self.mean = sum(data) / len(data)
#         self.threshold = self.mean
#         return [1 if x >= self.threshold else 0 for x in data]  
# classifier = ThresholdClassifier(0.5)

class ThresholdClassifier:
    def __init__(self, threshold: float):
        self.threshold = threshold
        
    def classify(self, data: List[float]):
        self.mean = sum(data) / len(data)
        self.threshold = self.mean
        classifications = []
        for value in data:
            if value > self.threshold:
                classifications.append(1)
            else:
                classifications.append(0)
        return classifications
    
classifier = ThresholdClassifier(0.5)

class ThresholdPlot:
    def __init__(self, data, classification):
        self.data = data
        self.classification = classification
        
    def plot(self):
        plt.style.use('dark_background')
        plt.figure(figsize=(15,6))
        plt.xlabel("Time", fontsize=14)
        plt.ylabel("Price (£)", color="tab:red", fontsize=14)
        plt.plot(self.data.index, self.data, color="tab:red")
        plt.twinx()
        plt.ylabel("Classification", color="tab:blue", fontsize=14)
        plt.plot(self.data.index, self.classification, color="tab:blue")
        plt.axhline(y=0.5, color="gray", linestyle="--")
        plt.title("Binary Classifications", fontsize=20, color="White")
        plt.show()

        colors = []
        for value in self.classification:
            if value > 0.5:
                colors.append("tab:green")
            else:
                colors.append("tab:red")

        plt.style.use('dark_background')
        plt.figure(figsize=(15,7))
        plt.xlabel("Time", fontsize=14)
        plt.ylabel("Price (£)", color="tab:red", fontsize=14)
        plt.plot(self.data.index, self.data, color="tab:red")
        plt.grid(linestyle="--", color="gray", alpha=0.7)
        plt.tick_params(axis="both", labelsize=12)
        plt.twinx()
        plt.ylabel("Classification", color="tab:blue", fontsize=14)
        plt.scatter(self.data.index, self.classification, color=colors)
        plt.tick_params(axis="both", labelsize=12)
        plt.title("Binary Classifications", fontsize=18, color="White")
        plt.show()



