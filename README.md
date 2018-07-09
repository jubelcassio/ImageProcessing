
## Image Processing

General use scripts for image processing using the Pillow library

#### Usage:

` python process_img.py [action] [file/directory] [arguments] `  
\[file/directory] must be a single image or a directory containing image files to be processed.

#### Supported Formats:
The supported file types for both, reading and writing are:  
bmp, eps, gif, ico, jpg, jpeg, png, tiff

#### Available actions:
* **convert**: Converts image(s) to given format.  
` python process_img.py convert [file/directory] [format to convert] --mode=[mode]`  
\[format to convert] must be one of the supported formats, listed above and in lower case  
--mode=\[mode] Optional argument for the color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the format.

* **resize**: Resizes image(s) to given width and height.  
` python process_img.py resize [file/directory] [width] [height] --save_as=[format]`  
\[width] and \[height] must be integers.  
--save_as=\[format] Optional argument for the format to use while saving the image. Must be one of the supported formats.


* **scale**: Scale image(s) by given scalar.  
` python process_img.py scale [file/directory] [scalar] `  
\[scalar] must be a decimal or integer.  
--save_as=\[format] Optional argument for the format to use while saving the image. Must be one of the supported formats.

* **fit**: Resize an image to a given width / height while maintaining its aspect ratio. The offset area is transparent or filled with a white background, depending on the mode of the original image.  
` python process_img.py fit [file/directory] [width] [height] [--color] [--alpha] `  
\[width] and \[height] must be integers.  
\[color] must be a hexadecimal color value, used to fill the background.  
\[alpha] a integer value between 0 to 255, makes the background transparent for image modes that support transparency.  
--save_as=\[format] Optional argument for the format to use while saving the image. Must be one of the supported formats.
