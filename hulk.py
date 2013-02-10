import sys, subprocess

def mustache_compile(*args):
    if sys.platform.startswith('win'):
        p = subprocess.Popen(['hulk', args[0][1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    else:
        p = subprocess.Popen(['hulk', args[0][1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    f = open(args[0][2], "w")
    try:
        f.write(out.replace("var templates = {};","if (templates) {} else {var templates={}}"))
    finally:
        f.close()

if __name__ == "__main__":
    try:
        mustache_compile(sys.argv)
    except:
        print 'Make sure you have installed hogan.js'
        print 'With node.js pakage manager: npm install -g hogan.js'
