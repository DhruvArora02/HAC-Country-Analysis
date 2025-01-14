import numpy as np

def hac(feature_vectors):
    num_samples = len(feature_vectors)
    linkage_matrix = np.zeros((num_samples - 1, 4))
    cluster_map = {i: [i] for i in range(num_samples)}
    dist_matrix = np.full((2 * num_samples - 1, 2 * num_samples - 1), np.inf)
    
    for i in range(num_samples):
        for j in range(i + 1, num_samples):
            dist_matrix[i, j] = dist_matrix[j, i] = np.linalg.norm(feature_vectors[i] - feature_vectors[j])
    
    current_cluster_id = num_samples
    for step in range(num_samples - 1):
        cluster_indices = list(cluster_map.keys())
        pairwise_distances = dist_matrix[np.ix_(cluster_indices, cluster_indices)]
        np.fill_diagonal(pairwise_distances, np.inf)
        min_distance = np.min(pairwise_distances)
        min_x, min_y = np.where(pairwise_distances == min_distance)
        
        merge_candidates = []
        for x, y in zip(min_x, min_y):
            if x != y:
                candidate_i = cluster_indices[x]
                candidate_j = cluster_indices[y]
                merge_candidates.append((min(candidate_i, candidate_j), max(candidate_i, candidate_j)))
        
        merge_candidates = list(set(merge_candidates))
        merge_candidates.sort()
        
        cluster_i, cluster_j = merge_candidates[0]
        linkage_matrix[step] = [cluster_i, cluster_j, dist_matrix[cluster_i, cluster_j], len(cluster_map[cluster_i]) + len(cluster_map[cluster_j])]
        
        cluster_map[current_cluster_id] = cluster_map[cluster_i] + cluster_map[cluster_j]
        del cluster_map[cluster_i], cluster_map[cluster_j]
        
        for cluster_k in cluster_map.keys():
            if cluster_k != current_cluster_id:
                dist_matrix[current_cluster_id, cluster_k] = dist_matrix[cluster_k, current_cluster_id] = min(dist_matrix[cluster_i, cluster_k], dist_matrix[cluster_j, cluster_k])
        
        dist_matrix[cluster_i, :] = dist_matrix[:, cluster_i] = np.inf
        dist_matrix[cluster_j, :] = dist_matrix[:, cluster_j] = np.inf
        current_cluster_id += 1
    
    return linkage_matrix
