from microphone import file_call_microphone
from microphone import process_new_input_microphone
from match_file import matching_check_file


################################
file_call_microphone()

################################
Inputname,InputMFCC=process_new_input_microphone()
mini,name=matching_check_file(InputMFCC)
print("\n\n","The Closest Match to",Inputname,"is:")
print(name,mini)

