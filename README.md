
## Image Processing

Scripts for image processing using the Pillow library  

#### Requirements:  
Python 3.6.3  
Pillow == 5.2.0  

For the tests:  
atomicwrites==1.1.5  
attrs==18.1.0  
more-itertools==4.2.0  
pluggy==0.6.0  
py==1.5.4  
pytest==3.6.3  
six==1.11.0  


#### Install:
Just clone the repository anywhere and call it by the full path while invoking python:
` python /home/user/scripts/ImageProcessing/process_img.py ... `

Alternatively, you can set the program in your PATH variable, so its accessible from anywhere in the system:  

**Linux:**  
Clone the repository into a directory of your choice (for example, /home/username/scripts)  
` git clone https://github.com/jubelcassio/ImageProcessing.git `  
Add the chosen directory into your PATH variable  
Set the permissions for the process_img.py file inside the ImageProcessing folder.  
` chmod +wx process_img.py `  
Create a symlink on the scripts directory to the process_img.py file  
` ln -s ImageProcess/process_img.py process_img.py`  
Now you can call the process_img file from any other directory on your system.  
`process_img [action] [file/directory] [arguments] `  
The tree of your directories should look like this:
<pre>
/home/username/scripts  
                  |---ImageProcessing  
                            |---process_img.py  
                            |--- ...  
                  |---process_img.py          <--- symlink  
</pre>

**Windows:**  
Clone the repository into a directory of your choice (for example, C:\user_scripts\)  
Add the program's directory (C:\user_scripts\ImageProcessing) into your user PATH variable  
Now you can call the process_img file from any other directory on your system.  
`process_img.py ...`


#### Usage:

After Installation:  
` process_img [action] [file/directory] [arguments] `  
Or by summoning python manually:
`python process_img.py [action] [file/directory] [arguments] `  
\[file/directory] must be a single image or a directory containing image files to be processed.


#### Supported Formats:
The supported file types for both, reading and writing are:  
bmp, eps, gif, ico, jpg, jpeg, png, tiff


#### Available commands:
* **convert**: Converts image(s) to given format.  
`process_img convert [file/directory] [save as] [optional arguments]`  
`[save as]` must be one of the supported formats, listed above and in lower case  
**optional arguments**  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--save_folder=[folder]` The directory where the images will be saved.  
`-optimize` If passed, the resulting images will be optimized for a smaller file size. Only works for jpg and png images.  
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
**example usage**  
Convert a directory of png images to jpg  
`process_img convert /png_images jpg`  
Replaces the transparency of a png image with a pink color  
`process_img convert transparent_img.png png --mode=RGB --background=255,0,255`  


* **resize**: Resizes image(s) to given width and height.  
`process_img resize [file/directory] [width] [height] [optional arguments]`  
`[width]` and `[height]` must be integers.  
**optional arguments**  
`--save_as=[format]` must be one of the supported formats, listed above and in lower case  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--save_folder=[folder]` The directory where the images will be saved.  
`--resample=[resampling filter]` The resampling filter to be used when resizing the images. The filters available are:  
"NEAREST", "LANCZOS", "BILINEAR", "BICUBIC", "BOX", "HAMMING"  
`-optimize` If passed, the resulting images will be optimized for a smaller file size. Only works for jpg and png images.   
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
**example usage**  
Resize all images of a directory to a size of 336 x 280.  
`process_img resize /images 336 280`  
Resize images to a size 336 x 280 while converting them to jpg and optimizing for web.  
`process_img resize /images 336 280 --save_as=jpg -optimize`  


* **scale**: Scale image(s) by given scalar.  
`process_img scale [file/directory] [scalar] [optional arguments]`  
`[scalar]` must be a decimal or integer, the image's width and height will be multiplied by this number.  
**optional arguments**  
`--save_as=[format]` must be one of the supported formats, listed above and in lower case  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--save_folder=[folder]` The directory where the images will be saved.  
`--resample=[resampling filter]` The resampling filter to be used when resizing the images. The filters available are:  
"NEAREST", "LANCZOS", "BILINEAR", "BICUBIC", "BOX", "HAMMING"  
`-optimize` If passed, the resulting images will be optimized for a smaller file size. Only works for jpg and png images.  
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
**example usage**  
Scale images of a directory by twice their size.  
`process_img scale /images 2`  


* **fit**: Resize an image to a given width / height while maintaining its aspect ratio. The offset area is transparent or filled with a white background, depending on the mode of the original image.  
`process_img fit [file/directory] [width] [height] [optional arguments]`  
`[width]` and `[height]` must be integers.  
`[color]` May be a hexadecimal color value ("#aabbcc" or "#aabbccff") or the rgb code for the chosen color, with each number separated by a comma and without spaces ("50,50,50" or "50,50,50,255")
`--save_as=\[format]` Optional argument for the format to use while saving the image. Must be one of the supported formats.  
**optional arguments**  
`--color=[color]` A color to be used as the background of the resulting image. Must be in hex code format ("#fff", "#ffffff", "#ffffffff") or as a list of rgb/rgba values, separated by a comma ("255,255,255" or "255,255,255,255")  
`--save_as=[format]` must be one of the supported formats, listed above and in lower case  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--save_folder=[folder]` The directory where the images will be saved.  
`--resample=[resampling filter]` The resampling filter to be used when resizing the images. The filters available are:  
"NEAREST", "LANCZOS", "BILINEAR", "BICUBIC", "BOX", "HAMMING"  
`-optimize` If passed, the resulting images will be optimized for a smaller file size. Only works for jpg and png images.  
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
**example usage**  
Fit images into a 400x400 image with white background. Useful for creating a grids of thumbnails that must have the same dimensions.  
`process_img fit /images 400 400 --color=255,255,255 --background=255,255,255`  
Same usage as the previous, but now we save the images as jpg and optimize their file size.  
`process_img fit /images 400 400 --color=255,255,255 --background=255,255,255 --save_as=jpg -optimize`  


* **info**: Prints the path, format, color mode and dimensions of the given image.  
`process_img info [file/directory]`


* **dessaturate**: Grayscales the image.  
`process_img dessaturate [file/directory] [optional arguments]`  
**optional arguments**  
`--save_as=[format]` must be one of the supported formats, listed above and in lower case  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--save_folder=[folder]` The directory where the images will be saved.  
`-optimize` If passed, the resulting images will be optimized for a smaller file size. Only works for jpg and png images.  
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
**example usage**  
Grayscaling all images of a directory:  
`process_img dessaturate /images`  


* **invert**: Invert the colors of the image.  
`process_img invert [file/directory] [optional arguments]`  
**optional arguments**  
`--save_as=[format]` must be one of the supported formats, listed above and in lower case  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--save_folder=[folder]` The directory where the images will be saved.  
`-optimize` If passed, the resulting images will be optimized for a smaller file size. Only works for jpg and png images.  
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
**example usage**  
Invert the colors of all images of a directory:  
`process_img invert /images`  


* **mirror**: Mirrors the images, by horizontal, vertical or both axis.  
`process_img mirror [file/directory] [mirror_mode] [optional arguments]`  
`[mirror mode]` Can be "v" for vertical, "h" for horizontal, or "vh" / "hv" for both.  
**optional arguments**  
`--save_as=[format]` must be one of the supported formats, listed above and in lower case  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--save_folder=[folder]` The directory where the images will be saved.  
`-optimize` If passed, the resulting images will be optimized for a smaller file size. Only works for jpg and png images.  
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
**example usage**  
Vertically mirroring of all images of a directory:  
`process_img mirror /images v`  
Vertically and Horizontally mirroring of all images of a directory:  
`process_img mirror /images vh`  


* **optimize**: Minimizes the image size.  
`process_img optimize [file/directory] [optional arguments]`  
**optional arguments**  
`--save_as=[format]` must be one of the supported formats, listed above and in lower case  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--save_folder=[folder]` The directory where the images will be saved.  
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
**example usage**  
Optimize all images of a directory and save them as jpg:  
`process_img optimize /images --save_as=jpg`  


* **colorswap**: Replaces the color of all pixels of the image with another.  
`process_img colorswap [file/directory] [before_color] [after_color] [optional arguments]`  
`[before_color]` and `[after_color]` must be a list of integers for each color value or a hexadecimal color name between quotes.  
**optional arguments**  
`--save_as=[format]` must be one of the supported formats, listed above and in lower case  
`--save_folder=[folder]` The directory where the images will be saved.  
`--mode=[mode]` The color mode to use when saving the image (RGB, RGBA, CMYK, ...)  
If the mode of the original image is not supported by the given format it will be saved in RGB or RGBA, depending on the image type.  
`--background` The color to use when saving a image with a mode that has alpha channel to a image mode that does NOT have alpha channel. The transparent area on the original image will be filled with the given color.  
`-optimize` If passed, the resulting images will be optimized for a smaller file size. Only works for jpg and png images.  
**example usage**  
Swaps the pink background of an image with transparent:  
`process_img colorswap pink_bg_image.png 255,0,255,255 255,255,255,0`  
Swaps the transparent background of an image with a white one.  
`process_img colorswap transparent_bg_image.png 255,255,255,0 255,255,255,255`  
Swaps the transparent background of an image with a white one and save them as optimized jpg.  
`process_img colorswap transparent_bg_image.png 255,255,255,0 255,255,255,255 --save_as=jpg -optimize`  


* **colorinfo**: Counts how many pixels of each color are in the image or in the given area from the image.  
`process_img colorinfo [file/directory] [optional arguments]`  
**optional arguments**  
`[--box]` A box of coordinates (left, upper, right, lower) representing the area to count the pixels  
`[--pixel]` The coordinates of a single pixel, prints the color of that pixel.  
**example usage**  
Count the colors of the whole image.  
`process_img colorinfo image.png`  
Count the colors of a 100 x 100 px square located at the top left of the image.  
`process_img colorinfo image.png --box=0,0,100,100`  
Check the color of a pixel at 255,100 coordinates.  
`process_img colorinfo image.png --pixel=255,100`  
