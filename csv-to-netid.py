#!/usr/bin/env python

import csv
import subprocess

# # CREATION LOOP
with open('all-thesis-students - with sections.csv', 'rb') as c:
    i = 0
    for row in csv.reader(c, delimiter=','):
        if i == 0:
            i += 1
            continue
        i += 1
        p = 'wp site create --slug=/blog/{} --email={} --title="{}"'.format(row[0], row[1], row[5])
	subprocess.call( p, shell=True )

# DELETION LOOP
# with open('all-thesis-students - with sections.csv', 'rb') as c:
#     i = 376
#     for row in csv.reader(c, delimiter=','):
#         if i == 376:
#             i += 1
#             continue
#         i += 1
#         p = "wp site delete "+str(i)+" --yes"
# 	subprocess.call( p, shell=True )