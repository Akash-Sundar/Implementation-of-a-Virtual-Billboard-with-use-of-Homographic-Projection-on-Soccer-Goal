import numpy as np
from est_homography import est_homography

def warp_pts(X, X_prime, interior_pts):
    """
    First compute homography from video_pts to logo_pts using X and X_prime,
    and then use this homography to warp all points inside the soccer goal

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
        interior_pts: Nx2 matrix of points inside goal
    Returns:
        warped_pts: Nx2 matrix containing new coordinates for interior_pts.
        These coordinate describe where a point inside the goal will be warped
        to inside the penn logo. For this assignment, you can keep these new
        coordinates as float numbers.

    """

    # You should Complete est_homography first!
    ##### STUDENT CODE START #####
  
    H = est_homography(X, X_prime)

    #lambda*X_logo = H*X_video

    homogenous_term = np.ones([interior_pts.shape[0],1])
    interior_pts = np.append(interior_pts,homogenous_term, axis = 1)

    warped_pts = np.zeros(interior_pts.shape)

    for i in range(0,interior_pts.shape[0]):
      warped_pts[i] = np.dot(H, interior_pts[i])
    
    warped_pts[:,0] = warped_pts[:,0]/warped_pts[:,2]
    warped_pts[:,1] = warped_pts[:,1]/warped_pts[:,2]

    warped_pts = warped_pts[:,[0,1]]

    ##### STUDENT CODE END #####

    return warped_pts
