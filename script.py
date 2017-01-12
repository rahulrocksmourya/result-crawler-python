
import mechanize
from BeautifulSoup import BeautifulSoup 

br = mechanize.Browser()
session = '2015-2016'
semester = '6'
resultCategory = 'R'
rollNoPrefix = '13043100'

  
for i in range(1,69):
    br.open('http://bietjhs.ac.in/studentresultdisplay/frmprintreport.aspx')
        
    br.select_form('aspnetForm')
        
        
    br.form['ctl00$ContentPlaceHolder1$ddlAcademicSession'] = [session]
    br.form['ctl00$ContentPlaceHolder1$ddlSem'] = [semester]
    br.form['ctl00$ContentPlaceHolder1$ddlResultCategory'] = [resultCategory]
    if(i<10):
        br.form['ctl00$ContentPlaceHolder1$txtRollno'] = rollNoPrefix + '0'+str(i)
    else:
        br.form['ctl00$ContentPlaceHolder1$txtRollno'] = rollNoPrefix + str(i)
    response = br.submit()
        
    soup = BeautifulSoup(response)
        
    name = soup.first('span',{'id':'ctl00_ContentPlaceHolder1_sName'})
    if(int(semester)%2==0):
        totalMarks=soup.first('span',{'id':'ctl00_ContentPlaceHolder1_omk'})
    else:
        totalMarks=soup.first('span',{'id':'ctl00_ContentPlaceHolder1_emk'})
    
    percentageArr=totalMarks.text.split('/');
    percentage = float(percentageArr[0])/float(percentageArr[1])*100;
    print name.text + '  ----  ' + totalMarks.text + '  ----  ' + str(percentage)

#print response.read()   # body
