#!/usr/bin/python3

import json
import sys


def handle_targets_scopes(filedata, asset):
	for program in filedata:
		targets = program['targets']
		in_scope = targets['in_scope']
		if in_scope == []:
			write_file_content("in_scope/h1-program.txt", f"{program['url']}\n")
		else:
			if asset == 'apk':
				for item in in_scope:
					if item['asset_type'] == 'GOOGLE_PLAY_APP_ID' or item['asset_type'] == 'OTHER_APK':
						write_file_content("in_scope/h1-apk.txt", f"{program['url']:<45}\t-->\t{item['asset_identifier']}\n")
			elif asset == 'url':
				for item in in_scope:
					if item['asset_type'] == 'URL':
						write_file_content("in_scope/h1-url.txt", f"{program['url']:<45}\t-->\t{item['asset_identifier']}\n")
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
	file = open("data/hackerone_data.json", "r")
	data = json.load(file)
	erase_file_content("in_scope/h1-program.txt")
	if asset == 'apk':
		erase_file_content("in_scope/h1-apk.txt")
	else:
		erase_file_content("in_scope/h1-url.txt")
	handle_targets_scopes(data, asset)
	file.close()


if __name__ == "__main__":
	main()


