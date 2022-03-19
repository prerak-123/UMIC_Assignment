import numpy as np

def theta_matrix(y = np.random.randint(0, 10, size=20, dtype='int32')):
    
    X = np.random.normal(size = (20,20))
    X_t = np.transpose(X)
    
    theta_matrix = np.linalg.inv((X_t @ X)) @ X_t @ y
    print(theta_matrix)
    
    return theta_matrix
    
theta_matrix()