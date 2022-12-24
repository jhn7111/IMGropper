# IMGropper

A gui application to crop images.

The application performs cropping multiple images to parts you want, with the same resolution.
It only works in jpeg format. (I have plan to add other formats. Somedays...)

## Installation

It's tested on Python3.10

```python
pip install -r requirement.txt #install required lib
python setup.py build #build to win32
```
Required lib: Pillow(PIL), cx_Freeze

## Usage

work resolution: The size of the main window you will use for your work.

output resoultion: A image you will get at the end.

work dir: Folder with images that need to be worked on.

Mouse left: Save an image.

Mouse right: To next image

Mouse wheel: Change the size of the cropping rectangle.

Worked images will saved "work_dir\worked"

## ISSUE
I only tested on Windows11.

## Contributing

## License

[MIT](https://choosealicense.com/licenses/mit/)
