import csv
import tempfile
import shutil

#inputs appropriate file from same folder
input_file = '2013_percentage.csv'

#opens input_file and temporary file, where it will write results
with open(input_file, 'rb') as f, \
	tempfile.NamedTemporaryFile(delete=False) as out_f:

#In order to be able to not have to read everything in memory, we have to write every processed row to disk immediately.
#For that, we need a temporary file because we can't read and write a single file at the same time.
	reader = csv.reader(f)
	writer = csv.writer(out_f)

#Header row
	writer.writerow(next(reader) + ["2013_percentage"])	

#Try/Except block prevents the code from stopping at every string, since there are strings in the csvs.
	for row in reader:
		try:
			val1 = float(row[3])
			val2 = float(row[1])
			writer.writerows([row + [val1 / val2 * 100]])
		except ValueError:
			print('There are strings in this file.')

# with open(input_file, 'wb') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerow(["Participating_states", "Number_of_participating_agencies", "Population_covered", "Agencies_submitting_incident_reports", "Total_number_of_incidents_reported", "Reporting_percentage"])

#Overwrites original file with new content.
shutil.move(out_f.name, input_file)