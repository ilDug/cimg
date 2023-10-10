# cimg
**compress** and **convert** images command.


## Compile
Use this [instructions](./COMPILE.md) to compile the code and get an executable binary file.

Save the `cimg` file in your executables directory in order to call the command. Usually into `/usr/bin` folder or link it.

## Compression

There are two ways to run the command:
- passing the reference to image file and respective output

```
cimg compress image.png  compressed.png
```

Or run `cimg compress --help` to get instructions

- passing the image as STDIN and the compressed result saved through STDOUT pipe

```
cimg compress < input.jpeg  > output.png
```
### Options

`-size -s ` dimension (in pixels) of the max size of output image 

`--quality -q` number to define the output quality of image [default : 70]


## Conversion

Convert from **HEIC** format to **JPEG**

```
cimg convert image.heic  imge.jpeg
```

Or run `cimg convert --help` to get instructions