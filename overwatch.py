#!/usr/bin/python3
import os
import subprocess

#shortcode_file = open('List.html', 'r')

shortcode = str(input("Enter shortcode: "))

#shortcode_list = shortcode_file.read()
#shortcode_file.close()

shortcode_list = ""
shortcode_list+=shortcode

for shortcode in shortcode_list.split():
	argument = "probhtml" + " " + shortcode + " " + shortcode + "/pretext_source" 
	print (argument)
	subprocess.run(["python3", "GenerateHTML.py", shortcode])
	try:
		os.mkdir('./' + shortcode + '/pretext_source')
	except FileExistsError:
		print("Directory exists already.. Overwriting")
	subprocess.run(["./ltol.py", "probhtml", shortcode , shortcode + "/pretext_source" ])
	pretext_html = shortcode + '/pretext_html' 
	try:
		os.mkdir('./' + pretext_html)
	except FileExistsError:
		print("Directory exists already.. Overwriting")
	os.system("cd ./" + pretext_html+';' " /Users/terrybusk/pretext/pretext/pretext " + "--component all -f html /Users/terrybusk/Problem_lists/" + shortcode + "/pretext_source/" + shortcode + "-index.ptx")
	os.system("cd /Users/terrybusk/Problem_lists")

#if not os.path.isdir(dir):
#	os.mkdir(dir)
