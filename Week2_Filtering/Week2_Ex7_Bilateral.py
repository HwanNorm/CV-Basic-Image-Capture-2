import cv2


class BilateralProcessor:
    def __init__(self):
        pass

    # =============================================================================
    # STEP 7: BILATERAL FILTER (Week 2)
    # Topic: Image Filtering - Edge-Preserving Smoothing
    # =============================================================================

    def apply_bilateral(self, img, d=15, sigma_color=150, sigma_space=150):
        """
        Apply bilateral filter to smooth while preserving edges

        Args:
            img: Input image (numpy array)
            d: Diameter of each pixel neighborhood
            sigma_color: Filter sigma in the color space
            sigma_space: Filter sigma in the coordinate space

        Returns:
            Filtered image
        """
        if img is None:
            return None

        # Apply Bilateral Filter
        bilateral_img = cv2.bilateralFilter(img, d, sigma_color, sigma_space)

        return bilateral_img
