Mustache build system package for Sublime Text 2
======================================

Provides build systems for `.mustache` files. Requires hulk (via [hogan.js](http://twitter.github.com/hogan.js/)).

Installing
----------
**With the Package Control plugin:** The easiest way to install this package is through Package Control, which can be found at this site: [http://wbond.net/sublime_packages/package_control](http://wbond.net/sublime_packages/package_control)

Installing Requirements
----------

1. Install [Pyhon](http://www.python.org)
2. Install [NodeJS](http://nodejs.org)
3. Install npm([NodeJS Package Manager](https://npmjs.org/doc/README.html))
4. Install hogan.js via npm

## 
    npm install -g hogan.js
    
### In Ubuntu

##
    sudo apt-get install node-legacy npm; sudo npm install -g hogan.js
    
Usage
----------

1. Open a mustache file
2. Select Hogan as Build System Tools > Build System > Hogan
3. Compile a .mustache file (Ctrl-B)
4. See compiled js file in the same directory

Note: You must add Hogan-X.js at the base of the project. See https://github.com/twitter/hogan.js/tree/master/web/builds

You can access templates with *templates* variable in your javascript files

