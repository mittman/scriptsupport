#!/usr/bin/env python3

import os, sys
import subprocess

subdir = "sl_images"

def doSomething(files):
	current = os.getcwd()

	# create subdir if needed
	target = os.path.join(current, subdir)
	if os.path.exists(target):
		pass
	else:
		subprocess.call(['mkdir', '-p', target])

	# process the files
	for filename in files:
		file_path = os.path.realpath(filename)
		basename = os.path.basename(file_path)
		new_path = os.path.join(current, subdir, basename)

		# symlink the files
		print("ln -s", file_path, new_path)
		subprocess.call(['ln', '-s', file_path, new_path])


if __name__ == '__main__':
	if len(sys.argv) >= 2:
		files = sys.argv
	else:
		files = os.listdir('.')

	try:
		doSomething(files)
	except KeyboardInterrupt:
		print("\nExiting...")

		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

