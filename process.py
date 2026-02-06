import time
import cv2
import numpy as np
import os
from Week1_Capturering.Week1_captureSaveImg import CaptureSaveImgProcessor

# Import all 10 filters
from Week2_Filtering.Week2_Ex1_Grayscale import GrayscaleProcessor
from Week2_Filtering.Week2_Ex2_Gaussian import GaussianProcessor
from Week2_Filtering.Week2_Ex3_MedianBlur import MedianBlurProcessor
from Week2_Filtering.Week2_Ex4_SobelX import SobelXProcessor
from Week2_Filtering.Week2_Ex5_Laplacian import LaplacianProcessor
from Week2_Filtering.Week2_Ex6_Sharpening import SharpeningProcessor
from Week2_Filtering.Week2_Ex7_Bilateral import BilateralProcessor
from Week2_Filtering.Week2_Ex8_Threshold import ThresholdProcessor
from Week2_Filtering.Week2_Ex9_Erosion import ErosionProcessor
from Week2_Filtering.Week2_Ex10_Dilation import DilationProcessor

# =============================================================================
# CHANGE THIS TO TEST DIFFERENT FILTERS (1-10)
# =============================================================================
CURRENT_FILTER = 10  # Change this number to test different filters
# 1 = Grayscale
# 2 = Gaussian Blur
# 3 = Median Blur
# 4 = Sobel X Edge Detection
# 5 = Laplacian Edge Detection
# 6 = Sharpening
# 7 = Bilateral Filter
# 8 = Threshold (Binary)
# 9 = Erosion
# 10 = Dilation
# =============================================================================


class ImageProcessor:
    """
    Class for processing images from camera feed
    Implements computer vision techniques from ProjectProgress.txt
    """

    def __init__(self):
        """Initialize image processor with calibration parameters"""
        self.camera_matrix = None  # Camera calibration matrix
        self.dist_coeffs = None    # Distortion coefficients
        self.homography_matrix = None  # Homography transformation matrix
        self.previous_frame = None  # For motion detection
        self.tracked_objects = []   # For object tracking

        # Initialize all filter processors
        self.grayscale = GrayscaleProcessor()
        self.gaussian = GaussianProcessor()
        self.median = MedianBlurProcessor()
        self.sobel_x = SobelXProcessor()
        self.laplacian = LaplacianProcessor()
        self.sharpening = SharpeningProcessor()
        self.bilateral = BilateralProcessor()
        self.threshold = ThresholdProcessor()
        self.erosion = ErosionProcessor()
        self.dilation = DilationProcessor()


    # =============================================================================
    # STEP 10: SYSTEM INTEGRATION (Week 14)
    # Topic: All Course Concepts
    # =============================================================================

    def process_frame(self, bgr_img):

        if bgr_img is None:
            raise ValueError("Input frame is None")

        start_time = time.perf_counter()
        results = {}

        ###################### WRITE YOUR PROCESS PIPELINE HERE #########################
        saveImg = CaptureSaveImgProcessor()

        # Step 1: Capture and Save Original Image
        step1_image = saveImg.capture_and_save_image(bgr_img, "test_capture.bmp")

        ######################## IMAGE FILTERING ########################################
        # Apply filter based on CURRENT_FILTER setting
        filter_names = {
            1: "Grayscale",
            2: "Gaussian Blur",
            3: "Median Blur",
            4: "Sobel X Edge",
            5: "Laplacian Edge",
            6: "Sharpening",
            7: "Bilateral",
            8: "Threshold",
            9: "Erosion",
            10: "Dilation"
        }

        if CURRENT_FILTER == 1:
            processed_img = self.grayscale.convert_to_grayscale(bgr_img)
        elif CURRENT_FILTER == 2:
            processed_img = self.gaussian.apply_gaussian_filter(bgr_img)
        elif CURRENT_FILTER == 3:
            processed_img = self.median.apply_median_blur(bgr_img)
        elif CURRENT_FILTER == 4:
            processed_img = self.sobel_x.apply_sobel_x(bgr_img)
        elif CURRENT_FILTER == 5:
            processed_img = self.laplacian.apply_laplacian(bgr_img)
        elif CURRENT_FILTER == 6:
            processed_img = self.sharpening.apply_sharpening(bgr_img)
        elif CURRENT_FILTER == 7:
            processed_img = self.bilateral.apply_bilateral(bgr_img)
        elif CURRENT_FILTER == 8:
            processed_img = self.threshold.apply_threshold(bgr_img)
        elif CURRENT_FILTER == 9:
            processed_img = self.erosion.apply_erosion(bgr_img)
        elif CURRENT_FILTER == 10:
            processed_img = self.dilation.apply_dilation(bgr_img)
        else:
            processed_img = self.grayscale.convert_to_grayscale(bgr_img)

        results['filter_name'] = filter_names.get(CURRENT_FILTER, "Unknown")
        results['filter_number'] = CURRENT_FILTER

        # Save Processed Image
        saveImg.capture_and_save_image(processed_img, "processed_capture.bmp")
        #################################################################################

        process_time_ms = (time.perf_counter() - start_time) * 1000
        return processed_img, results, process_time_ms
    
    def visualize_results(self, bgr_img, results):
        """
        Visualize all processing results on image
        
        Args:
            bgr_img: Original image
            results: Dictionary of results from process_frame
            
        Returns:
            Annotated image
        """

        pass
