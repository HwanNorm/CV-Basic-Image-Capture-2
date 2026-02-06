import cv2


class MedianBlurProcessor:
    def __init__(self):
        pass

    # =============================================================================
    # STEP 3: MEDIAN BLUR (Week 2)
    # Topic: Image Filtering - Noise Reduction
    # =============================================================================

    def apply_median_blur(self, img, kernel_size=31):
        """
        Apply Median blur to reduce salt-and-pepper noise

        Args:
            img: Input image (numpy array)
            kernel_size: Size of the kernel, must be odd (e.g., 3, 5, 7)

        Returns:
            Blurred image
        """
        if img is None:
            return None

        # Apply Median Blur
        blurred_img = cv2.medianBlur(img, kernel_size)
        return blurred_img
