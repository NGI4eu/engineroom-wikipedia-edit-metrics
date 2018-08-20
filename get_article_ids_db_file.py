# -*- coding: utf-8 -*-## Extracts page IDs from wiki pages (given their title).## EXECUTE:# python get_pageids_db.py data_test##import MySQLdb as mdbimport sysimport codecsimport datetimeimport ConfigParser#config = ConfigParser.RawConfigParser()#config.read('tool_labs.cfg')reload(sys)sys.setdefaultencoding('utf-8')if sys.stdout.encoding is None:	sys.stdout = codecs.open("/dev/stdout", "w", 'utf-8')### SETTINGS#data_dir = sys.argv[1]input_file_name = sys.argv[1] output_file_name = sys.argv[2] lang = 'en'if len(sys.argv)>3:	lang = sys.argv[3]with open('DB_info') as DB_info:	DB_USER_NAME = DB_info.readline().strip('\n')	DB_PASSWORD = DB_info.readline().strip('\n')## extract IDs from a list of titles#def extract_data(page_titles, mysql_cur, output_file):	page_titles_asstring = ','.join(['%s'] * len(page_titles))	mysql_cur.execute( 'SELECT page_title, page_id FROM page WHERE page_namespace = 0 AND page_title IN (%s)' % page_titles_asstring, page_titles)	rows = mysql_cur.fetchall()	page_titles_found = []	for row in rows:		page_titles_found.append(str(row[0]).decode('utf-8'))		output_file.write(row[0] + '\t' + str(row[1]) + '\n')	page_titles_notfound = list(set(page_titles) - set(page_titles_found))	for title in page_titles_notfound:		output_file.write(title + '\t\n')### EXECUTEprint "Current date and time [START]: " , datetime.datetime.now()mysql_con = mdb.connect('enwiki.labsdb', DB_USER_NAME, DB_PASSWORD, 'enwiki_p')mysql_con.set_character_set('utf8')input_file = codecs.open(input_file_name, 'r', 'UTF-8')output_file = codecs.open(output_file_name, 'w', 'UTF-8')with mysql_con:	mysql_cur = mysql_con.cursor()	page_titles = []	for line in input_file:		page_title = line.strip('\n')		print 'PROCESS PAGE: ' + page_title		sys.stdout.flush()		page_titles.append(page_title)		# get data		if len(page_titles) == 10000:			extract_data(page_titles, mysql_cur, output_file)			page_titles = []	# last data	extract_data(page_titles, mysql_cur, output_file)input_file.close()output_file.close()print "Current date and time [FIN]: " , datetime.datetime.now()