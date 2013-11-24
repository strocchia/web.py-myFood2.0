import web
web.config.debug = False
from web import form
import datetime
import time
import csv
from StringIO import StringIO
from collections import defaultdict

urls = (
	"/", "index",
	"/getcsv", "getcsv",
	"/nothingInCSV", "nothingInCSV"
)

render = web.template.render('templates/')

app = web.application(urls, globals())

#users_store = web.session.Session(app, web.session.DiskStore('users_store'), initializer={'double_dict': defaultdict(dict)})

double_dict = defaultdict(dict)

class index:

	def POST(self):
		allFormInputs = web.input()
		print allFormInputs

		global user, clearFlag, undoFlag
		clearFlag = 0
		mealType = ""
		
		user = allFormInputs.Username
		mealType = allFormInputs.Whichmeal
		
		chosen_date = allFormInputs.MDY
		chosen_date = chosen_date.split('/')
		Month = chosen_date[0]
		Day = chosen_date[1]
		Year = chosen_date[2]		

		currentMonth = datetime.datetime.now().month
		monthDict={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
		currentMonth = monthDict[currentMonth]
		Month = monthDict[int(Month)]

		print ""	
		print "DD immediately after POST called: %s" % double_dict

		if allFormInputs.buttonDo == "Clear your database":
			print "In the clear"
			clearFlag = 1
			double_dict[user].clear()
			double_dict[user]['dateList'] = []
			double_dict[user]['lunchList'] = []
			double_dict[user]['dinnerList'] = []
			double_dict[user]['miscList'] = []
			double_dict[user]['CSVrows'] = []
			double_dict[user]['Ltot_thisMonth'] = 0.00
			double_dict[user]['Dtot_thisMonth'] = 0.00
			double_dict[user]['Mtot_thisMonth'] = 0.00
			double_dict[user]['Ltot_All'] = 0.00
			double_dict[user]['Dtot_All'] = 0.00
			double_dict[user]['Mtot_All'] = 0.00
			clearMessage = "Your personal meal expense database is cleared!"
			print "DD after clear: %s" % double_dict
			return render.init_form_bootstrap_jquery(clearFlag)

		elif allFormInputs.buttonDo == "Undo last entry":
			print "Undo phase"
			if mealType == "Lunch":
				print "undo lunch"
				last_L_entry = float(double_dict[user]['Ltot_All'])
				double_dict[user]['lunchList'] = double_dict[user]['lunchList'][:-1]
				double_dict[user]['Ltot_All'] -= last_L_entry
				if Month == currentMonth:
					double_dict[user]['Ltot_thisMonth'] -= last_L_entry
			if mealType == "Dinner":
				print "undo dinner"
				last_D_entry = float(double_dict[user]['Dtot_All'])
				double_dict[user]['dinnerList'] = double_dict[user]['dinnerList'][:-1]
				double_dict[user]['Dtot_All'] -= last_D_entry
				if Month == currentMonth:
					double_dict[user]['Dtot_thisMonth'] -= last_D_entry
			if mealType == "Miscellaneous":
				print "undo misc"
				last_M_entry = float(double_dict[user]['Mtot_All'])
				double_dict[user]['miscList'] = double_dict[user]['miscList'][:-1]
				double_dict[user]['Mtot_All'] -= last_M_entry
				if Month == currentMonth:
					double_dict[user]['Mtot_thisMonth'] -= last_M_entry

			double_dict[user]['CSVrows'] = map(None, double_dict[user]['dateList'], double_dict[user]['lunchList'], double_dict[user]['dinnerList'], double_dict[user]['miscList'])
	
			return render.returned_data_bootstrap(currentMonth, double_dict[user]['CSVrows'], double_dict[user]['Ltot_thisMonth'], double_dict[user]['Dtot_thisMonth'], double_dict[user]['Mtot_thisMonth'], double_dict[user]['Ltot_All'], double_dict[user]['Dtot_All'], double_dict[user]['Mtot_All'])
			print "DD CSVrows after undo: %s" % double_dict[user]['CSVrows']
	
		else:
		### saving convenient values to make it easier to reference them in future parts of the code
			print "saving data phase"
			LDM = allFormInputs.LDM
			LDM = float(LDM)	
			
			#joined_date = ' '.join([chosen_month, allFormInputs.Day, allFormInputs.Year])
			joined_date = ' '.join([Month, Day, Year])

			print 'DD b4: %s' % double_dict

			if not user in double_dict:
				### create the nested dict fields
				double_dict[user]['dateList'] = []
				double_dict[user]['lunchList'] = []
				double_dict[user]['dinnerList'] = []
				double_dict[user]['miscList'] = []
				double_dict[user]['CSVrows'] = []
				double_dict[user]['Ltot_thisMonth'] = 0.00
				double_dict[user]['Dtot_thisMonth'] = 0.00
				double_dict[user]['Mtot_thisMonth'] = 0.00
				double_dict[user]['Ltot_All'] = 0.00
				double_dict[user]['Dtot_All'] = 0.00
				double_dict[user]['Mtot_All'] = 0.00
			else:
				print "User already exists!"
			
			### add to those fields
			
			if not joined_date in double_dict[user]['dateList']:
				double_dict[user]['dateList'].append(joined_date)
				
			if mealType == "Lunch":
				double_dict[user]['lunchList'].append(LDM)
				double_dict[user]['Ltot_All'] += LDM
				if Month == currentMonth:
					double_dict[user]['Ltot_thisMonth'] += LDM
			elif mealType == "Dinner":
				double_dict[user]['dinnerList'].append(LDM)
				double_dict[user]['Dtot_All'] += LDM
				if Month == currentMonth:
					double_dict[user]['Dtot_thisMonth'] += LDM	
			elif mealType == "Miscellaneous":
				double_dict[user]['miscList'].append(LDM)
				double_dict[user]['Mtot_All'] += LDM
				if Month == currentMonth:
					double_dict[user]['Mtot_thisMonth'] += LDM
			else:
				print ""

			print 'DD after: %s' % double_dict
			
			double_dict[user]['CSVrows'] = map(None, double_dict[user]['dateList'], double_dict[user]['lunchList'], double_dict[user]['dinnerList'], double_dict[user]['miscList'])
				
			print 'DD CSVrows: %s' % double_dict[user]['CSVrows']
			print ""			
		
			return render.returned_data_bootstrap(currentMonth, double_dict[user]['CSVrows'], double_dict[user]['Ltot_thisMonth'], double_dict[user]['Dtot_thisMonth'], double_dict[user]['Mtot_thisMonth'], double_dict[user]['Ltot_All'], double_dict[user]['Dtot_All'], double_dict[user]['Mtot_All'])

	def GET(self):
		return render.init_form_bootstrap_jquery(0)


### --> Render and generate a CSV file, which includes all user input information up to this point in time
class getcsv:

	def GET(self):

		global user, clearFlag

		if clearFlag == 1:
 			raise web.seeother('/nothingInCSV')
		else:
			csv_file = StringIO()
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(['Date', 'Lunch', 'Dinner', 'Miscellaneous'])
			for i in double_dict[user]['CSVrows']:
				csv_writer.writerow(i)
						
			currentDate = datetime.datetime.today().strftime('%m-%d-%Y')
			web.header('Content-Type', 'text/csv')
			web.header('Content-disposition', 'attachment; filename=MYFOOD_' + user.upper() + '_' + currentDate + '.csv')			
			return csv_file.getvalue()


class nothingInCSV:

	def GET(self):

		nothingMessage = "You have not entered any data into your personal CSV file!"
		return render.nothing_to_show(nothingMessage)


app = app.gaerun()
