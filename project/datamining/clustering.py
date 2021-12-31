from re import I
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering


class Cluster:
    def __init__(self, data=None):
        self.data = data

    def categorical_to_numerical(self, data):
        s = (data.dtypes == 'object')
        object_cols = list(s[s].index)
        # Use encoder for categorical datatypes
        encoder = LabelEncoder()
        for i in object_cols:
            data[i] = data[[i]].apply(encoder.fit_transform)
        return data

    def scaler_values(self, data):
        scaler = StandardScaler()
        scaler.fit(data)
        scaled_data = pd.DataFrame(
            scaler.transform(data), columns=data.columns)
        return scaled_data

    def get_clustering(self, targets, n_clusters):
        # Remove columns
        data = self.data.filter(targets, axis=1)
        data = self.categorical_to_numerical(data)
        data = self.scaler_values(data)
        # Initiating the Agglomerative Clustering model
        agg_cluster = AgglomerativeClustering(n_clusters=n_clusters)
        # fit model and predict clusters
        cluster_values = agg_cluster.fit_predict(data)
        self.data["clusters"] = cluster_values
        clusters = self.__prepare_output_clusters()
        return clusters

    def __prepare_output_clusters(self):
        """Helper for return an object with values from clusters"""
        clusters = self.data['clusters'].unique().tolist()
        clusters.sort()
        output = {"clusters_name": clusters, "clusters": []}
        # For each cluster create a dataframe
        df_clusters = []
        for clu in clusters:
            df_cluster = self.data[self.data['clusters'] == clu]
            df_clusters.append(df_cluster)
        # Create an object whit totals and averages from variables
        for clu in clusters:
            data = df_clusters[clu]
            data_cluster = {
                "name": clu,
                # "data": data,
                "total_elements": len(data.index),
                "count_values": [
                    {"gender": data["gender"].value_counts().to_dict()},
                    {"feeling": data["feeling"].value_counts().to_dict()}
                ],
                "average_values": [
                    {"reactions": data["reactions"].mean()}
                ]
            }
            output['clusters'].append(data_cluster)

        return output


if __name__ == "__main__":
    import json
    path = 'project/static/04 Datos Limpios.xlsx'
    df = pd.read_excel(path, sheet_name='Comments')
    clu = Cluster(df)
    clusters = clu.get_clustering(['feeling', 'reactions'], 4)
    print(json.dumps(clusters, sort_keys=False, indent=2))
