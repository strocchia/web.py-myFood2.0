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
	"/getcsv", "getcsv"
	#"/userI", "userI"
)

render = web.template.render('templates/')

app = web.application(urls, globals())

foodForm = form.Form(
	form.Textbox('User name', web.form.notnull),
	form.Dropdown('Which meal?', ['Lunch', 'Dinner', 'Miscellaneous']),
	form.Dropdown('Month', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
	form.Dropdown('Day', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']),
	form.Dropdown('Year', ['2013', '2014', '2015', '2016']),
        form.Textbox('Lunch, Dinner, or Miscellaneous $'),
	form.Textbox('Clear? (y/n)')
)

#session = web.session.Session(app, web.session.DiskStore('sessions'))
#myUserDict = web.session.Session(app, web.session.DiskStore('userdicts'))
#user_store = web.session.Session(app, web.session.DiskStore('user_store'))

#fromform = dict()
#fromform['mealType'] = ''
#fromform['chosen_month'] = ''

double_dict = defaultdict(dict)
userList = []
CSVrows = []

Ltot_thisMonth = 0.0
Dtot_thisMonth = 0.0
Mtot_thisMonth = 0.0
Ltot_All = 0.0
Dtot_All = 0.0
Mtot_All = 0.0

class index:

	def POST(self):
		form = foodForm()
		
		if not form.validates():
			return render.init_form(form)
		else:
			global userList, CSVrows, Ltot_thisMonth, Dtot_thisMonth, Mtot_thisMonth, Ltot_All, Dtot_All, Mtot_All

			if form['Clear? (y/n)'].value == 'y':
			#	Ltot_thisMonth = 0.0
			#	Dtot_thisMonth = 0.0
			#	Mtot_thisMonth = 0.0
			#	Ltot_All = 0.0
			#	Dtot_All = 0.0
			#	Mtot_All = 0.0
			#	fromform.clear()
			#	userList = []
			#	dateList = []
			#	lunchList = []
			#	dinnerList = []
			#	miscList = []
			#	CSVrows = []
				return render.init_form(form)
		
			else:
				# saving convenient values to make it easier to reference them in future parts of the code
				username = form['User name'].value
				mealType= form['Which meal?'].value
				chosen_month  = form['Month'].value
				LDM = float(form['Lunch, Dinner, or Miscellaneous $'].value)

				currentMonth = datetime.datetime.now().month
				monthDict={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
				currentMonth = monthDict[currentMonth]
				
				joined_date = ' '.join([chosen_month, form['Day'].value, form['Year'].value])	

				print 'DD b4: %s' % double_dict

				if username not in double_dict:
					# create the nested dict fields
					double_dict[username]['dateList'] = []
					double_dict[username]['lunchList'] = []
					double_dict[username]['dinnerList'] = []
					double_dict[username]['miscList'] = []
					double_dict[username]['Ltot_All'] = ['0']
				else:
					print "User already exists!"
				
				# add to those fields
				if not joined_date in double_dict[username]['dateList']:
					double_dict[username]['dateList'].append(joined_date)
				if mealType == "Lunch":
					double_dict[username]['lunchList'].append(LDM)
					last_L_entry = float(double_dict[username]['Ltot_All'][-1])
					#print last_L_entry
					double_dict[username]['Ltot_All'].append(str(last_L_entry + LDM))
				elif mealType == "Dinner":
					double_dict[username]['dinnerList'].append(LDM)
				else:
					double_dict[username]['miscList'].append(LDM)

				print 'DD after: %s' % double_dict

				#myUserDict['username'] = form['User name'].value	
				#if not myUserDict['username'] in userList:
				#	userList.append(myUserDict['username'])

				#if mealType == 'Lunch':
					#lunchList.append(LDM)
				#	Ltot_All += LDM
				#	if chosen_month == currentMonth:
				#		Ltot_thisMonth += LDM
				#elif mealType == 'Dinner':
				#	#dinnerList.append(LDM)
				#	Dtot_All += LDM
				#	if chosen_month == currentMonth:
				#		Dtot_thisMonth += LDM
				#else:
				#	#miscList.append(LDM)
				#	Mtot_All += LDM
				#	if chosen_month == currentMonth:
				#		Mtot_thisMonth += LDM

				#CSVrows = map(None, dateList, lunchList, dinnerList, miscList)
	
				#return render.returned_data(CSVrows, currentMonth, Ltot_thisMonth, Dtot_thisMonth, Mtot_thisMonth, Ltot_All, Dtot_All, Mtot_All)

	def GET(self):
		form = foodForm()
		return render.init_form(form)


""" Render and generate a CSV file, which includes all user input information up to this point in time """
class getcsv:

	def GET(self):
	
		global CSVrows

		csv_file = StringIO()
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['Date', 'Lunch', 'Dinner', 'Miscellaneous'])
		#for i in CSVrows:
		#	csv_writer.writerow(i)

		currentDate = datetime.datetime.today().strftime('%m-%d-%Y')
		web.header('Content-Type', 'text/csv')
		web.header('Content-disposition', 'attachment; filename=myFood_' + currentDate + '.csv')			
		return csv_file.getvalue()


app = app.gaerun()
