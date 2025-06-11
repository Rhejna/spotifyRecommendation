import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

def get_custom_recommendations(sp, seed_track_id, num_recommendations=10):
    """Generate custom recommendations based on audio features"""
    # Get seed track features
    seed_features = sp.audio_features([seed_track_id])[0]
    
    # Get user's top tracks as candidate pool
    top_tracks = sp.current_user_top_tracks(limit=50, time_range='short_term')
    candidate_ids = [t['id'] for t in top_tracks['items']]
    
    # Remove seed if present
    candidate_ids = [tid for tid in candidate_ids if tid != seed_track_id]
    
    # Get audio features for candidates
    candidate_features = sp.audio_features(candidate_ids)
    
    # Prepare feature matrix
    feature_keys = ['danceability', 'energy', 'valence', 
                   'acousticness', 'instrumentalness', 
                   'liveness', 'speechiness', 'tempo']
    
    seed_vector = np.array([seed_features[k] for k in feature_keys]).reshape(1, -1)
    candidate_matrix = np.array([[f[k] for k in feature_keys] for f in candidate_features])
    
    # Normalize features
    scaler = StandardScaler()
    scaled_candidates = scaler.fit_transform(candidate_matrix)
    scaled_seed = scaler.transform(seed_vector)
    
    # Calculate similarities
    similarities = cosine_similarity(scaled_seed, scaled_candidates)[0]
    
    # Get top recommendations
    top_indices = np.argsort(similarities)[::-1][:num_recommendations]
    return [candidate_ids[i] for i in top_indices]

