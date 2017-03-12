#! /usr/bin/python
import sys
import webbrowser

try:

	print '''
 -----------------------------------------------------------
|                                ( Filter Duplicate )      |____
|      #     #  #####                                           |
|      #     # #     # #    #   ##    ####   ####  #    #       |
|      #     #       #  #  #   #  #  #    # #    # ##   #       |
|      #######  #####    ##   #    # #      #    # # #  #       |
|      #     #       #   ##   ###### #  ### #    # #  # #       |
|      #     # #     #  #  #  #    # #    # #    # #   ##       |
|      #     #  #####  #    # #    #  ####   ####  #    #       |
|                                                               |
|                            Powered by Cyber Merah Putih       |
|                                  ( Denny Septian )            |
|                                                               |
 ----------------------------------------------------------------'''

	# Nge Input Data File
	fillh3x = raw_input("\n\t[+] Input your name file ? Example : namefileduplicatelur.txt \n\n > ")
	outfillh3x = raw_input("\n\t[+] Input your name output file? Example : outputnamefilelur.txt \n\n > ")
	# Nge Baca dan Nge Set Setiap Barisan Kata
	bacabarisan = open(fillh3x, 'r').readlines()
	ngesetbaris = set(bacabarisan)
	output  = open(outfillh3x, 'w')

	for baris in ngesetbaris:
		output.write(baris)
except KeyboardInterrupt:
	webbrowser.open('https://www.facebook.com/h3xagon.id')
	sys.exit()