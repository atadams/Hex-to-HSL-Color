# About
Adds commands to Sublime Text that converts RGB colors, in either hex or RGB() format, to HSL colors. For example:

* `#bada55` becomes `hsl(74, 64%, 59%)`
* `rgb(75, 96, 6)` becomes `hsl(74, 88%, 20%)`
* `rgba(117, 149, 9, 0.65)` becomes `hsla(74, 89%, 31%, 0.65)`

In the past, due to browser (IE) compatibility, it was best to use a CSS preprocessor to convert the HSL colors to hex. But now all major browsers [support HSL color](http://caniuse.com/#feat=css3-colors), including IE9+, so you can use HSL colors in CSS unless you need to support IE8.

# Installation
You can install using [Package Control](http://wbond.net/sublime_packages/package_control) or you can download or clone the repository and drop it into your Sublime Text packages directory.

# Version 2 Features
* Version 2 now converts hex and RGB to HSL and RGBA to HSLA. The previous version only converted hex to HSL.
* Optionally, you can convert hex, RGB, and RGBA to HSLA (force alpha). 
* You can now convert all hex, RGB, and RGBA colors in a file with a single command (`shift+ctrl+U`).

# Usage
* Convert All to HSL (preserving alpha): `shift+ctrl+U`
* Convert All to HSLA (force alpha): `shift+ctrl+alt+U`
* Convert Selected to HSL: `Edit > RGB to HSL`
* Convert Selected to HSLA: `Edit > RGB to HSL`

# Why No Hex/HSL to RGB support
HSL color is just better than hex or RGB ([Brandon Mathis](http://brandonmathis.com/blog/2011/03/02/hslpicker.com-released/) gives a good explanation why HSL rocks). I don't see any use for RGB—HSL is just more intuitive and makes it much easier to [combine colors](http://www.colorsontheweb.com/combiningcolors.asp) into a logical color scheme.

If you have the need to convert to RGB, you might try the [CSS Color Converter](https://github.com/TheDutchCoder/ColorConvert) plugin.

#HSL Resources
If you need more convincing about HSL, try these:

* [W3: HSL Colors](http://dev.w3.org/csswg/css-color/#the-hsl-notation)
* [HSL Color Picker](http://hslpicker.com/)
* [An Easy Guide To HSL Color In CSS3](http://demosthenes.info/blog/61/An-Easy-Guide-To-HSL-Color-In-CSS3)
* [Three Ways You Should Be Using HSL Color In Your Site Today](http://demosthenes.info/blog/576/Three-Ways-You-Should-Be-Using-HSL-Color-In-Your-Site-Today)
* [Color in Opera 10 — HSL, RGB and Alpha Transparency](http://dev.opera.com/articles/view/color-in-opera-10-hsl-rgb-and-alpha-transparency/)
* [HSL Color Wheel Demo](http://itpastorn.github.io/webbteknik/future-stuff/svg/color-wheel.html)
* [Paul Irish's Mother-effing HSL](http://mothereffinghsl.com/)
* [Coding Colors Easily Using CSS3 hsl() Notation](http://www.useragentman.com/blog/2010/08/28/coding-colors-easily-using-css3-hsl-notation/)
* [Treehouse Quick Tip: HSLa Color Values in CSS](http://www.youtube.com/watch?v=IdSsSaTU4lk)
* [HSL Color Wheel](http://hsl.clrpick.me/)
