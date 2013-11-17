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

foodForm = form.Form(
	form.Textbox('User name', web.form.notnull),
	form.Dropdown('Which meal?', ['Lunch', 'Dinner', 'Miscellaneous']),
	form.Dropdown('Month', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
	form.Dropdown('Day', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']),
	form.Dropdown('Year', ['2013', '2014', '2015', '2016']),
        form.Textbox('Lunch, Dinner, or Miscellaneous $'),
	form.Textbox('Clear? (y/n)')
)

#users_store = web.session.Session(app, web.session.DiskStore('users_store'), initializer={'double_dict': defaultdict(dict)})

double_dict = defaultdict(dict)

class index:

	def POST(self):
		form = foodForm()
		
		if not form.validates():
			return render.init_form(form, "")
		else:
			global user
			clearMessage = ""

			if form['Clear? (y/n)'].value == 'y':
				#users_store['double_dict'].clear()
				double_dict.clear()
				clearMessage = "Your personal meal expense database is cleared!"
				return render.init_form(form, clearMessage)
	
			else:
				### saving convenient values to make it easier to reference them in future parts of the code
				user = form['User name'].value
				mealType= form['Which meal?'].value
				chosen_month  = form['Month'].value
				LDM = float(form['Lunch, Dinner, or Miscellaneous $'].value)

				currentMonth = datetime.datetime.now().month
				monthDict={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
				currentMonth = monthDict[currentMonth]
				
				joined_date = ' '.join([chosen_month, form['Day'].value, form['Year'].value])	

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
					if chosen_month == currentMonth:
						double_dict[user]['Ltot_thisMonth'] += LDM
				elif mealType == "Dinner":
					double_dict[user]['dinnerList'].append(LDM)
					double_dict[user]['Dtot_All'] += LDM
					if chosen_month == currentMonth:
						double_dict[user]['Dtot_thisMonth'] += LDM
				else:
					double_dict[user]['miscList'].append(LDM)
					double_dict[user]['Mtot_All'] += LDM
					if chosen_month == currentMonth:
						double_dict[user]['Mtot_thisMonth'] += LDM
				
				print 'DD after: %s' % double_dict

				double_dict[user]['CSVrows'] = map(None, double_dict[user]['dateList'], double_dict[user]['lunchList'], double_dict[user]['dinnerList'], double_dict[user]['miscList'])
	
				print 'CSVrows: %s' % double_dict[user]['CSVrows']
				
				#return render.returned_data(currentMonth, double_dict[user]['CSVrows'], double_dict[user]['Ltot_thisMonth'], double_dict[user]['Dtot_thisMonth'], double_dict[user]['Mtot_thisMonth'], double_dict[user]['Ltot_All'], double_dict[user]['Dtot_All'], double_dict[user]['Mtot_All'])
				return render.returned_data_bootstrap(currentMonth, double_dict[user]['CSVrows'], double_dict[user]['Ltot_thisMonth'], double_dict[user]['Dtot_thisMonth'], double_dict[user]['Mtot_thisMonth'], double_dict[user]['Ltot_All'], double_dict[user]['Dtot_All'], double_dict[user]['Mtot_All'])

	def GET(self):
		form = foodForm()
		return render.init_form(form, "")


### --> Render and generate a CSV file, which includes all user input information up to this point in time
class getcsv:

	def GET(self):

		global user

		if len(double_dict) == 0:
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
