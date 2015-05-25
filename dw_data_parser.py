# -*- coding: big5 -*-
import csv
import os, sys, platform

f = open(sys.argv[1], 'r')
# j=0

output_folder='/media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/stock'

# check output file 
try:
	os.stat(output_folder)
except:	
	print "Not exist, try to create it."
	try :
		os.makedirs(output_folder)
	except:
		print "Failed to create it."
		exit

for i in csv.reader(f):
	# j=j+1
	if len(i) == 16:
		# print id  and no NEW LINE (Include ",")
		sid=str(i[0])

		if sid.isdigit():
		#	print i[0], 
			# print stock name in chinese
			name=str(i[1])

			# output utf-8 encod
			# if output to file, it will show chinese in utf-8
			try:
				# print name.decode('utf-8')

				# output path
				stock_indep_file=os.path.join(output_folder, sid + '_' + name.decode('utf-8') )
				str_encode='utf8'
			except:	
				print sid # + ' not encode utf-8 '

			try: 
				# print name.decode('big5')

				# output path
				stock_indep_file=os.path.join(output_folder, sid + '_' + name.decode('big5') )
				str_encode='big5'
			except:
				print sid # + ' not encode big5 '

			if 'utf8' != str_encode:
				if 'big5'!= str_encode:
					print "ascii string " + name + name
			

			# print "output to ", stock_indep_file, 
			try:
				# output to file
				f=open(stock_indep_file, "w")
				for sec_idx in range(2, 16):
					# sperate with ";" not ','
					f.write(str(i[sec_idx]) )
					if 15 != sec_idx:
						f.write(";")
				f.close()
			except:	
				print "Failed to write file. exit"
				exit
		else:
			# ETF contains a '=' charater in id, it should be remove 
			print 'is ETF' + sid



	# elif len(i) < 16:
	# else
		
f.close()


