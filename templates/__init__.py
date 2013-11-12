from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def init_form (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<title>myFood2.0 - form</title>\n'])
    extend_([u'\n'])
    extend_([u'<form name="main" method="post">\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" />\n'])
    extend_([u'</form>\n'])
    extend_([u'\n'])
    extend_([u'Go to <a href="/getcsv">myfood-2p0.appspot.com/getcsv</a> to retrieve a compiled CSV file of your meal expenses.\n'])

    return self

init_form = CompiledTemplate(init_form, 'templates/init_form.html')
join_ = init_form._join; escape_ = init_form._escape

# coding: utf-8
def returned_data (CSVrows, currentMonth, Ltot_thisMonth, Dtot_thisMonth, Mtot_thisMonth, Ltot_All, Dtot_All, Mtot_All):
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

