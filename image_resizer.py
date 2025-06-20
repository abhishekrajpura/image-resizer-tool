#!/usr/bin/env python3
"""
Image Resizer Tool
A simple Python script to resize images with user input
"""

from PIL import Image
import os
import sys

def resize_image(input_path, output_path, width, height, maintain_aspect=True):
    """
    Resize an image to specified dimensions
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to save resized image
        width (int): Target width
        height (int): Target height
        maintain_aspect (bool): Whether to maintain aspect ratio
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            original_width, original_height = img.size
            print(f"Original size: {original_width}x{original_height}")
            
            if maintain_aspect:
                # Calculate aspect ratio
                aspect_ratio = original_width / original_height
                
                # Adjust dimensions to maintain aspect ratio
                if width / height > aspect_ratio:
                    width = int(height * aspect_ratio)
                else:
                    height = int(width / aspect_ratio)
            
            # Resize the image
            resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
            
            # Save the resized image
            resized_img.save(output_path)
            print(f"Resized image saved as: {output_path}")
            print(f"New size: {width}x{height}")
            
            return True
            
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def get_user_input():
    """Get input parameters from user"""
    print("=== Image Resizer Tool ===\n")
    
    # Get input file path
    while True:
        input_path = input("Enter the path to your image file: ").strip()
        if os.path.exists(input_path):
            break
        print("File not found. Please enter a valid file path.")
    
    # Get output file path
    output_path = input("Enter output file path (press Enter for auto-generated name): ").strip()
    if not output_path:
        name, ext = os.path.splitext(input_path)
        output_path = f"{name}_resized{ext}"
    
    # Get target dimensions
    while True:
        try:
            width = int(input("Enter target width (pixels): "))
            height = int(input("Enter target height (pixels): "))
            if width > 0 and height > 0:
                break
            print("Please enter positive numbers for width and height.")
        except ValueError:
            print("Please enter valid numbers for width and height.")
    
    # Ask about aspect ratio
    while True:
        maintain_aspect = input("Maintain aspect ratio? (y/n): ").lower().strip()
        if maintain_aspect in ['y', 'yes', 'n', 'no']:
            maintain_aspect = maintain_aspect in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    return input_path, output_path, width, height, maintain_aspect

def main():
    """Main function"""
    try:
        # Check if PIL is available
        import PIL
    except ImportError:
        print("Error: Pillow library is not installed.")
        print("Please install it using: pip install Pillow")
        sys.exit(1)
    
    # Get user input
    input_path, output_path, width, height, maintain_aspect = get_user_input()
    
    # Resize the image
    success = resize_image(input_path, output_path, width, height, maintain_aspect)
    
    if success:
        print("\n✅ Image resized successfully!")
        
        # Ask if user wants to view the result
        view_result = input("\nWould you like to open the resized image? (y/n): ").lower().strip()
        if view_result in ['y', 'yes']:
            try:
                # Try to open the image with default system viewer
                if sys.platform.startswith('darwin'):  # macOS
                    os.system(f"open '{output_path}'")
                elif sys.platform.startswith('win'):   # Windows
                    os.system(f"start '{output_path}'")
                else:  # Linux
                    os.system(f"xdg-open '{output_path}'")
            except Exception as e:
                print(f"Could not open image automatically: {e}")
                print(f"You can manually open: {output_path}")
    else:
        print("\n❌ Failed to resize image.")

if __name__ == "__main__":
    main()