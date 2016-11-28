from flask import Flask
from flask import url_for, render_template, request, redirect
import pickle
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    random.seed()
    questdic = {}
    if request.args:
        # Анкета
        questdic['Date'] = request.args['Date']
        questdic['Time'] = request.args['Time']
        questdic['FIO1'] = request.args['FIO1']
        questdic['Phone'] = request.args['Phone']
        questdic['FIO2'] = request.args['FIO2']
        questdic['FIO3'] = request.args['FIO3']
        questdic['Q1'] = request.args['Q1']
        questdic['Q2'] = request.args['Q2']
        questdic['Q3'] = request.args['Q3']
        questdic['Q4'] = request.args['Q4']
        questdic['Q5'] = request.args['Q5']
        questdic['Q6'] = request.args['Q6']
        questdic['Q7'] = request.args['Q7']
        questdic['Q8'] = request.args['Q8']
        questdic['Q9'] = request.args['Q9']
        questdic['Q10'] = request.args['Q10']
        questdic['Q11'] = request.args['Q11']
        questdic['Q12'] = request.args['Q12']
        questdic['Q13'] = request.args['Q13']
        questdic['Q14'] = request.args['Q14']
        questdic['Q15'] = request.args['Q15']
        questdic['Q16'] = request.args['Q16']
        questdic['Q17'] = request.args['Q17']
        questdic['Q18'] = request.args['Q18']
        questdic['Q19'] = request.args['Q19']
        questdic['Q20'] = request.args['Q20']
        questdic['Q21'] = request.args['Q21']
        questdic['Q22'] = request.args['Q22']
        questdic['Q23'] = request.args['Q23']
        questdic['Q24'] = request.args['Q24']
        questdic['Q25'] = request.args['Q25']
        questdic['Q26'] = request.args['Q26']
        questdic['reviews'] = request.args['reviews']
        questdic['wait'] = request.args['wait']
        questdic['competence'] = request.args['competence']
        questdic['comments'] = request.args['comments']
        questdic['OrgAddr'] = request.args['OrgAddr']
        questdic['OrgName'] = request.args['OrgName']

        f = open('f_'+questdic['Date'].replace('-', '')+'_' + str(random.randint(100, 1000)) + '.dic', 'wb')
        pickle.dump(questdic, f)
        f.close()
        return render_template('thanks.html')
    return render_template('migra.html')



if __name__ == '__main__':
    app.run()
