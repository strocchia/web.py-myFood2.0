import web
web.config.debug = False
from web import form
import datetime
import time
import csv
from StringIO import StringIO

urls = (
	"/*", "index",
	"/getcsv", "getcsv"
)

render = web.template.render('templates/')

app = web.application(urls, globals())

foodForm = form.Form(
	form.Textbox('User name'),
	form.Dropdown('Which meal?', ['Lunch', 'Dinner', 'Miscellaneous']),
	form.Dropdown('Month', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
	form.Dropdown('Day', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']),
	form.Dropdown('Year', ['2013', '2014', '2015', '2016']),
        form.Textbox('Lunch, Dinner, or Miscellaneous $'),
	form.Textbox('Clear? (y/n)')
)

userList = []
dateList = []
lunchList = []
dinnerList = []
miscList = []
CSVrows = []

session = dict()
session['mealType'] = ''
session['chosen_month'] = ''
session['user'] = ''

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
			global userList, dateList, lunchList, dinnerList, miscList, CSVrows, Ltot_thisMonth, Dtot_thisMonth, Mtot_thisMonth, Ltot_All, Dtot_All, Mtot_All

			#print form['Clear? (y/n)'].value

			if form['Clear? (y/n)'].value == 'y':
				Ltot_thisMonth = 0.0
				Dtot_thisMonth = 0.0
				Mtot_thisMonth = 0.0
				Ltot_All = 0.0
				Dtot_All = 0.0
				Mtot_All = 0.0
				session.clear()
				userList = []
				dateList = []
				lunchList = []
				dinnerList = []
				miscList = []
				CSVrows = []
				return render.init_form(form)
		
			else:
				currentUser = form['User name'].value
				if not currentUser in userList:
					userList.append(currentUser)

				session['mealType'] = form['Which meal?'].value
				session['chosen_month'] = form['Month'].value
				currentMonth = datetime.datetime.now().month
				monthDict={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
				currentMonth = monthDict[currentMonth]

				LDM = float(form['Lunch, Dinner, or Miscellaneous $'].value)

				if session['mealType'] == 'Lunch':
					lunchList.append(LDM)
					Ltot_All += LDM
					if session['chosen_month'] == currentMonth:
						Ltot_thisMonth += LDM
				elif session['mealType'] == 'Dinner':
					dinnerList.append(LDM)
					Dtot_All += LDM
					if session['chosen_month'] == currentMonth:
						Dtot_thisMonth += LDM
				else:
					miscList.append(LDM)
					Mtot_All += LDM
					if session['chosen_month'] == currentMonth:
						Mtot_thisMonth += LDM

				joined_date = ' '.join([form['Month'].value, form['Day'].value, form['Year'].value])	

				if not joined_date in dateList:
					dateList.append(joined_date)

				CSVrows = map(None, dateList, lunchList, dinnerList, miscList)
			
				return render.returned_data(CSVrows, currentMonth, Ltot_thisMonth, Dtot_thisMonth, Mtot_thisMonth, Ltot_All, Dtot_All, Mtot_All)

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
		for i in CSVrows:
			csv_writer.writerow(i)

		currentDate = datetime.datetime.today().strftime('%m-%d-%Y')
		web.header('Content-Type', 'text/csv')
		web.header('Content-disposition', 'attachment; filename=myFood_' + currentDate + '.csv')			
		return csv_file.getvalue()

app = app.gaerun()
