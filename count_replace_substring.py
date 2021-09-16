import re

input_string = input ("Enter a string ")
substring = input ("Enter a substring ")

(output_string, count) = re.subn(substring, "", input_string)
print (count)
print (output_string)