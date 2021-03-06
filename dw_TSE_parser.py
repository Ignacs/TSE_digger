# -*- coding: big5 -*-
import csv
import os, sys, platform

# j=0
csv_line=0
today=''
era=''
################# Usage ################# 
def usage():
#	"python dw_data_parser.py xxx.csv"
	print "python dw_data_parser.py (csv flle download from TSE) (ouptut foloder)" 

################ check history file record by date ################
# if record has same date, ignore it 
def csv_date_check(f, date):
	res=0
	try:
		os.stat(f)
	except:	
		return res

	f=open(f, 'r')
	print "[Info] date " + str(date)
	for his_data in csv.reader(f, delimiter=';' ):
		if his_data[0] == str(date):
			res=-1
	f.close()
	return res
################ check history file record by date ################
# check 
if  3 > len(sys.argv):
	print "[Error] Too few arguments."
	usage()
	sys.exit()	

output_folder=str(sys.argv[2])

# check output file 
try:
	os.stat(output_folder)
except:	
	print "[Warning] Not exist, try to create it." + output_folder
	try :
		os.makedirs(output_folder)
	except:
		print "[Error] Failed to create it."
		sys.exit()

total_stock_file = open(sys.argv[1], 'r')

for nline_data in csv.reader(total_stock_file):
	csv_line = csv_line+1
	date_line=str(nline_data)

	# j=j+1
	if len(nline_data) == 16:
		# print id  and no NEW LINE (Include ",")
		sid=str(nline_data[0])

		# print stock name in chinese and trim string
		name=str(nline_data[1]).strip()

		if sid.isdigit():
			# output utf-8 encod
			# if output to file, it will show chinese in utf-8
			try:
				# output path
				# Stop trying to use Chinese file name // Foxconn modify, Ignacs Wu, 2015/06/27 
				# stock_indep_file = os.path.join(output_folder, sid + '_' + name.decode('utf-8') )
				stock_indep_file = os.path.join(output_folder, sid  )
				str_encode='utf8'
			except:	
				try: 
					# output path
					# Stop trying to use Chinese file name // Foxconn modify, Ignacs Wu, 2015/06/27 
					# stock_indep_file = os.path.join(output_folder, sid + '_' + name.decode('big5') )
					stock_indep_file = os.path.join(output_folder, sid )
					str_encode='big5'
				except:
					print '[Warning] cant handle name ' + sid # + ' not encode big5 '

			if 'utf8' != str_encode:
				if 'big5'!= str_encode:
					continue

			try:
				# if record has more than 16 elements
				if csv_date_check(stock_indep_file, today) < 0:
					continue

				# output to file
				f=open(stock_indep_file, "a+")

				# write date into file as first element 
				if '' != today:
					f.write( today + ';')

				# information begins from 2nd element
				for sec_idx in range(2, len(nline_data)):
					# sperate with ";" not ','
					f.write(str(nline_data[sec_idx]).replace(',', "") )
					if 15 != sec_idx:
						f.write(";")
					elif 15 == sec_idx:
						f.write("\n")

				f.close()
			except:	
				print "[Warning] Failed to write file. "
				continue
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
					for id_eidx in range(id_idx, len(sid)):
						if not sid[id_eidx].isdigit():
							end_idx = id_eidx
							break;
					break;

			# string is not a stock index, check next line in CSV
			if 0 == is_stock_idx:
				continue

			str_encode=''
			# output utf-8 encod
			# if output to file, it will show chinese in utf-8
			try:
				# output path
				# Stop trying to use Chinese file name # // Foxconn add, Ignacs Wu, 2015/06/27 
				# stock_indep_file=os.path.join(output_folder, sid[start_idx:end_idx] + '_' + name.decode('utf-8') )
				stock_indep_file=os.path.join(output_folder, sid[start_idx:end_idx]  )
				str_encode='utf8'
			except:	
				try: 
					# output path
					# Stop trying to use Chinese file name // Foxconn modify, Ignacs Wu, 2015/06/27 
					# stock_indep_file=os.path.join(output_folder, sid[start_idx:end_idx] + '_' + name.decode('big5') )
					stock_indep_file=os.path.join(output_folder, sid[start_idx:end_idx]  )
					str_encode='big5'
				except:
					print '[Warning] cant handle name ' + sid # + ' not encode big5 '
					continue

			print "[Info] output " + stock_indep_file,
			try:
				# if record has more than 16 elements
				if csv_date_check(stock_indep_file, today) < 0:
					continue
				print "[Info] begin to write"

				# output to file
				f = open(stock_indep_file, "a+")

				# write date into file as first element 
				if '' != today:
					f.write( today + ';')

				print "[Info] write " + today
				# information begins from 2nd element
				for sec_idx in range(2, len(nline_data)):
					# sperate with ";" not ','
					f.write(str(nline_data[sec_idx]).replace(',', "") )
					if 15 != sec_idx:
						f.write(";")
					elif 15 == sec_idx:
						f.write("\n")
				f.close()
			except:	
				continue


	# NULL string , donothing
	elif 0 == len(nline_data):
		continue

	# ROC years 
	elif date_line[2].isdigit() and date_line[3].isdigit() and date_line[4].isdigit() and  date_line[10].isdigit() and date_line[11].isdigit() and date_line[20].isdigit() and date_line[21].isdigit():
		# try to get first line not null : date
		# the first line, it should be like below one:
		# ['104\xa6~05\xa4\xeb22\xa4\xe9\xa4j\xbdL\xb2\xce\xadp\xb8\xea\xb0T']
		# print "[ date:  "+  date_line[2] + date_line[3] + date_line[4] + date_line[10] + date_line[11] + date_line[20] + date_line[21]+ "]"
		era = str(int(date_line[2])*100 + int(date_line[3])*10 + int(date_line[4]) + 1911)
		today = era + date_line[10] + date_line[11] + date_line[20] + date_line[21]
		print "[Info] Found date string : " + today
		continue
	# ERA 
	elif date_line[2].isdigit() and date_line[3].isdigit() and date_line[4].isdigit()and date_line[5].isdigit() and  date_line[18].isdigit() and date_line[19].isdigit() and date_line[32].isdigit() and date_line[33].isdigit():
		# try to get first line not null : date
		# the first line, it should be like below one:
		# ['104\xa6~05\xa4\xeb22\xa4\xe9\xa4j\xbdL\xb2\xce\xadp\xb8\xea\xb0T']
		# print "[ date:  " + date_line[2] + date_line[3] + date_line[4]+ date_line[5] +  date_line[18] + date_line[19] + date_line[32] + date_line[33]+ "]"
		today = date_line[2] + date_line[3] + date_line[4]+ date_line[5] +  date_line[18] + date_line[19] + date_line[32] + date_line[33]
		print "[Info] Found date string : " + today
		continue

total_stock_file.close()
sys.exit()

