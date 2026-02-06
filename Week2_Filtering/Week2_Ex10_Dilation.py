import cv2
import numpy as np


class DilationProcessor:
    def __init__(self):
        pass

    # =============================================================================
    # STEP 10: DILATION - MORPHOLOGICAL FILTERING (Week 2)
    # Topic: Image Filtering - Morphological Operations
    # =============================================================================

    def apply_dilation(self, img, kernel_size=(5, 5), iterations=1):
        """
        Apply dilation to expand bright regions (foreground)

        Args:
            img: Input image (numpy array)
            kernel_size: Size of the structuring element
            iterations: Number of times dilation is applied

        Returns:
            Dilated image
        """
        if img is None:
            return None

        # Create structuring element (kernel)
        kernel = np.ones(kernel_size, np.uint8)

        # Apply dilation
        dilated_img = cv2.dilate(img, kernel, iterations=iterations)

        return dilated_img
