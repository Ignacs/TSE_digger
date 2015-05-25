# -*- coding: big5 -*-
import csv
import os, sys, platform

f = open(sys.argv[1], 'r')
# j=0
csv_line=0

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

for nline_data in csv.reader(f):
	csv_line = csv_line+1

	# j=j+1
	if len(nline_data) == 16:
		# print id  and no NEW LINE (Include ",")
		sid=str(nline_data[0])

		# print stock name in chinese
		name=str(nline_data[1])

		if sid.isdigit():
		#	print nline_data[0], 

			# output utf-8 encod
			# if output to file, it will show chinese in utf-8
			try:
				# print name.decode('utf-8')

				# output path
				stock_indep_file=os.path.join(output_folder, sid + '_' + name.decode('utf-8') )
				str_encode='utf8'
			except:	
				try: 
					# print name.decode('big5')

					# output path
					stock_indep_file=os.path.join(output_folder, sid + '_' + name.decode('big5') )
					str_encode='big5'
				except:
					print 'cant handle name ' + sid # + ' not encode big5 '

			if 'utf8' != str_encode:
				if 'big5'!= str_encode:
					print "ascii string " + name 
			

			# print "output to ", stock_indep_file, 
			try:
				# output to file
				f=open(stock_indep_file, "w")
				# information begins from 2nd element
				for sec_idx in range(2, 16):
					# sperate with ";" not ','
					f.write(str(nline_data[sec_idx]) )
					if 15 != sec_idx:
						f.write(";")
				f.close()
			except:	
				print "Failed to write file. exit"
				exit
		else:
			# ETF contains a '=' charater in id, it should be remove 
#			if '=' ==  sid[0]:
#				print 'is ETF [' + sid + ']'
#			elif not sid[-1].isdigit():
#				print 'is ETF [' + sid + ']'
#			else:
#				print "Can't handle " + sid 
#				break;

			start_idx=0
			end_idx=0
			is_stock_idx=0
			for id_idx in range(0, len(sid)):
				if sid[id_idx].isdigit():
					is_stock_idx=1
					start_idx = id_idx
					# print 'found digit ' + str(start_idx)
					for id_eidx in range(id_idx, len(sid)):
						if not sid[id_eidx].isdigit():
							end_idx = id_eidx
							# print 'found digit end ' + str(end_idx)
							break;
					break;

			# string is not a stock index, check next line in CSV
			if 0 == is_stock_idx:
#				print "error: "+ sid 
				continue

#			if len(sid)==start_idx:
#				print "is ascii or other encode string: "	+ sid
#			else:
#				print 'stock id = ' + sid[start_idx:end_idx]
			str_encode=''
			# output utf-8 encod
			# if output to file, it will show chinese in utf-8
			try:
				# print name.decode('utf-8')
				# output path
				stock_indep_file=os.path.join(output_folder, sid[start_idx:end_idx] + '_' + name.decode('utf-8') )
				str_encode='utf8'
			except:	
				try: 
					# print name.decode('big5')
					# output path
					stock_indep_file=os.path.join(output_folder, sid[start_idx:end_idx] + '_' + name.decode('big5') )
					str_encode='big5'
				except:
					print 'cant handle name ' + sid # + ' not encode big5 '

			if 'utf8' != str_encode:
				if 'big5'!= str_encode:
					print "ascii string " + name 

			# print "output to ", stock_indep_file, 
			try:
				# output to file
				f = open(stock_indep_file, "w")
				# information begins from 2nd element
				for sec_idx in range(2, 16):
					# sperate with ";" not ','
					f.write(str(nline_data[sec_idx]) )
					if 15 != sec_idx:
						f.write(";")
				f.close()
			except:	
				print "Failed to write file. exit"
				exit


	elif 1 == csv_line:
		# try to get first line : date
		date_line=str(nline_data)
		try:
			print date_line.decode('utf-8')
		except UnicodeDecodeError:
			print date_line.decode('big5')
		else:
			print date_line.decode('ascii')

		# for idx in range(0, len(date_line)):
		#	print idx

		
	#else:
	#	print "too long to handle : [" + str(nline_data) + "]"
		
f.close()


