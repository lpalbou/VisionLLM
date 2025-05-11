"""
Tests for the VisionManager class.
"""

import unittest
from visionllm import VisionManager


class TestVisionManager(unittest.TestCase):
    """Test cases for the VisionManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.vision_manager = VisionManager(debug_mode=True)
    
    def tearDown(self):
        """Tear down test fixtures."""
        self.vision_manager.cleanup()
    
    def test_initialization(self):
        """Test that the VisionManager initializes correctly."""
        self.assertIsNotNone(self.vision_manager)
        self.assertTrue(self.vision_manager.debug_mode)
        self.assertFalse(self.vision_manager.is_processing())
    
    def test_text_to_image(self):
        """Test the text_to_image method."""
        prompt = "A test prompt"
        result = self.vision_manager.text_to_image(prompt)
        # In the current implementation, this returns None
        self.assertIsNone(result)
        self.assertFalse(self.vision_manager.is_processing())
    
    def test_image_to_image(self):
        """Test the image_to_image method."""
        # This is a placeholder test since we don't have actual image processing yet
        result = self.vision_manager.image_to_image(None, prompt="A test prompt")
        self.assertIsNone(result)
        self.assertFalse(self.vision_manager.is_processing())
    
    def test_text_to_video(self):
        """Test the text_to_video method."""
        prompt = "A test prompt"
        result = self.vision_manager.text_to_video(prompt)
        self.assertIsNone(result)
        self.assertFalse(self.vision_manager.is_processing())
    
    def test_image_to_video(self):
        """Test the image_to_video method."""
        # This is a placeholder test since we don't have actual video processing yet
        result = self.vision_manager.image_to_video(None, prompt="A test prompt")
        self.assertIsNone(result)
        self.assertFalse(self.vision_manager.is_processing())
    
    def test_stop_processing(self):
        """Test the stop_processing method."""
        # Set processing to True manually for testing
        self.vision_manager._processing = True
        self.assertTrue(self.vision_manager.is_processing())
        
        # Stop processing
        result = self.vision_manager.stop_processing()
        self.assertTrue(result)
        self.assertFalse(self.vision_manager.is_processing())


if __name__ == "__main__":
    unittest.main() 