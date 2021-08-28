# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:56:28 2021

@author: Smegn
"""

import pandas as pd

import plotly.express as px
import plotly.io as pio
import seaborn as sns
import matplotlib.pyplot as plt




class VisualizeFeature():

    def __init__(self):
        pass

    def histplot(df,x,y,title,hue=None,palette='Set2',w_size=12,h_size=7,size=None):
        plt.figure(figsize=(w_size, h_size))
        sns.distplot(data=df,x=x,y=y,hue=hue,palette=palette,size=size)
        plt.title(title)
        plt.show()
    def scatterplot(df,x,y,title,hue=None,style=None,w_size=12,h_size=7,size=None):
        plt.figure(figsize=(w_size, h_size))
        sns.scatterplot(data=df, x=x, y=y, hue=hue, style=style,size=size)
        plt.title(title,fontsize=23)
        plt.show()
    def correlation_heatmap(corr,title):
        plt.figure(figsize=(20, 10))
        ax = sns.heatmap(
        corr, 
        annot=True, cmap="coolwarm"
    )
        plt.title("Correlation Map of"+title)
        ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
   )
    def lineplot(df,x=None,y=None,title=None,w_size=12,h_size=7,size=None):
        plt.figure(figsize=(w_size, h_size))
        sns.lineplot(data=df, x=x, y=y,size=size)
        plt.title(title)
        plt.show()


    def barplot(self,df:pd.DataFrame,column:str, title:str):
        fig = px.bar(df.drop('column',axis=1).corrwith(df.column),title = title)

        fig.show()
#df = pd.read_csv(r'C:/Users/Smegn/Documents/GitHub/Breast-Cancer/data/data.csv')
#column='diagnosis'
#viz = VisualizeFeature()
#viz.barplot(df,column,'barplot')
