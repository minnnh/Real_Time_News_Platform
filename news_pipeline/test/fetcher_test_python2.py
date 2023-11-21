#!/usr/bin/env python2

# def show(text):
# 	print "text"


# python2_script.py
import subprocess


# try:
#     text = subprocess.check_call(['python3', 'fetcher_test_python3.py'])
#     print text
# except subprocess.CalledProcessError as e:
# 	print e
#     # print(f"Error running Python 3 script: {e}")

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'

try:
    # Run the target_script.py and capture its output
    #command = ['python3', 'fetcher_test_python3.py', 'getText', url]
    command = ['python3', 'fetcher_test_python3.py', url]

    # Use subprocess.PIPE to capture the output
    # result = subprocess.check_call(command)
    result = subprocess.check_output(command, stderr=subprocess.STDOUT)
    result_text = ''.join(result.decode('utf-8').strip().splitlines())

    print (result_text)
    # return result.strip()

except subprocess.CalledProcessError as e:
	print (e)