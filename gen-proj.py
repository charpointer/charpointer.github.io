#!/usr/bin/python3

#
# Generate a static HTML page with links to the Github projects
#

template = """
<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>charpointer.github.io</title>
<head>

<body>
	<div class="sidebar" style="float: left;">
		<ul>
            <li><a href="../index.html">/home</a></li>
			<li><a href="about.html">/about</a></li>
			<li><a href="proj.html">/proj</a></li>
		</ul>
	
		<img class="pride-badge" src="../assets/asexual.png">
	</div>

    <div class="container">
	<div class="content">
        <h2 class="page-header">Project listing (auto-generated)</h2>
		<ul>
$PROJ
        </ul>
    </div>
    </div>

    <style>
    </style>

	<link rel="stylesheet" href="../styles.css">
</html>
"""

def generate_template(x, xs):
    return f'<li><a href={xs}>{x}</a></li>'

def parse_projects():
    f = open("projects.txt", "r")
    templates = []
    
    for a in f.readlines():
        c = a.strip("\n").replace("\n", "").split("=")
        templates.append(generate_template(c[0], c[1]))

    f.close()
    return templates

projects = parse_projects()
new = ""
for proj in projects:
    # replace the $PROJ
    new += " "*12 + f"{proj}" + "\n"
    temp = template.replace("$PROJ", new)

    f = open("pages/proj.html", "w")
    f.write(temp)
    f.close()