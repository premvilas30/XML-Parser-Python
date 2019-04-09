python_xml_parser
=================

This is a simple XML parser, It will return the value of a tag in an xml document.
It is capable of identifying non-sibling repeated tag.


Requirements
------------

No external requirements. Python 3+ is required


Usage
-----

Step 1: Execute the parser using below command:
            >>>python python_xml_parser.py
		
Step 2:	It will ask for xml file path, Please look into below example:
			>>>Please enter the file name:
			>>>input.xml
		
		
Step 3:	Then it will ask for target path input, please use below shown format to pass the target path :
			>>>Please enter / separated path (e.g. /person/name ):
			>>>/person/address/name
			
Output
------
        Please enter the file name:
		input.xml
		Please enter / separated path (e.g. /person/name ):
		/person/address/name
		Value for target path "/person/address/name" is "Mansion house"
				
				