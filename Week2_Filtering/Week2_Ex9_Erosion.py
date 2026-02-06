import cv2
import numpy as np


class ErosionProcessor:
    def __init__(self):
        pass

    # =============================================================================
    # STEP 9: EROSION - MORPHOLOGICAL FILTERING (Week 2)
    # Topic: Image Filtering - Morphological Operations
    # =============================================================================

    def apply_erosion(self, img, kernel_size=(5, 5), iterations=1):
        """
        Apply erosion to shrink bright regions (foreground)

        Args:
            img: Input image (numpy array)
            kernel_size: Size of the structuring element
            iterations: Number of times erosion is applied

        Returns:
            Eroded image
        """
        if img is None:
            return None

        # Create structuring element (kernel)
        kernel = np.ones(kernel_size, np.uint8)

        # Apply erosion
        eroded_img = cv2.erode(img, kernel, iterations=iterations)

        return eroded_img
