import cv2


class ThresholdProcessor:
    def __init__(self):
        pass

    # =============================================================================
    # STEP 8: THRESHOLDING - BINARY (Week 2)
    # Topic: Image Filtering - Image Segmentation
    # =============================================================================

    def apply_threshold(self, img, thresh_value=127, max_value=255):
        """
        Apply binary thresholding to convert image to black and white

        Args:
            img: Input image (numpy array)
            thresh_value: Threshold value (pixels above this become max_value)
            max_value: Value assigned to pixels above threshold

        Returns:
            Binary thresholded image
        """
        if img is None:
            return None

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray_img = img

        # Apply binary threshold
        _, thresh_img = cv2.threshold(gray_img, thresh_value, max_value, cv2.THRESH_BINARY)

        return thresh_img
