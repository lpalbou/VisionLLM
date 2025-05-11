#!/usr/bin/env python
"""
Simple example demonstrating basic VisionLLM usage.
"""

import os
import sys
import time

# Add the parent directory to the path so we can import visionllm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from visionllm import VisionManager


def main():
    """Run a simple demonstration of VisionLLM capabilities."""
    print("VisionLLM Simple Example")
    print("------------------------")
    
    # Initialize the vision manager with debug mode
    vision_manager = VisionManager(debug_mode=True)
    
    try:
        # Example 1: Text to Image
        print("\nExample 1: Text to Image")
        print("Generating an image from text...")
        prompt = "A beautiful sunset over mountains with a lake in the foreground"
        image = vision_manager.text_to_image(prompt)
        print("Text to image generation completed.")
        
        # Example 2: Image to Video
        print("\nExample 2: Image to Video")
        print("Creating a video from the generated image...")
        video_frames = vision_manager.image_to_video(
            image,
            prompt="Add gentle ripples to the lake and clouds moving slowly",
            duration=5.0
        )
        print("Image to video generation completed.")
        
        # Example 3: Text to Video
        print("\nExample 3: Text to Video")
        print("Generating a video directly from text...")
        prompt = "A timelapse of a blooming flower"
        video_frames = vision_manager.text_to_video(prompt, duration=3.0)
        print("Text to video generation completed.")
        
        print("\nAll examples completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up resources
        vision_manager.cleanup()


if __name__ == "__main__":
    main() 