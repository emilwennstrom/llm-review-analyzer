import os
from langchain_google_vertexai import VertexAIEmbeddings
import faiss
import numpy as np

def cluster_reviews(review_column, translated = True, num_clusters = 10):
        '''
            Clustering texts based on semantic similarity.
            Returns a column of the cluster ids.
            Example usage: df['cluster_id'] = cluster_reviews(df['translated'], True, 10)
    
        '''
    
        # Init embedding model and create embeddings
        model_name = 'textembedding-gecko@003' if translated else 'textembedding-gecko-multilingual@001'
        embedding_model = VertexAIEmbeddings(model_name=model_name,project=os.getenv('PROJECT'),location=os.getenv('LOCATION'))
        embeddings = embedding_model.embed(texts=review_column.tolist(), embeddings_task_type='CLUSTERING')
        
        # Store embeddings
        embeddings_array = np.stack(embeddings)
        d = embeddings_array.shape[1]
        index = faiss.IndexFlatL2(d)
        embeddings_faiss = embeddings_array.astype(np.float32)
        index.add(embeddings_faiss)
        
        # Cluster reviews
        d = embeddings_faiss.shape[1]  # Dimension of the embeddings
        k = num_clusters
        kmeans = faiss.Kmeans(d, k, niter=400, verbose=True) # K-means clustering algoritm
        kmeans.train(embeddings_faiss)

        # Assigning the reviews to clusters
        D, I = kmeans.index.search(embeddings_faiss, 1)  # D is the distances, I is the indices of the clusters
        cluster_id_column = I.flatten() # Assign this to the data frame
        return cluster_id_column
        
        