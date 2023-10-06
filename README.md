# Formatizer
video to text based video format converter for [this](https://scratch.mit.edu/projects/904394551/) project

first comes the metadata:
```
xRes
yRes
skipframes
fps
```
*skipframes is the amount of frames that are skipped

the image format is b-g-r-

where it is a-j that mapps to 0-255

example: ```aaa-abb-ggg-```

if there is a large amount of the same letters they get replaced with ```#(letter)(amount in decimal)+```

```aaaaaaa -> #a7+```




