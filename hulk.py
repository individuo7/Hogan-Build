import sys, subprocess

def mustache_compile(*args):
    p = subprocess.Popen(['hulk', args[0][1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    f = open(args[0][2], "w")
    try:
        f.write(out.replace("var templates = {};","try {templates}catch(e){var templates={}}"))
    finally:
        f.close()

if __name__ == "__main__":
    mustache_compile(sys.argv)