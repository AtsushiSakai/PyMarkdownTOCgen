"""

Table of contents generator for markdown

author: Atsushi Sakai (@Atsushi_twi)

"""

import subprocess

TOC_HEADER_NUMBER = 2
HEADER = "Table of Contents"


def get_toc_str(fname):

    cmd = "./github-markdown-toc/gh-md-toc " + fname
    tocstr = subprocess.check_output(cmd, shell=True)
    tocstr = tocstr.decode("utf-8")

    ntoc = 0
    fstr = "\n# " + HEADER + "\n"
    for line in tocstr.split("\n")[1:]:
        if line.find('*') > -1 and line.find(HEADER) == -1:
            if ntoc >= 1:
                fstr += line + "\n"
            ntoc += 1

    fstr += "\n"
    #  print(fstr)

    return fstr


def get_original_contents(fname):
    f1 = open(fname, 'r')
    contents = f1.read()
    f1.close()
    return contents


def build_final_contenst(contents, tocstr):

    final_contents = ""
    add_toc = False
    header = 0
    for line in contents.split("\n"):

        if len(line) <= 0:
            continue

        if line[0] == "#":
            header += 1

        if header == TOC_HEADER_NUMBER:
            if not add_toc:
                final_contents += tocstr
                add_toc = True
        else:
            final_contents += line + "\n"

    if not add_toc:
        final_contents += tocstr

    return final_contents


def insertTOC(fname):
    print("fname:", fname)

    tocstr = get_toc_str(fname)

    contents = get_original_contents(fname)
    final_contents = build_final_contenst(contents, tocstr)

    # save final contents
    f = open(fname, 'w')
    f.write(final_contents)
    f.close()

    print("Done")


def main():
    print(__file__ + " start!!")

    fname = "./README.md"

    insertTOC(fname)


if __name__ == '__main__':
    main()
