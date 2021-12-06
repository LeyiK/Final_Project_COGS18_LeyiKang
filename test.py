# Import from modules
from chatbot_script import library_spooky
from chatbot_script import activities
from chatbot_script import df_colleges

# Tests
assert callable(library_spooky)
print('Test 1 passed: function is callable.')

assert type(activities) == type
print('Test 2 passed: correct class type.')

assert df_colleges('colleges') == True
print('Test 3 passed: function returns desired output.')