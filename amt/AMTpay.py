# Use this script if the AMTscript.py script happens to fail,close,etc.
# This script checks for reviewable hits and pays them according to whether or not
# they input the correct code that we gave them

from boto.mturk.connection import MTurkConnection, HIT
from boto.mturk.question import SimpleField,QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
import time
 
ACCESS_ID = ''
SECRET_KEY = ''
HOST = 'mechanicalturk.amazonaws.com'
 
mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)

payCodes = ['CG6H5', 'X38T1', 'S1W59', 'D2K9K', 
            'DCURP', 'KJHCY', 'KSSIZ', 'YYLMB', 
            '47NQK', 'WILIM']

#----------- TIMER FUNCTION ---------------
def wait(time_lapse):
  time_start = time.time()
  time_end = (time_start + time_lapse)
 
  while time_end > time.time():
    pass

#--------------- GET ALL REVIEWABLE HITS FUNCTION ----------

def get_all_reviewable_hits(mtc2):
    page_size = 50
    hits = mtc2.get_reviewable_hits(page_size=page_size)
    print "Total results to fetch %s " % hits.TotalNumResults
    print "Request hits page %i" % 1
    total_pages = float(hits.TotalNumResults)/page_size
    int_total= int(total_pages)
    if(total_pages-int_total>0):
        total_pages = int_total+1
    else:
        total_pages = int_total
    pn = 1
    while pn < total_pages:
        pn = pn + 1
        print "Request hits page %i" % pn
        temp_hits = mtc2.get_reviewable_hits(page_size=page_size,page_number=pn)
        hits.extend(temp_hits)
    return hits

#--------------- WAIT FOR ASSIGNMENTS TO COMPLETE ----------

hits = get_all_reviewable_hits(mtc)
hitReviewed = False;

# this busy loops until we have processed the one reviewable HIT
while True:
  if not hits:
    print "Waiting for reviewable hits (30 second wait)..."
    hits = get_all_reviewable_hits(mtc)
  else:
    for hit in hits: # for every hit that's reviewable, review turker answers
      assignments = mtc.get_assignments(hit.HITId)
      
      for assignment in assignments: # get individual turker assignments
        print "Answers of the worker %s" % assignment.WorkerId
        
        for question_form_answer in assignment.answers[0]:
          
          for key in question_form_answer.fields: # get individual turker answers to assignments
            print "%s" % (key)
            if key.upper() in payCodes: # if they used the right code, approve/pay them
              print "%s: Accepted and paid!" % assignment.WorkerId
              mtc.approve_assignment(assignment.AssignmentId)
            else: # if they used the wrong code, reject them
              print "%s: Rejected and not paid!" % assignment.WorkerId
              mtc.reject_assignment(assignment.AssignmentId, feedback = 'Invalid code.') 
        print "--------------------"
      
      ##mtc2.disable_hit(hit.HITId)
      hitReviewed = True;

  if hitReviewed:
    break;
  else:
    wait(30)

print "All assignments have been reviewed!"