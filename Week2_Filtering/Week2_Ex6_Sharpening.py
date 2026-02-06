import cv2
import numpy as np


class SharpeningProcessor:
    def __init__(self):
        pass

    # =============================================================================
    # STEP 6: SHARPENING FILTER (Week 2)
    # Topic: Image Filtering - Image Enhancement
    # =============================================================================

    def apply_sharpening(self, img):
        """
        Apply sharpening filter to enhance edges and details

        Args:
            img: Input image (numpy array)

        Returns:
            Sharpened image
        """
        if img is None:
            return None

        # Sharpening kernel
        sharpening_kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        # Apply sharpening filter using filter2D
        sharpened_img = cv2.filter2D(img, -1, sharpening_kernel)

        return sharpened_img
