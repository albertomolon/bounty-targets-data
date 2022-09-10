#!/usr/bin/python3

import json
import sys

PROGRAM_BC_FILE = "in_scope/bc-program.txt"
APK_BC_FILE = "in_scope/bc-apk.txt"
URL_BC_FILE = "in_scope/bc-url.txt"

PROGRAM_H1_FILE = "in_scope/h1-program.txt"
APK_H1_FILE = "in_scope/h1-apk.txt"
URL_H1_FILE = "in_scope/h1-url.txt"

PROGRAM_IN_FILE = "in_scope/in-program.txt"
APK_IN_FILE = "in_scope/in-apk.txt"
URL_IN_FILE = "in_scope/in-url.txt"

################
### BUGCROWD ###
################
def handle_bc_targets_scopes(filedata):
	for program in filedata:
		targets = program['targets']
		in_scope = targets['in_scope']
		if in_scope == []:
			write_file_content(PROGRAM_BC_FILE, f"{program['url']}\n")
		else:
			for item in in_scope:
				if item['type'] == 'android' or (item['type'] == 'other' and 'Android' in item['target']):
					write_file_content(APK_BC_FILE, f"{program['url']:<45}\t-->\t{item['target']}\n")
				elif item['type'] == 'website' or (item['type'] == 'other' and (('https://' in item['target']) or ('domain' in item['target']))):
					write_file_content(URL_BC_FILE, f"{program['url']:<45}\t-->\t{item['target']}\n")
				else:
					pass


#################
### HACKERONE ###
#################
def handle_h1_targets_scopes(filedata):
	for program in filedata:
		targets = program['targets']
		in_scope = targets['in_scope']
		if in_scope == []:
			write_file_content(PROGRAM_H1_FILE, f"{program['url']}\n")
		else:
			for item in in_scope:
				if item['asset_type'] == 'GOOGLE_PLAY_APP_ID' or item['asset_type'] == 'OTHER_APK':
					write_file_content(APK_H1_FILE, f"{program['url']:<45}\t-->\t{item['asset_identifier']}\n")
				elif item['asset_type'] == 'URL':
					write_file_content(URL_H1_FILE, f"{program['url']:<45}\t-->\t{item['asset_identifier']}\n")
				else:
					pass


#################
### INTIGRITI ###
#################
def handle_in_targets_scopes(filedata):
	for program in filedata:
		targets = program['targets']
		in_scope = targets['in_scope']
		if in_scope == []:
			write_file_content(PROGRAM_IN_FILE, f"{program['url']}\n")
		else:
			for item in in_scope:
				if item['type'] == 'android' or (item['type'] == 'other' and item['description'] != None and 'app' in item['description']):
					write_file_content(APK_IN_FILE, f"{program['url']:<45}\t-->\t{item['endpoint']}\n")
				elif item['type'] == 'url':
					write_file_content(URL_IN_FILE, f"{program['url']:<45}\t-->\t{item['endpoint']}\n")
				else:
					pass


def erase_file_content(filename):
	f = open(filename, "w")
	f.write("")
	f.close()


def write_file_content(filename, content):
	f = open(filename, "a")
	f.write(content)
	f.close()


def main():
	file = open("data/bugcrowd_data.json", "r")
	data = json.load(file)
	erase_file_content("in_scope/bc-program.txt")
	erase_file_content("in_scope/bc-apk.txt")
	erase_file_content("in_scope/bc-url.txt")
	handle_bc_targets_scopes(data)
	file.close()

	file = open("data/hackerone_data.json", "r")
	data = json.load(file)
	erase_file_content("in_scope/h1-program.txt")
	erase_file_content("in_scope/h1-apk.txt")
	erase_file_content("in_scope/h1-url.txt")
	handle_h1_targets_scopes(data)
	file.close()

	file = open("data/intigriti_data.json", "r")
	data = json.load(file)
	erase_file_content("in_scope/in-program.txt")
	erase_file_content("in_scope/in-apk.txt")
	erase_file_content("in_scope/in-url.txt")
	handle_in_targets_scopes(data)
	file.close()


if __name__ == "__main__":
	main()


