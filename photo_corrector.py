#!/usr/bin/env python3
"""
Photo Correction Tool
A comprehensive tool for correcting and enhancing photos with various filters and adjustments.
"""

import os
import sys
import argparse
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np

class PhotoCorrector:
    def __init__(self):
        self.supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')
    
    def auto_correct(self, image_path, output_path=None, intensity=0.7):
        """
        Automatically correct a photo with common enhancements
        """
        try:
            # Open the image
            img = Image.open(image_path)
            original_mode = img.mode
            
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            print(f"Processing: {os.path.basename(image_path)}")
            
            # Auto-enhance brightness
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.0 + intensity * 0.1)
            
            # Auto-enhance contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.0 + intensity * 0.2)
            
            # Auto-enhance color saturation
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.0 + intensity * 0.15)
            
            # Auto-enhance sharpness
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.0 + intensity * 0.25)
            
            # Apply noise reduction (slight blur then sharpen)
            img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
            img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))
            
            # Auto-level (improve dynamic range)
            img = ImageOps.autocontrast(img, cutoff=2)
            
            # Convert back to original mode if needed
            if original_mode != 'RGB' and original_mode in ['L', 'P']:
                img = img.convert(original_mode)
            
            # Save the corrected image
            if output_path is None:
                name, ext = os.path.splitext(image_path)
                output_path = f"{name}_corrected{ext}"
            
            img.save(output_path, quality=95)
            print(f"Saved corrected image: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"Error processing {image_path}: {str(e)}")
            return None
    
    def adjust_brightness(self, image_path, factor=1.2, output_path=None):
        """Adjust image brightness"""
        try:
            img = Image.open(image_path)
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(factor)
            
            if output_path is None:
                name, ext = os.path.splitext(image_path)
                output_path = f"{name}_bright{ext}"
            
            img.save(output_path, quality=95)
            print(f"Brightness adjusted: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error adjusting brightness: {str(e)}")
            return None
    
    def adjust_contrast(self, image_path, factor=1.2, output_path=None):
        """Adjust image contrast"""
        try:
            img = Image.open(image_path)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(factor)
            
            if output_path is None:
                name, ext = os.path.splitext(image_path)
                output_path = f"{name}_contrast{ext}"
            
            img.save(output_path, quality=95)
            print(f"Contrast adjusted: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error adjusting contrast: {str(e)}")
            return None
    
    def adjust_saturation(self, image_path, factor=1.2, output_path=None):
        """Adjust color saturation"""
        try:
            img = Image.open(image_path)
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(factor)
            
            if output_path is None:
                name, ext = os.path.splitext(image_path)
                output_path = f"{name}_saturated{ext}"
            
            img.save(output_path, quality=95)
            print(f"Saturation adjusted: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error adjusting saturation: {str(e)}")
            return None
    
    def sharpen_image(self, image_path, factor=1.5, output_path=None):
        """Sharpen the image"""
        try:
            img = Image.open(image_path)
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(factor)
            
            if output_path is None:
                name, ext = os.path.splitext(image_path)
                output_path = f"{name}_sharp{ext}"
            
            img.save(output_path, quality=95)
            print(f"Image sharpened: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error sharpening image: {str(e)}")
            return None
    
    def reduce_noise(self, image_path, output_path=None):
        """Reduce image noise"""
        try:
            img = Image.open(image_path)
            
            # Apply median filter to reduce noise
            img = img.filter(ImageFilter.MedianFilter(size=3))
            
            if output_path is None:
                name, ext = os.path.splitext(image_path)
                output_path = f"{name}_denoised{ext}"
            
            img.save(output_path, quality=95)
            print(f"Noise reduced: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error reducing noise: {str(e)}")
            return None
    
    def process_directory(self, directory_path, output_dir=None, auto_correct=True):
        """Process all images in a directory"""
        directory = Path(directory_path)
        
        if output_dir is None:
            output_dir = directory / "corrected"
        else:
            output_dir = Path(output_dir)
        
        # Create output directory if it doesn't exist
        output_dir.mkdir(exist_ok=True)
        
        processed_count = 0
        
        for file_path in directory.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in self.supported_formats:
                output_path = output_dir / f"corrected_{file_path.name}"
                
                if auto_correct:
                    result = self.auto_correct(str(file_path), str(output_path))
                    if result:
                        processed_count += 1
        
        print(f"\nProcessed {processed_count} images. Results saved in: {output_dir}")
        return processed_count

def main():
    parser = argparse.ArgumentParser(description="Photo Correction Tool")
    parser.add_argument('input', help='Input image file or directory')
    parser.add_argument('-o', '--output', help='Output file or directory')
    parser.add_argument('-b', '--brightness', type=float, default=1.2, 
                       help='Brightness factor (default: 1.2)')
    parser.add_argument('-c', '--contrast', type=float, default=1.2,
                       help='Contrast factor (default: 1.2)')
    parser.add_argument('-s', '--saturation', type=float, default=1.2,
                       help='Saturation factor (default: 1.2)')
    parser.add_argument('--sharpen', type=float, default=1.5,
                       help='Sharpness factor (default: 1.5)')
    parser.add_argument('--auto', action='store_true', default=True,
                       help='Apply automatic corrections (default)')
    parser.add_argument('--manual', action='store_true',
                       help='Apply manual adjustments instead of auto')
    parser.add_argument('--intensity', type=float, default=0.7,
                       help='Intensity of auto corrections (0.0-1.0, default: 0.7)')
    
    args = parser.parse_args()
    
    corrector = PhotoCorrector()
    input_path = Path(args.input)
    
    if not input_path.exists():
        print(f"Error: Input path '{args.input}' does not exist.")
        return 1
    
    if input_path.is_file():
        # Process single file
        if args.manual:
            # Apply manual adjustments
            corrector.adjust_brightness(args.input, args.brightness, args.output)
            corrector.adjust_contrast(args.input, args.contrast, args.output)
            corrector.adjust_saturation(args.input, args.saturation, args.output)
            corrector.sharpen_image(args.input, args.sharpen, args.output)
        else:
            # Apply auto correction
            corrector.auto_correct(args.input, args.output, args.intensity)
    
    elif input_path.is_dir():
        # Process directory
        corrector.process_directory(args.input, args.output, not args.manual)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())