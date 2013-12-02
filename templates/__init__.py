from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def csv_page():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html lang="en">\n'])
    extend_([u'<head>\n'])
    extend_([u'        <meta charset="utf-8">\n'])
    extend_([u'\n'])
    extend_([u'        <style text="text/css">\n'])
    extend_([u'                .csv-example {\n'])
    extend_([u'                        margin: 20px;\n'])
    extend_([u'                        width: 500px;\n'])
    extend_([u'                {\n'])
    extend_([u'        </style>\n'])
    extend_([u'</head>\n'])
    extend_([u'        <div class="csv-example">\n'])
    extend_([u'                <form role="form" method="post">\n'])
    extend_([u'                        <label for="user">User name (same as main page)</label>\n'])
    extend_([u'                        <input type="text" name="user">\n'])
    extend_([u'                        <input type="submit">\n'])
    extend_([u'                </form>\n'])
    extend_([u'</html>\n'])

    return self

csv_page = CompiledTemplate(csv_page, 'templates/csv_page.html')
join_ = csv_page._join; escape_ = csv_page._escape

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
def init_form_bootstrap_jquery (clearFlag):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html lang="en">\n'])
    extend_([u'\n'])
    extend_([u'<head>\n'])
    extend_([u'        <meta charset="utf-8">\n'])
    extend_([u'        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'])
    extend_([u'        <meta name="description" content="">\n'])
    extend_([u'        <meta name="author" content="">  \n'])
    extend_([u'\n'])
    extend_([u'        <title>myFood 2.0 - form</title>\n'])
    extend_([u'        <link rel="stylesheet" href="../static/bootstrap/css/bootstrap.css">\n'])
    extend_([u'  \n'])
    extend_([u'        <link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css">\n'])
    extend_([u'        <script src="http://code.jquery.com/jquery-1.9.1.js"></script>\n'])
    extend_([u'        <script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>\n'])
    extend_([u'        <link rel="stylesheet" href="/resources/demos/style.css">\n'])
    extend_([u'        <script type="text/javascript">\n'])
    extend_([u'        jQuery(function() {\n'])
    extend_([u'                jQuery( "#datepicker" ).datepicker();\n'])
    extend_([u'                jQuery( "#datepicker" ).datepicker("setDate", new Date()); \n'])
    extend_([u'        });\n'])
    extend_([u'        </script>\n'])
    extend_([u'\n'])
    extend_([u'                <style text="text/css">\n'])
    extend_([u'                        .bs-example {\n'])
    extend_([u'                                margin: 20px;\n'])
    extend_([u'                                width: 500px;\n'])
    extend_([u'                        }\n'])
    extend_([u'                </style>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'\n'])
    extend_([u'        <div class="bs-example">\n'])
    extend_([u'                <form role="form" method="post">\n'])
    extend_([u'                        <div class="form-group">\n'])
    extend_([u'                                <label for="Username">User name</label>\n'])
    extend_([u'                                <input type="text" name="Username" class="form-control" placeholder="Enter user name" required>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                        <div class="form-group">\n'])
    extend_([u'                                <label for="Whichmeal">Which meal?</label>\n'])
    extend_([u'                                <select name="Whichmeal" class="form-control">\n'])
    extend_([u'                                        <option>Lunch</option>\n'])
    extend_([u'                                        <option>Dinner</option>\n'])
    extend_([u'                                        <option>Miscellaneous</option>\n'])
    extend_([u'                                </select>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                        <div class="form-group">\n'])
    extend_([u'                                <label for="MDY">Date on which you consumed meal</label>\n'])
    extend_([u'                                <input type="text" name="MDY" id="datepicker" class="form-control" placeholder="Click this box, enter date on which you spent &#36; on specified meal">\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                        <div class="form-group">\n'])
    extend_([u'                                <label for="LDM">Lunch, Dinner, or Miscellaneous &#36;</label>\n'])
    extend_([u'                                <input type="tel" name="LDM" class="form-control" placeholder="Enter money spent for specified meal">\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                        <div class="form-group">\n'])
    extend_([u'                                <input type="submit" name="buttonDo" value="Submit" class="btn btn-primary">\n'])
    extend_([u'                                <input type="submit" name="buttonDo" value="Clear your database" class="btn btn-primary">\n'])
    extend_([u'                                <input type="submit" name="buttonDo" value="Undo last entry" class="btn btn-primary">\n'])
    extend_([u'                                <input type="submit" name="buttonDo" value="Get CSV" class="btn btn-primary">\n'])
    extend_([u'                        </div>\n'])
    extend_([u'\n'])
    if clearFlag == 1:
        extend_(['                        ', u'    <b>Your personal meal expense database is cleared!</b>\n'])
        extend_(['                        ', u'\n'])
    extend_([u'                        <br></br>\n'])
    extend_([u'                        <br></br>\n'])
    extend_([u'                        <b>INSTRUCTIONS:</b>\n'])
    extend_([u'                        <br>- Submit: submits your entire form\n'])
    extend_([u'                        <br>-- Clear: clears your entire personal database\n'])
    extend_([u'                        <br>--- Undo: clears the last entry for a particular chosen meal type\n'])
    extend_([u'                        <br>---- Get CSV: retrieves a personalized CSV file of your meal expenses. Only push this button <i>after</i> you have entered at least one meal entry. \n'])
    extend_([u'\n'])
    extend_([u'                        <br></br>\n'])
    extend_([u'                        <br></br>\n'])
    extend_([u'                        <font size="2">&copy; <i>Scott Trocchia (2013)</i> </font>\n'])
    extend_([u'\n'])
    extend_([u'                </form>\n'])
    extend_([u'        </div>\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

init_form_bootstrap_jquery = CompiledTemplate(init_form_bootstrap_jquery, 'templates/init_form_bootstrap_jquery.html')
join_ = init_form_bootstrap_jquery._join; escape_ = init_form_bootstrap_jquery._escape

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
def plot_jquery_test():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html lang="en">\n'])
    extend_([u'<head>\n'])
    extend_([u'        <h1> Hello </h1>\n'])
    extend_([u'        <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jquery.js"></script>   \n'])
    extend_([u'        <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jquery.min.js"></script>\n'])
    extend_([u'        <!--script language="javascript" type="text/javascript" src="../static/bootstrap/js/jquery.flot.js"></script-->\n'])
    extend_([u'        <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jquery.jqplot.min.js"></script>\n'])
    extend_([u'        <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.canvasAxisLabelRenderer.min.js"></script>\n'])
    extend_([u'        <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.canvasTextRenderer.min.js"></script>\n'])
    extend_([u'        <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.dateAxisRenderer.min.js"></script>\n'])
    extend_([u'\n'])
    extend_([u'        <script type="text/javascript">\n'])
    extend_([u'        jQuery(document).ready(function() {\n'])
    extend_([u'                var y1 = []\n'])
    extend_([u"                var plot1 = jQuery.jqplot('chart1', [[1,3]]);\n"])
    extend_([u'        });\n'])
    extend_([u'        </script>\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body>\n'])
    extend_([u'        <div id="header">\n'])
    extend_([u'                <h2> jqPlot plot </h2>\n'])
    extend_([u'        </div>\n'])
    extend_([u'\n'])
    extend_([u'        <div id="chart1" style="width:600px;height:300px"></div>\n'])
    extend_([u'\n'])
    extend_([u'        <input type="text" id="text1" />\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

plot_jquery_test = CompiledTemplate(plot_jquery_test, 'templates/plot_jquery_test.html')
join_ = plot_jquery_test._join; escape_ = plot_jquery_test._escape

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
def returned_data_bootstrap_jquery (M, D, Y, pyDates, lunches, dinners, miscs, CSVrows, Ltot_thisMonth, Dtot_thisMonth, Mtot_thisMonth, Ltot_All, Dtot_All, Mtot_All):
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
    extend_([u'                <title>myFood 2.0 - tabulated</title>\n'])
    extend_([u'                            \n'])
    extend_([u'                <!-- Bootstrap core CSS -->\n'])
    extend_([u'                <link href="../static/bootstrap/css/bootstrap.css" rel="stylesheet">\n'])
    extend_([u'\n'])
    extend_([u'                <script language="javscript" type="text/javascript" src="../static/bootstrap/js/jquery.js"></script>\n'])
    extend_([u'                <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jquery.min.js"></script>\n'])
    extend_([u'                <script language="javascript" type="text/javascript"  src="../static/bootstrap/js/bootstrap.min.js"></script>\n'])
    extend_([u'                <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jquery.jqplot.min.js"></script>\n'])
    extend_([u'                <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.canvasAxisLabelRenderer.min.js"></script>\n'])
    extend_([u'                <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.canvasTextRenderer.min.js"></script>\n'])
    extend_([u'                <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.dateAxisRenderer.min.js"></script>      \n'])
    extend_([u'                <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.highlighter.min.js"></script>\n'])
    extend_([u'                <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.cursor.min.js"></script>\n'])
    extend_([u'                <script language="javascript" type="text/javascript" src="../static/bootstrap/js/jqplot.canvasAxisTickRenderer.min.js"></script>\n'])
    extend_([u'\n'])
    extend_([u'                <script type="text/javascript">\n'])
    extend_([u'                jQuery(document).ready(function() {\n'])
    extend_([u'                        var y1 = [];\n'])
    extend_([u'                        var y2 = [];\n'])
    extend_([u'                        var y3 = [];\n'])
    extend_([u'                        var Jdates = [];\n'])
    extend_([u'                        \n'])
    extend_([u'                        for(var i = 0; i < ', escape_((pyDates), True), u'.length; i+=1)\n'])
    extend_([u'                        {\n'])
    extend_([u'                                Jdates.push(new Date(', escape_((pyDates), True), u'[i]));\n'])
    extend_([u'                                if(', escape_((lunches), True), u'.length > 0)\n'])
    extend_([u'                                {\n'])
    extend_([u'                                        y1.push([Jdates[i], ', escape_((lunches), True), u'[i]]);\n'])
    extend_([u'                                }\n'])
    extend_([u'                                if(', escape_((dinners), True), u'.length > 0)\n'])
    extend_([u'                                {\n'])
    extend_([u'                                        y2.push([Jdates[i], ', escape_((dinners), True), u'[i]]);\n'])
    extend_([u'                                }\n'])
    extend_([u'                                if(', escape_((miscs), True), u'.length > 0)\n'])
    extend_([u'                                {\n'])
    extend_([u'                                        y3.push([Jdates[i], ', escape_((miscs), True), u'[i]]);\n'])
    extend_([u'                                }\n'])
    extend_([u'                        }\n'])
    extend_([u'\n'])
    extend_([u'                        /* solely for debugging!\n'])
    extend_([u"                        jQuery('#text1').val(y1);\n"])
    extend_([u'                        */\n'])
    extend_([u'\n'])
    extend_([u"                        jQuery.jqplot('chart1', [y1], {\n"])
    extend_([u"                                title:'Lunch Expenses',\n"])
    extend_([u'                                axesDefaults: {\n'])
    extend_([u'                                                tickRenderer: jQuery.jqplot.CanvasAxisTickRenderer\n'])
    extend_([u'                                              },\n'])
    extend_([u'                                axes:{\n'])
    extend_([u'                                        xaxis:{\n'])
    extend_([u'                                                renderer:jQuery.jqplot.DateAxisRenderer, \n'])
    extend_([u"                                                tickOptions:{formatString:'%b %#d %Y', angle: -45},\n"])
    extend_([u"                                                tickInterval: '1 month'\n"])
    extend_([u'                                              },\n'])
    extend_([u'                                        yaxis:{\n'])
    extend_([u"                                                tickOptions:{formatString:  '", u'$', u"%.2f', angle: -45},\n"])
    extend_([u'                                                min: 0,\n'])
    extend_([u'                                                autoscale: true\n'])
    extend_([u'                                              }\n'])
    extend_([u'                                     },\n'])
    extend_([u"                                series:[{lineWidth:4, markerOptions:{style:'square'}}],\n"])
    extend_([u"                                highlighter:{ show: true, tooltipLocation: 'e' },\n"])
    extend_([u"                                cursor:{ show: true, tooltipLocation: 'ne' }\n"])
    extend_([u'                        });\n'])
    extend_([u'\n'])
    extend_([u"                        jQuery.jqplot('chart2', [y2], {\n"])
    extend_([u"                                title:'Dinner Expenses',\n"])
    extend_([u'                                axesDefaults: {\n'])
    extend_([u'                                                tickRenderer: jQuery.jqplot.CanvasAxisTickRenderer\n'])
    extend_([u'                                              },\n'])
    extend_([u'                                axes:{\n'])
    extend_([u'                                        xaxis:{\n'])
    extend_([u'                                                renderer:jQuery.jqplot.DateAxisRenderer, \n'])
    extend_([u"                                                tickOptions:{formatString:'%b %#d %Y', angle: -45},\n"])
    extend_([u"                                                tickInterval: '1 month'\n"])
    extend_([u'                                              },\n'])
    extend_([u'                                        yaxis:{\n'])
    extend_([u"                                                tickOptions:{formatString:  '", u'$', u"%.2f', angle: -45},\n"])
    extend_([u'                                                min: 0,\n'])
    extend_([u'                                                autoscale: true\n'])
    extend_([u'                                              }\n'])
    extend_([u'                                     },\n'])
    extend_([u"                                series:[{lineWidth:4, markerOptions:{style:'square'}}],\n"])
    extend_([u"                                highlighter:{ show: true, tooltipLocation: 'e' },\n"])
    extend_([u"                                cursor:{ show: true, tooltipLocation: 'ne' }\n"])
    extend_([u'                        });\n'])
    extend_([u'\n'])
    extend_([u"                        jQuery.jqplot('chart3', [y3], {\n"])
    extend_([u"                                title:'Miscellaneous Expenses',\n"])
    extend_([u'                                axesDefaults: {\n'])
    extend_([u'                                                tickRenderer: jQuery.jqplot.CanvasAxisTickRenderer\n'])
    extend_([u'                                              },\n'])
    extend_([u'                                axes:{\n'])
    extend_([u'                                        xaxis:{\n'])
    extend_([u'                                                renderer:jQuery.jqplot.DateAxisRenderer, \n'])
    extend_([u"                                                tickOptions:{formatString:'%b %#d %Y', angle: -45},\n"])
    extend_([u"                                                tickInterval: '1 month'\n"])
    extend_([u'                                              },\n'])
    extend_([u'                                        yaxis:{\n'])
    extend_([u"                                                tickOptions:{formatString:  '", u'$', u"%.2f', angle: -45},\n"])
    extend_([u'                                                min: 0,\n'])
    extend_([u'                                                autoscale: true\n'])
    extend_([u'                                              }\n'])
    extend_([u'                                     },\n'])
    extend_([u"                                series:[{lineWidth:4, markerOptions:{style:'square'}}],\n"])
    extend_([u"                                highlighter:{ show: true, tooltipLocation: 'e' },\n"])
    extend_([u"                                cursor:{ show: true, tooltipLocation: 'ne' }\n"])
    extend_([u'                        });\n'])
    extend_([u'\n'])
    extend_([u'                });\n'])
    extend_([u'                </script>\n'])
    extend_([u'         \n'])
    extend_([u'        </head>\n'])
    extend_([u'        <body>\n'])
    extend_([u'                <div class="bs-example" style="margin:20px">\n'])
    extend_([u'                        <table class="table table-striped">\n'])
    extend_([u'                                <thead>\n'])
    extend_([u'                                        <tr>\n'])
    extend_([u'                                        <th>Date</th>\n'])
    extend_([u'                                        <th>Lunch</th>\n'])
    extend_([u'                                        <th>Dinner</th>\n'])
    extend_([u'                                        <th>Miscellaneous</th>\n'])
    extend_([u'                                        </tr>\n'])
    extend_([u'                                </thead>\n'])
    extend_([u'                                <tbody>\n'])
    for row in loop.setup(CSVrows):
        extend_(['                                        ', u'    <tr>\n'])
        extend_(['                                        ', u'    <td>', escape_(row[0], True), u'</td>\n'])
        extend_(['                                        ', u'    <td>', escape_(row[1], True), u'</td>\n'])
        extend_(['                                        ', u'    <td>', escape_(row[2], True), u'</td>\n'])
        extend_(['                                        ', u'    <td>', escape_(row[3], True), u'</td>\n'])
        extend_(['                                        ', u'    </tr>\n'])
        extend_(['                                        ', u'\n'])
        extend_(['                                        ', u'    <tr>\n'])
        extend_(['                                        ', u'    <td></td>\n'])
    if Ltot_thisMonth:
        extend_(['                                        ', u'    <td>Lunch (this month) = &#36;', escape_(Ltot_thisMonth, True), u' <br> Lunch (all months) = &#36;', escape_(Ltot_All, True), u'</td>\n'])
    if Dtot_thisMonth:
        extend_(['                                        ', u'    <td>Dinner (this month) = &#36;', escape_(Dtot_thisMonth, True), u' <br> Dinner (all months) = &#36;', escape_(Dtot_All, True), u'</td>\n'])
    if Mtot_thisMonth:
        extend_(['                                        ', u'    <td>Miscellaneous (this month) = &#36;', escape_(Mtot_thisMonth, True), u' <br> Miscellaneous (all months) = &#36;', escape_(Mtot_All, True), u'</td>     \n'])
        extend_(['                                        ', u'    </tr>   \n'])
    extend_([u'                                </tbody>\n'])
    extend_([u'                        </table>\n'])
    extend_([u'                </div>\n'])
    extend_([u'\n'])
    extend_([u'                <!--input type="text" id="text1" style="margin:20px"/-->\n'])
    extend_([u'\n'])
    extend_([u'                <div id="chart1" style="margin:100px;width:600px;height:300px"></div>\n'])
    extend_([u'                <div id="chart2" style="margin:100px;width:600px;height:300px"></div>\n'])
    extend_([u'                <div id="chart3" style="margin:100px;width:600px;height:300px"></div>\n'])
    extend_([u'\n'])
    extend_([u'        </body>\n'])
    extend_([u'</html>\n'])

    return self

returned_data_bootstrap_jquery = CompiledTemplate(returned_data_bootstrap_jquery, 'templates/returned_data_bootstrap_jquery.html')
join_ = returned_data_bootstrap_jquery._join; escape_ = returned_data_bootstrap_jquery._escape

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

