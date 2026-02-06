import cv2
import numpy as np


class LaplacianProcessor:
    def __init__(self):
        pass

    # =============================================================================
    # STEP 5: LAPLACIAN EDGE DETECTION (Week 2)
    # Topic: Image Filtering - Edge Detection
    # =============================================================================

    def apply_laplacian(self, img, ksize=3):
        """
        Apply Laplacian edge detection to detect edges in all directions

        Args:
            img: Input image (numpy array)
            ksize: Aperture size for the Sobel operator (must be positive and odd)

        Returns:
            Edge detected image (absolute values, uint8)
        """
        if img is None:
            return None

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray_img = img

        # Apply Laplacian
        laplacian = cv2.Laplacian(gray_img, cv2.CV_64F, ksize=ksize)

        # Convert to absolute values and uint8
        laplacian_abs = np.uint8(np.absolute(laplacian))

        return laplacian_abs
