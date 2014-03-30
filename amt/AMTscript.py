# This is the main AMT script that should be executed and will do the following:
#   * Create a HIT
#   * Wait for the HIT to become reviewable
#   * Process assignments once the HIT is reviewable
#       * Check whether their input code is one that we gave them. 
#       * If yes, pay them, if not, reject them.

# NOTE: Should this script close before all assignments are reviewed, please run 'AMTpay.py'
# NOTE: Fill in your AWS keys in 'ACCESS_KEY' and 'SECRET_KEY'

from boto.mturk.connection import MTurkConnection, HIT
from boto.mturk.question import SimpleField,QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
import time
 
ACCESS_ID = ''
SECRET_KEY = ''
HOST = 'mechanicalturk.amazonaws.com'

# this mtc is used for creating the HIT
mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)
 
title = 'CrowdMix: Remix a Classical Composition'
description = ('Help remix a classical music composition '
               'by choosing the next sound bits! Simple, easy, and fast!')
keywords = 'music, create, easy, fast'
max_assignments = 50

# acceptable codes that will ge the turker paid
payCodes = ['CG6H5', 'X38T1', 'S1W59', 'D2K9K', 
            'DCURP', 'KJHCY', 'KSSIZ', 'YYLMB', 
            '47NQK', 'WILIM']

#-------------- WAIT FUNCTION ----------------------------

# wait timer function since time.sleep() was giving issues
def wait(time_lapse):
  time_start = time.time()
  time_end = (time_start + time_lapse)
 
  while time_end > time.time():
    pass

# this mtc is used for data retrieval
mtc2 = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)

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
 
#---------------  BUILD OVERVIEW -------------------
 
overview = Overview()
overview.append_field('Title', 'CrowdMix: Remix a Classical Composition')
overview.append(FormattedContent('<a target="_blank"'
                                 ' href="http://allekant.com/cgi-bin/welcome.py">'
                                 ' CrowdMix Homepage</a>'))
overview.append(FormattedContent('Please visit the link above in order to complete this HIT.\n'
                                 'When completed, you will be given a code to input below.'))
overview.append(FormattedContent('On the webpage linked above, you will be given five random '
                                 'sound bits to listen to. Then you will choose two clips, using '
                                 'the radio buttons, that will be combined and added with other '
                                 'clips to make a new song'))
overview.append(FormattedContent('When you have selected two clips using the radio buttons, '
                                 'click the Load My New Choice button to confirm your selection.'))
overview.append(FormattedContent('When you are satisfied with your choices and you have '
                                 'already clicked the Load My New Choice button, click the '
                                 'Submit My Decision and Get My Code! button.'))
overview.append(FormattedContent('After clicking the Submit button, you will be given a code '
                                 'to input in to the box below. Once you have put the code in '
                                 'box, submit the hit and wait for approval.'))
 
#---------------  BUILD QUESTION 1 -------------------
 
qc1 = QuestionContent()
qc1.append_field('Title','Enter your code in the box below.')
fta1 = FreeTextAnswer();
q1 = Question(identifier='code',
              content=qc1,
              answer_spec=AnswerSpecification(fta1),
              is_required=True)
 
#--------------- BUILD THE QUESTION FORM -------------------
 
question_form = QuestionForm()
question_form.append(overview)
question_form.append(q1)
 
#--------------- CREATE THE HIT -------------------
 
mtc.create_hit(questions=question_form,
               max_assignments = max_assignments,
               title = title,
               description = description,
               keywords = keywords,
               duration = 60*5,
               reward = 0.25)

#--------------- WAIT FOR ASSIGNMENTS TO COMPLETE ----------
#-------------------- AND REVIEW ASSIGNMENTS ---------------

hits = get_all_reviewable_hits(mtc2)
hitReviewed = False;

# this busy loops until we have processed the one reviewable HIT
while True:
  if not hits:
    print "Waiting for reviewable hits..."
    hits = get_all_reviewable_hits(mtc2)
  else:
    for hit in hits: # for every hit that's reviewable, review turker answers
      assignments = mtc2.get_assignments(hit.HITId)
      
      for assignment in assignments: # get individual turker assignments
        print "Answers of the worker %s" % assignment.WorkerId
        
        for question_form_answer in assignment.answers[0]:
          
          for key in question_form_answer.fields: # get individual turker answers to assignments
            print "%s" % (key)
            if key.upper() in payCodes: # if they used the right code, approve/pay them
              print "%s: Accepted and paid!" % assignment.WorkerId
              mtc2.approve_assignment(assignment.AssignmentId)
            else: # if they used the wrong code, reject them
              print "%s: Rejected and not paid!" % assignment.WorkerId
              mtc2.reject_assignment(assignment.AssignmentId, feedback = 'Invalid code.') 
        print "--------------------"
      
      # the hit stays enabled in case a turker is rejected, however they should have been approved
      # this should hopefully never happen
      ##mtc2.disable_hit(hit.HITId)
      hitReviewed = True;

  if hitReviewed: # since I know that I only submit one HIT, I quit after one HIT is reviewed
    break;
  else: # wait 30 seconds so that Amazon does not get mad
    wait(30)

print "All assignments have been reviewed!\n"
print "Program has been terminated!"
