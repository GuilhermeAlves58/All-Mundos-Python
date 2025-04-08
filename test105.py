overall = {}
def grades(*marks,sit=False):
    overall['Max'] = max(marks)
    overall['Min']= min(marks)
    overall['ave'] = sum(marks) / len(marks)
    if sit == True:
        if overall['ave'] < 5:
            overall['sit'] = 'Bad'
        else:
            overall['sit'] = 'good'
            return overall
    else:
        return overall



overall = grades(5, 5, 5, 5, sit=True)
print(overall)