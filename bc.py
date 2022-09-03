#!/usr/bin/python3

import json
import sys

PROGRAM_FILE = "in_scope/bc-program.txt"
APK_FILE = "in_scope/bc-apk.txt"
URL_FILE = "in_scope/bc-url.txt"


def handle_targets_scopes(filedata, asset):
	for program in filedata:
		targets = program['targets']
		in_scope = targets['in_scope']
		if in_scope == []:
			write_file_content(PROGRAM_FILE, f"{program['url']}\n")
		else:
			if asset == 'apk':
				for item in in_scope:
					if item['type'] == 'android' or (item['type'] == 'other' and 'Android' in item['target']):
						write_file_content(APK_FILE, f"{program['url']:<45}\t-->\t{item['target']}\n")
			elif asset == 'url':
				for item in in_scope:
					if item['type'] == 'website' or (item['type'] == 'other' and (('https://' in item['target']) or ('domain' in item['target']))):
						write_file_content(URL_FILE, f"{program['url']:<45}\t-->\t{item['target']}\n")
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
	asset = sys.argv[1]
	file = open("data/bugcrowd_data.json", "r")
	data = json.load(file)
	erase_file_content("in_scope/bc-program.txt")
	if asset == 'apk':
		erase_file_content("in_scope/bc-apk.txt")
	else:
		erase_file_content("in_scope/bc-url.txt")
	handle_targets_scopes(data, asset)
	file.close()


if __name__ == "__main__":
	main()


