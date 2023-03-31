# cimg
compress images command


## Compile
Use this [instructions](./COMPILE.md) to compile the code and get an executable binary file.

Save the `cimg` file in your executables directory in order to call the command. Usually into `/usr/bin` folder or link it.

## Usage

There are two ways to run the command:
- passing the reference to image file and respective output

```
cimg image.png  compressed.png
```

Or run `cimg --help` to get instructions

- passing the image as STDIN and the compressed result saved through STDOUT pipe

```
cimg < input.jpeg  > output.png
```
## Options

`-size -s ` dimension (in pixels) of the max size of output image 

`--quality -q` number to define the output quality of image [default : 70]
