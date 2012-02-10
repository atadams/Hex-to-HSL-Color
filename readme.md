# About
Adds a command to Sublime Text 2 that converts hexadecimal colors to HSL colors. For example, #bada55 becomes hsl(74, 64%, 59%).

I work in Sass most often for my CSS and much prefer HSL colors ([Brandon Mathis](http://brandonmathis.com/blog/2011/03/02/hslpicker.com-released/) gives a good explaination why HSL rocks). When converting a CSS file to Sass, I usually move the colors to HSL, but that can be tedious even with great tools like [HSL Color Picker](http://hslpicker.com/) and [ColorSnapper](http://colorsnapper.com/). This plugin makes it much easier.

# Installation
I have submitted a pull request to be included in Package Control. Until then, you can download or clone the repository and drop it into your Sublime Text 2 packages directory.

# Usage
Put the cursor on or select one or more hex colors (three character colors are OK)

![Example 1](https://github.com/atadams/Hex-to-HSL-Color/raw/master/ex1.png)

Press shift+ctrl+U.

The colors will be converted to a properly formated CSS HSL color.

![Example 2](https://github.com/atadams/Hex-to-HSL-Color/raw/master/ex2.png)

# Future
I hope to modify the plugin to convert decimal RGB colors and also handle alphas.