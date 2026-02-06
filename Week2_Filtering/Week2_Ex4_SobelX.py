import cv2
import numpy as np


class SobelXProcessor:
    def __init__(self):
        pass

    # =============================================================================
    # STEP 4: SOBEL EDGE DETECTION - X DIRECTION (Week 2)
    # Topic: Image Filtering - Edge Detection
    # =============================================================================

    def apply_sobel_x(self, img, ksize=3):
        """
        Apply Sobel edge detection in X direction to detect vertical edges

        Args:
            img: Input image (numpy array)
            ksize: Size of the Sobel kernel (1, 3, 5, or 7)

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

        # Apply Sobel in X direction
        sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=ksize)

        # Convert to absolute values and uint8
        sobel_x_abs = np.uint8(np.absolute(sobel_x))

        return sobel_x_abs
