#!/usr/bin/env python
import re

__program__ = 'python_xml_parser'
___author__ = 'Prem k. <kesharip@tcd.ie>'


class Parser:
	def __init__(self, xml_input, target_path):
		self.xml_input = xml_input
		self.target_path = target_path

	def xml_parser(self) -> str:
		"""
			Summary line.

			Parses the input XML and returns the value of the requested tag

			:parameter
			----------
			xml_input : str
				input xml in string format
			target_path : List[str]
				path of the target tag separated by '/'.

			:raises:
				IndexError: If the path provided is incorrect

			:returns
			-------
			str
				value of the target tag

			"""
		try:
			# Parsing XML from outer lever
			for tag in self.target_path:
				pref_num = re.compile(f'(<(.?){tag}(.?)>|</(.?){tag}(.?)>)')
				out = [m for m in re.finditer(pref_num, self.xml_input)]
				self.xml_input = self.xml_input[out[0].end():out[-1].start()]

			# Making sure it finds correct value in case of non-sibling repeated tag
			if self.xml_input.__contains__('</' + self.target_path[-1] + '>'):
				end = [a for a in re.finditer('</' + self.target_path[-1] + '>', self.xml_input)]
				self.xml_input = self.xml_input[:end[-1].start()]
			return str(self.xml_input)
		except IndexError as e:
			print(f'Some exception occurred, make sure you have correct '
			      f'xml and path.')
		except Exception as e:
			print(f'Some exception occurred, Please find more info here:\n {e}')


def main():
	try:
		file = str(input('Please enter the file name:\n'))
		# Putting the readfile operation in context manager for tear-down purposes
		with open(file, 'r') as f:
			xml_input_text = str(f.read())
			path = str(input('Please enter / separated path '
			                 '(e.g. /person/name ):\n'))[1:].split('/')
			parser = Parser(xml_input_text, path)
			print(f'Value for target path \"/{"/".join(path)}\" is \"{parser.xml_parser()}\"')
	except FileNotFoundError as e:
		print(f'File not found: {file}')


if __name__ == '__main__':
	main()
