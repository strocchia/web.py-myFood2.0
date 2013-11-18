from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def init_form (form, clearMessage):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<title>myFood2.0 - form</title>\n'])
    extend_([u'\n'])
    extend_([u'<form name="main" method="post">\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'</form>\n'])
    extend_([u'\n'])
    if clearMessage:
        extend_([u'    <b>', escape_(clearMessage, True), u'</b>\n'])
        extend_([u'\n'])
    extend_([u'<br></br>\n'])
    extend_([u'After entering data, go to <a href="/getcsv">myfood2p0.appspot.com/getcsv</a> to retrieve a personalized CSV file of your meal expenses.\n'])
    extend_([u'\n'])
    extend_([u'<br></br>\n'])
    extend_([u'<br></br>\n'])
    extend_([u'<font size="2">&copy; <i>Scott Trocchia (2013)</i> </font>\n'])

    return self

init_form = CompiledTemplate(init_form, 'templates/init_form.html')
join_ = init_form._join; escape_ = init_form._escape

# coding: utf-8
def init_form_bootstrap (clearMessage):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html lang="en">\n'])
    extend_([u'        <head>\n'])
    extend_([u'                <meta charset="utf-8">\n'])
    extend_([u'                <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'])
    extend_([u'                <meta name="description" content="">\n'])
    extend_([u'                    <meta name="author" content="">\n'])
    extend_([u'                        <!--link rel="shortcut icon" href="../static/img/favicon.png"-->\n'])
    extend_([u'                        \n'])
    extend_([u'                        <title>myFood2.0 - form</title>\n'])
    extend_([u'                        \n'])
    extend_([u'                        <!-- Bootstrap core CSS -->\n'])
    extend_([u'                        <link href="../static/bootstrap/css/bootstrap.css" rel="stylesheet">\n'])
    extend_([u'                            \n'])
    extend_([u'                            <style type="text/css">\n'])
    extend_([u'                                .bs-example{\n'])
    extend_([u'                                    margin: 20px;\n'])
    extend_([u'                                    width: 500px;\n'])
    extend_([u'                                }\n'])
    extend_([u'                            </style>\n'])
    extend_([u'        </head>\n'])
    extend_([u'\n'])
    extend_([u'    <body>\n'])
    extend_([u'        <div class="bs-example">\n'])
    extend_([u'        <form role="form" method="post">\n'])
    extend_([u'            <div class="form-group">\n'])
    extend_([u'                <label for="Username">User name</label>\n'])
    extend_([u'                <input type="text" name="Username" class="form-control" placeholder="Enter user name">\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="form-group">\n'])
    extend_([u'                <label for="Whichmeal">Which meal?</label> \n'])
    extend_([u'                <select id="Which meal?" name="Whichmeal" class="form-control">\n'])
    extend_([u'                    <option>Lunch</option>\n'])
    extend_([u'                    <option>Dinner</option>\n'])
    extend_([u'                    <option>Miscellaneous</option>\n'])
    extend_([u'                </select>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="form-group">\n'])
    extend_([u'                <label for="Month">Month</label>\n'])
    extend_([u'                <select id="Month" name="Month" class="form-control">\n'])
    extend_([u'                        <option>January</option>\n'])
    extend_([u'                        <option>February</option>\n'])
    extend_([u'                        <option>March</option>\n'])
    extend_([u'                        <option>April</option>\n'])
    extend_([u'                        <option>May</option>\n'])
    extend_([u'                        <option>June</option>\n'])
    extend_([u'                        <option>July</option>\n'])
    extend_([u'                        <option>August</option>\n'])
    extend_([u'                        <option>September</option>\n'])
    extend_([u'                        <option>October</option>\n'])
    extend_([u'                        <option>November</option>\n'])
    extend_([u'                        <option>December</option>\n'])
    extend_([u'                </select>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="form-group">\n'])
    extend_([u'                <label for="Day">Day</label>\n'])
    extend_([u'                <select id="Day" name="Day" class="form-control">\n'])
    extend_([u'                    <option>1</option>\n'])
    extend_([u'                    <option>2</option>\n'])
    extend_([u'                    <option>3</option>\n'])
    extend_([u'                    <option>4</option>\n'])
    extend_([u'                    <option>5</option>\n'])
    extend_([u'                    <option>6</option>\n'])
    extend_([u'                    <option>7</option>\n'])
    extend_([u'                    <option>8</option>\n'])
    extend_([u'                    <option>9</option>\n'])
    extend_([u'                    <option>10</option>\n'])
    extend_([u'                    <option>11</option>\n'])
    extend_([u'                    <option>12</option>\n'])
    extend_([u'                    <option>13</option>\n'])
    extend_([u'                    <option>14</option>\n'])
    extend_([u'                    <option>15</option>\n'])
    extend_([u'                    <option>16</option>\n'])
    extend_([u'                    <option>17</option>\n'])
    extend_([u'                    <option>18</option>\n'])
    extend_([u'                    <option>19</option>\n'])
    extend_([u'                    <option>20</option>\n'])
    extend_([u'                    <option>21</option>\n'])
    extend_([u'                    <option>22</option>\n'])
    extend_([u'                    <option>23</option>\n'])
    extend_([u'                    <option>24</option>\n'])
    extend_([u'                    <option>25</option>\n'])
    extend_([u'                    <option>26</option>\n'])
    extend_([u'                    <option>27</option>\n'])
    extend_([u'                    <option>28</option>\n'])
    extend_([u'                    <option>29</option>\n'])
    extend_([u'                    <option>30</option>\n'])
    extend_([u'                    <option>31</option>\n'])
    extend_([u'                </select>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="form-group">\n'])
    extend_([u'                <label for="Year">Year</label> \n'])
    extend_([u'                <select id="Year" name="Year" class="form-control">\n'])
    extend_([u'                    <option>2013</option>\n'])
    extend_([u'                    <option>2014</option>\n'])
    extend_([u'                    <option>2015</option>\n'])
    extend_([u'                    <option>2016</option>\n'])
    extend_([u'                </select>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="form-group">\n'])
    extend_([u'                <label for="LDM">Lunch, Dinner, or Miscellaneous &#36;</label>\n'])
    extend_([u'                <input type="number" name="LDM" class="form-control" placeholder="Enter money spent for particular meal">\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="form-group">\n'])
    extend_([u'                <label for="Clear">Clear? (y/n)</label>\n'])
    extend_([u'                <input type="text" name="Clear" class="form-control" placeholder="Enter \'y\' or \'n\' (without quotes)">\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="form-group">\n'])
    extend_([u'                <button type="submit" name="Submit" class="btn btn-primary">Submit</button>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            \n'])
    if clearMessage:
        extend_(['            ', u'<b>', escape_(clearMessage, True), u'</b>\n'])
        extend_(['            ', u'\n'])
    extend_([u'            <br></br>\n'])
    extend_([u'            After entering data, go to <a href="/getcsv">myfood2p0.appspot.com/getcsv</a> to retrieve a personalized CSV file of your meal expenses.\n'])
    extend_([u'            \n'])
    extend_([u'            <br></br>\n'])
    extend_([u'            <br></br>\n'])
    extend_([u'            <font size="2">&copy; <i>Scott Trocchia (2013)</i> </font>\n'])
    extend_([u'        \n'])
    extend_([u'            </form>    \n'])
    extend_([u'        </div>\n'])
    extend_([u'                    \n'])
    extend_([u'    <script src="../static/bootstrap/js/jquery.js"></script>    \n'])
    extend_([u'    <script src="../static/bootstrap/js/bootstrap.min.js"></script>\n'])
    extend_([u'    </body>\n'])
    extend_([u'</html>    \n'])

    return self

init_form_bootstrap = CompiledTemplate(init_form_bootstrap, 'templates/init_form_bootstrap.html')
join_ = init_form_bootstrap._join; escape_ = init_form_bootstrap._escape

# coding: utf-8
def nothing_to_show (nothingMessage):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<html>\n'])
    extend_([u'<p style="font-size: 150%;"> <b>', escape_(nothingMessage, True), u'</b> </p>\n'])
    extend_([u'</html>\n'])

    return self

nothing_to_show = CompiledTemplate(nothing_to_show, 'templates/nothing_to_show.html')
join_ = nothing_to_show._join; escape_ = nothing_to_show._escape

# coding: utf-8
def returned_data (currentMonth, CSVrows, Ltot_thisMonth, Dtot_thisMonth, Mtot_thisMonth, Ltot_All, Dtot_All, Mtot_All):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<title>myFood2.0 - tabulated</title>\n'])
    if CSVrows:
        extend_([u'    <table border="1">\n'])
        extend_([u'    <tr>\n'])
        extend_([u'            <th> Date </th>\n'])
        extend_([u'            <th> Lunch </th>\n'])
        extend_([u'            <th> Dinner </th>\n'])
        extend_([u'            <th> Miscellaneous </th>\n'])
        extend_([u'    </tr>\n'])
        for row in loop.setup(CSVrows):
            extend_(['    ', u'    <tr>\n'])
            extend_(['    ', u'            <td> ', escape_(row[0], True), u' </td>\n'])
            extend_(['    ', u'            <td> ', escape_(row[1], True), u' </td>\n'])
            extend_(['    ', u'            <td> ', escape_(row[2], True), u' </td>\n'])
            extend_(['    ', u'            <td> ', escape_(row[3], True), u' </td>\n'])
            extend_(['    ', u'    </tr>\n'])
        extend_([u'    </table>\n'])
        extend_([u'\n'])
    extend_([u'<p>\n'])
    if Ltot_thisMonth or Dtot_thisMonth or Mtot_thisMonth:
        extend_([u'    <br> <i><u>CURRENT MONTH TOTALS:</u></i> </br>\n'])
    extend_([u'<br>\n'])
    if Ltot_thisMonth:
        extend_([u'    Lunch total for this month (', escape_(currentMonth, True), u') = &#36;', escape_(Ltot_thisMonth, True), u'\n'])
    extend_([u'</br>\n'])
    extend_([u'<br>\n'])
    if Dtot_thisMonth:
        extend_([u'    Dinner total for this month (', escape_(currentMonth, True), u') = &#36;', escape_(Dtot_thisMonth, True), u'\n'])
    extend_([u'</br>\n'])
    extend_([u'<br>\n'])
    if Mtot_thisMonth:
        extend_([u'    Miscellaneous total for this month (', escape_(currentMonth, True), u') = &#36;', escape_(Mtot_thisMonth, True), u'\n'])
    extend_([u'</br>\n'])
    extend_([u'<br></br>\n'])
    if Ltot_All or Dtot_All or Mtot_All:
        extend_([u'    <br> <i><u>ALL MONTH TOTALS:</u></i> </br>\n'])
    extend_([u'<br>\n'])
    if Ltot_All:
        extend_([u'    Lunch total for all months = &#36;', escape_(Ltot_All, True), u'\n'])
    extend_([u'</br>\n'])
    extend_([u'<br>\n'])
    if Dtot_All:
        extend_([u'    Dinner total for all months = &#36;', escape_(Dtot_All, True), u'\n'])
    extend_([u'</br>\n'])
    extend_([u'<br>\n'])
    if Mtot_All:
        extend_([u'    Miscellaneous total for all months = &#36;', escape_(Mtot_All, True), u'\n'])
    extend_([u'</br>\n'])
    extend_([u'</p>\n'])

    return self

returned_data = CompiledTemplate(returned_data, 'templates/returned_data.html')
join_ = returned_data._join; escape_ = returned_data._escape

# coding: utf-8
def returned_data_bootstrap (currentMonth, CSVrows, Ltot_thisMonth, Dtot_thisMonth, Mtot_thisMonth, Ltot_All, Dtot_All, Mtot_All):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html lang="en">\n'])
    extend_([u'        <head>\n'])
    extend_([u'                <meta charset="utf-8">\n'])
    extend_([u'                <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'])
    extend_([u'                <meta name="description" content="">\n'])
    extend_([u'                <meta name="author" content="">\n'])
    extend_([u'                <!--link rel="shortcut icon" href="../static/img/favicon.png"-->\n'])
    extend_([u'                            \n'])
    extend_([u'                <title>myFood2.0 - tabulated</title>\n'])
    extend_([u'                            \n'])
    extend_([u'                <!-- Bootstrap core CSS -->\n'])
    extend_([u'                <link href="../static/bootstrap/css/bootstrap.css" rel="stylesheet">\n'])
    extend_([u'                                    \n'])
    extend_([u'                <style type="text/css">\n'])
    extend_([u'                        .bs-example{\n'])
    extend_([u'                                margin: 20px;\n'])
    extend_([u'                        }\n'])
    extend_([u'                </style>\n'])
    extend_([u'        </head>\n'])
    extend_([u'        <body>\n'])
    extend_([u'                        <div class="bs-example">\n'])
    extend_([u'                                <table class="table table-striped">\n'])
    extend_([u'                                        <thead>\n'])
    extend_([u'                                                <tr>\n'])
    extend_([u'                                                <th>Date</th>\n'])
    extend_([u'                                                <th>Lunch</th>\n'])
    extend_([u'                                                <th>Dinner</th>\n'])
    extend_([u'                                                <th>Miscellaneous</th>\n'])
    extend_([u'                                                </tr>\n'])
    extend_([u'                                        </thead>\n'])
    extend_([u'                                        <tbody>\n'])
    for row in loop.setup(CSVrows):
        extend_(['                                        ', u'    <tr>\n'])
        extend_(['                                        ', u'    <td>', escape_(row[0], True), u'</td>\n'])
        extend_(['                                        ', u'    <td>', escape_(row[1], True), u'</td>\n'])
        extend_(['                                        ', u'    <td>', escape_(row[2], True), u'</td>\n'])
        extend_(['                                        ', u'    <td>', escape_(row[3], True), u'</td>\n'])
        extend_(['                                        ', u'    </tr>\n'])
    extend_([u'                                        </tbody>\n'])
    extend_([u'                                </table>\n'])
    extend_([u'\n'])
    if Ltot_thisMonth or Dtot_thisMonth or Mtot_thisMonth:
        extend_(['                                ', u'    <br> <i><u>CURRENT MONTH TOTALS:</u></i> </br>\n'])
    extend_([u'                                <br>\n'])
    if Ltot_thisMonth:
        extend_(['                                ', u'    Lunch total for this month (', escape_(currentMonth, True), u') = &#36;', escape_(Ltot_thisMonth, True), u'\n'])
    extend_([u'                                </br>\n'])
    extend_([u'                                <br>\n'])
    if Dtot_thisMonth:
        extend_(['                                ', u'    Dinner total for this month (', escape_(currentMonth, True), u') = &#36;', escape_(Dtot_thisMonth, True), u'\n'])
    extend_([u'                                </br>\n'])
    extend_([u'                                <br>\n'])
    if Mtot_thisMonth:
        extend_(['                                ', u'    Miscellaneous total for this month (', escape_(currentMonth, True), u') = &#36;', escape_(Mtot_thisMonth, True), u'\n'])
    extend_([u'                                </br>\n'])
    extend_([u'                                <br></br>\n'])
    if Ltot_All or Dtot_All or Mtot_All:
        extend_(['                                ', u'    <br> <i><u>ALL MONTH TOTALS:</u></i> </br>\n'])
    extend_([u'                                <br>\n'])
    if Ltot_All:
        extend_(['                                ', u'    Lunch total for all months = &#36;', escape_(Ltot_All, True), u'\n'])
    extend_([u'                                </br>\n'])
    extend_([u'                                <br>\n'])
    if Dtot_All:
        extend_(['                                ', u'    Dinner total for all months = &#36;', escape_(Dtot_All, True), u'\n'])
    extend_([u'                                </br>\n'])
    extend_([u'                                <br>\n'])
    if Mtot_All:
        extend_(['                                ', u'    Miscellaneous total for all months = &#36;', escape_(Mtot_All, True), u'\n'])
    extend_([u'                                </br>\n'])
    extend_([u'                                </p>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                <script src="../static/bootstrap/js/jquery.js"></script>        \n'])
    extend_([u'                <script src="../static/bootstrap/js/bootstrap.min.js"></script>\n'])
    extend_([u'        </body>\n'])
    extend_([u'</html>\n'])

    return self

returned_data_bootstrap = CompiledTemplate(returned_data_bootstrap, 'templates/returned_data_bootstrap.html')
join_ = returned_data_bootstrap._join; escape_ = returned_data_bootstrap._escape

# coding: utf-8
def tutorial (name):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    if name:
        extend_([u'    I just wanted to say <em>hello</em> to ', escape_(name, True), u'\n'])
        extend_([u'\n'])
    else:
        extend_([u'    <em>Hello</em>, world!\n'])
        extend_([u'\n'])
    extend_([u'<form>\n'])
    extend_([u'        <input text="Scott">\n'])
    extend_([u'        <input type="submit">\n'])
    extend_([u'</form>\n'])

    return self

tutorial = CompiledTemplate(tutorial, 'templates/tutorial.html')
join_ = tutorial._join; escape_ = tutorial._escape

