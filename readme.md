# OpenAutoBookmark

OpenAutoBookmark is a tool that replaces the AutoBookmark™ Plug-in for Adobe® Acrobat. It is designed to help users add bookmarks to their PDF files automatically.

## Features

- Automatically add bookmarks to PDF files
- Customize bookmark generation using regular expressions
- Open source and free to use

In the foreseeable future, a more intuitive and user-friendly version will be created and made available for download on Homebrew:

- Support for specifying regular expressions via the argc parameter in the terminal
- Various default regular expressions to use, with sub bookmarks


## Usage

1. Install OpenAutoBookmark repo on your machine.
2. Run the program and edit the PDF file that you want to add bookmarks to.
3. Customize bookmark generation if needed.
4. Click the "Add Bookmarks" button to automatically add bookmarks to the PDF file.

## Installation

To install OpenAutoBookmark, follow these steps:

1. Download the latest release from the [OpenAutoBookmark GitHub repository](https://github.com/SYXiao2002/OpenAutoBookmark/releases).
2. Extract the downloaded ZIP file to a directory of your choice.
3. Run the `openautobookmark.py` script to launch the program.

## Customization

To customize bookmark generation, use the regular expression feature in OpenAutoBookmark. Regular expressions can be used to match specific text patterns in the PDF file, which can then be used to generate bookmarks.

Default:
```
# Define the regular expression for header levels
""" 
Default: header_regex = r"^(\d+\.){1,3}\s+([\w\s]+)"
Able to find string like 
    3. THE ACTIVITY RECOGNITION CHAIN
    3.1. Sensor Data Acquisition and Preprocessing
    3.2. Data Segmentation
    3.2.1. Sliding Window.
""" 
```
For the sub bookmarks, similar way to customize.


## Support

If you encounter any issues or have any questions about OpenAutoBookmark, please open an issue on the [OpenAutoBookmark GitHub repository](https://github.com/SYXiao2002/OpenAutoBookmark/issues).

## License

OpenAutoBookmark is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
