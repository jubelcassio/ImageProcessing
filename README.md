
## Image Processing

General use scripts for image processing using the Pillow library

#### Usage:

` python process_img.py [action] [file/directory] [arguments] `  
\[file/directory] must be a single image or a directory containing image files to be processed.

#### Supported Formats:
The supported file types for both, reading and writing are:  
bmp, eps, gif, ico, jpg, jpeg, png, tiff, webp

#### Available actions:
* **convert**: Converts image(s) to given format.  
` python process_img.py convert [file/directory] [format to convert] `  
\[format to convert] must be one of the supported formats, listed above and in lower case

* **resize**: Resizes image(s) to given width and height.  
` python process_img.py resize [file/directory] [width] [height] `  
\[width] and \[height] must be integers.

* **scale**: Scale image(s) by given scalar.  
` python process_img.py scale [file/directory] [scalar] `  
\[scalar] must be a decimal or integer.

* **fit**: Resize an image to a given width / height while maintaining its aspect ratio. The offset area is transparent or filled with a white background, depending on the mode of the original image.  
` python process_img.py fit [file/directory] [width] [height] [--color] [--alpha] `  
\[width] and \[height] must be integers.  
\[color] must be a hexadecimal color value, used to fill the background.  
\[alpha] a integer value between 0 to 255, makes the background transparent for image modes that support transparency.
