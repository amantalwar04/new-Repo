#! /usr/bin/python3

import shutil
import fileinput
import os

# Write yaml into md header
#
def write_into_md(md_file_path, yaml):
    md_file = open(md_file_path, 'r+')
    contents = md_file.readlines();
    contents.insert(0, yaml);
    md_file.seek(0);
    md_file.writelines(contents);
    md_file.close();


# Write yaml into firts level *.md file header
#
def write_level_one(title, md_file_path):
    yaml = """---
layout: default
title: """ + title + """
nav_order: 1
---
""";
    md_file = open(md_file_path, 'r+')
    for line in md_file:
        if(line.find("-   **[") != -1):
            yaml = """---
layout: default
title: """ + title + """
nav_order: 1
has_children: true
---
""";
            break;
    write_into_md(md_file_path, yaml)


# Write yaml into second level *.md file header
#
def write_level_two(title, md_file_path):
    parent = get_parent(md_file_path, "false")
    yaml = """---
layout: default
title: """ + title + """
parent: """ + str(parent) + """
nav_order: 2
---
""";

    md_file = open(md_file_path, 'r+')
    for line in md_file:
        if(line.find("-   **[") != -1):
            yaml = """---
layout: default
title: """ + title + """
parent: """ + str(parent) + """
nav_order: 2
has_children: true
---
""";
            break;
    write_into_md(md_file_path, yaml)



# Write yaml into thrd level *.md file header
#
def write_level_three(title, md_file_path):
    parent = get_parent(md_file_path, "true")
    grand_parent = get_parent(parent[1], "false")
    yaml = """---
layout: default
title: """ + title + """
parent: """ + str(parent[0]) + """
grand_parent: """ + grand_parent + """
nav_order: 3
---
""";

    md_file = open(md_file_path, 'r+')
    for line in md_file:
        if(line.find("-   **[") != -1):
            yaml = """---
layout: default
title: """ + title + """
parent: """ + str(parent[0]) + """
grand_parent: """ + grand_parent + """
nav_order: 3
has_children: true
---
""";
            break;
    write_into_md(md_file_path, yaml)


# Write yaml into fourth level *.md file header
#
def write_level_four(title, md_file_path):
    parent = get_parent(md_file_path, "true")
    grand_parent = get_parent(parent[1], "true")
    grand_grand_parent = get_parent(grand_parent[1], "false")
    yaml = """---
layout: default
title: """ + title + """
parent: """ + str(parent[0]) + """
grand_parent: """ + str(grand_parent[0]) + """
grand_grand_parent: """ + str(grand_grand_parent) + """
nav_order: 4
---
""";

    md_file = open(md_file_path, 'r+')
    for line in md_file:
        if(line.find("-   **[") != -1):
            yaml = """---
layout: default
title: """ + title + """
parent: """ + str(parent[0]) + """
grand_parent: """ + str(grand_parent[0]) + """
grand_grand_parent: """ + str(grand_grand_parent) + """
nav_order: 4
has_children: true
---
""";
            break;
    write_into_md(md_file_path, yaml)

# Get level of the topic.
#
def get_level(line):
    level = line.split("[")[0]
    return level.count(' ');


# Get title of the topic, remove '\'.
#
def get_title(line):
    title = line.split("](")[0]
    title = title.split("[")[1]
    return title.replace("\\", '');


# Get md file of the topic.
#
def get_md_file(line):
    md = line.split("](")[1]
    md = md.split(")")[0]
    return md;


# Get parent topic of the topic.
# first argument: specify md file path,
# second argument: specify true if you want to get grand parent
def get_parent(md_file_path, need_parent_md_file):
    parent = "";
    parent_md_file = "";
    md_file = open(md_file_path, 'r+')
    for line in md_file:
        if(line.find("**Parent topic:**") != -1):
            parent = line.split("](")[0]
            parent = parent.split("*[")[1]
            parent = parent.replace("\\",'')
            if ("true" == need_parent_md_file):
                parent_md_file = line.split("](")[1];
                parent_md_file = parent_md_file.split(")")[0];
                return [parent, parent_md_file];
            else:
                return parent;


def main():
    index_md_file_path = "index.md"
    f = open(index_md_file_path, "r")
    lines = [line for line in f.readlines() if line.find("-") != -1]

    for line in lines:
        l = get_level(line);
        t = get_title(line);
        md = get_md_file(line);
        if (3 == l):
            write_level_one(t, md);
        elif (7 == l):
            write_level_two(t, md);
        elif (11 == l):
            write_level_three(t, md);
        else :
            write_level_four(t, md);


if __name__ == "__main__":
    main()

