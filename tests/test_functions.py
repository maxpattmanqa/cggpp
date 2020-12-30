import pytest
from application.routes import get_pedals_entry

#test database crud functions 

#test Read function 

def test_read_pedal_entry():
   entry = get_pedals_entry('MX-101')
   print(entry)
   assert(entry.model == 'MX-101')



def test_insert_pedal_entry():
    model = "MX-101"
    effect = "Phase 90"
    year_intro  = "1974"
    series = "Reference"
    #insert_pedal_entry(model,effect,year_intro,series)


   