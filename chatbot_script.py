# Import
from datetime import date
from datetime import time
from datetime import datetime
import pandas as pd
from IPython.display import Markdown
import random
import string
from IPython.display import display # This one is needed only when the chatbot is run in a terminal


# Collections of chats
greetings_in = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings','wassup']
greetings_out = ['Nice to meet you!','Hello!','Pleasure to meet you!']

goodbyes_in = ['bye','goodbye','byebye','adieu','quit']
goodbyes_out = ['Goodbye :(','See you next time!','I hate saying goodbyes!']

weathers = ['sunny. Nice day, eh?','rainy. Raining makes me sad.', "foggy. I can't see a thing!",'cloudy.',"snowy. I love snow! Let's play!"]

intro_in = ['who', 'name', 'identity','introduction','yourself']
intro_out = ["I am a chatbot created by Leyi from COGS18. I can give you information about our school!\n type 'topics' to know what I can do.",
            "I am a chatbot assisting you to know more about our school and I am created by Leyi from COGS18.\n type 'topics' to know what I can do."]

echo_list = ['good','ok','yeah','yes','cool','wow','oh']


# Specify topics
possible_topics = ['Please tell me what you want to know!', 'I can talk about:',
'-Weather',
'-Date and day',
'-Colleges',
'-Dining halls',
'-Housing',
'-Library',
'-Price Center',
'And I can give you more detailed information about school activities for the next week!', "Type 'activities' for that."]


# DataFrame of Colleges
colleges_df = pd.DataFrame({'Name': ['Revelle College','John Muir College','Thurgood Marshall College','Earl Warren College',
                            'Elenar Rooservelt College','Six college','Seventh College'],
                   'Founded in': ['1964','1967','1970','1974','1988','2001','2020'],},
                  index = ['1','2','3','4','5','6','7'])

# DataFrame for dining halls
dining_df = pd.DataFrame({'Name': ['Revelle College','John Muir College','Thurgood Marshall College','Earl Warren College',
                            'Elenar Rooservelt College','Six college','Seventh College'],
                   'Dining Hall': ['64 Degrees','Pines','OceanView Terrace','Canyon Vista','Cafe Ventanas','Wolftown','The Bistro'],},
                  index = ['1','2','3','4','5','6','7'])


# Functions that help return df without raising value error
def df_colleges(i):
    if i == 'colleges':
        return True

def df_dining(i):
    if i == 'dining':
        return True
    
    
# Housing information
housing = 'Check out this link for UCSD on-campus housing! https://hdhughousing.ucsd.edu/living-on-campus/neighborhoods/index.html'


# Library urban legend
def library_spooky():
    print('My creator goes to Geisel Library a lot. She has been to all floors of the library but never the third floor.' ,
          'Nobody can ever get to the third floor.', '',sep = '\n')

    # Refer to A2
    spooky = True
    counter = 0

    while spooky:
        print('Nobody can get to the third floor.')
        counter += 1
        if counter == 5:
            spooky = False

    encoded = ''
    for char in 'Nobody can get to the third floor.':
        result = chr(ord(char)+400)
        encoded = encoded+result
    print(encoded)
    
    # I found this code that altering output's color online, but I forgot to take down the web link and now I failed to find it again
    display (Markdown('<span style="color: #ff0000">DO NOT GO TO THE THIRD FLOOR.</span> '))

    debrief = 'No that was a joke. There is actually no third floor in Geisel, because it is an open forum above 1st and 2nd floor.'
    return debrief


# Price Center
def pc():
    
    print("There are many food options at Price Center! I have randomly choosen one for you for today's lunch:")
    food = ['Subway',"Rubio's",'Panda Express','Burger King','Seed + Sprout']
    out = random.choice(food)
    return out


# Activieties for next week
class activities():
    '''All activities are attributed to a class with instance attributes of their information.'''
    
    def __init__(self, name, time, location, info):
        
        self.name = name
        self.time = time
        self.location = location
        self.info = info
    
    def print_info(self):
        '''Print out information of specific object in a user-friendly way.'''
        
        out_list = [self.time, self.name,'Location:', self.location,self.info]
        out_string = list_to_string(out_list,'\n')
        return out_string

activity_dic = {'monday':activities('Free snacks', 'Monday at 2pm', 'Library Walk', 'Enjoy free chips and protein bars!'),
                 'tuesday':activities('Therapy dogs', 'Tuesday at 10am', 'Muir Quad', 'Get healed by therapy fluffy!'),
                 'wednesday':activities('Destress meditation', 'Wednesday at 10am', 'Revelle College', 'Destress with Revelle before finals'),
                 'thursday':activities('Late Night Study Fest', 'Thursday at 8pm', 'Price Center', 'Vendors open late to support final week!'),
                 'friday':activities('Tea & Coffee Hour', 'Friday at 1pm', 'Price Center', 'Chilling, listening, sharing')} 


# Basic functions needed by the chatbot
# From A3

# Remove punctuation
def remove_punctuation(input_string):
    '''First create an empty string, then add character from the input string if the character is not a punctuation.
    This method gets rid of all punctuations in input to avoid bugs.'''
    
    out_string = ''
    for i in input_string:
        if i not in string.punctuation:
            out_string = out_string + i
    return out_string

# Prepare the text: turn input string into list
def prepare_text(input_string):
    '''Because the input is a string, this method converts it to a list for further methods of looping and selecting.'''
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

# String concatenator
def string_concatenator(string1, string2, separator):
    '''This method concatenates strings.'''
    
    output = string1 + separator + string2
    return output

# List to string
def list_to_string(input_list, separator):
    '''When the output returned from a method is a list, this method coverts it to a string for further output, 
    seperated each item in the list with the specific seperator.'''
    
    output = input_list[0]
    for i in input_list[1:]:
        output = string_concatenator(output,i,separator)
    return output

# End the chat
def end_chat(input_list, check_list, return_list):
    '''End the chat when the input list contains the same item in the check list.'''
    
    for i in input_list:
        if i in check_list:
            return True
        

# Main structure of the chatbot
# From A3

def have_a_chat():
    '''Main function to run the chatbot'''
    
    chat = True
    while chat:

        # Get a input message from the user
        in_msg = input('INPUT :\t')
        out_msg = None

        # Turn input string into list
        msg = prepare_text(in_msg)
        
        # See if input message is an end message, return a goodbye and end the chat if so 
        if end_chat(msg, goodbyes_in, goodbyes_out):
            out_msg = random.choice(goodbyes_out)
            chat = False
            
        if not out_msg:  
            for i in msg:
                
                # See if the input message is a greeting, return a greeting output if so
                if i in greetings_in:
                    out_msg = random.choice(greetings_out)
                
                # See if the input is about date/day
                if i == 'date':
                    today_date = date.today()
                    out_msg = 'Today is ' + str(today_date) + '.'
                if i == 'day':
                    today_date = date.today()
                    wd_num = today_date.weekday() # Index of day
                    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
                    wd = weekdays[wd_num]
                    out_msg = 'Today is ' + str(wd) + '.'
                    
                # See if the input asks for weather
                if i == 'weather':
                    out_msg = 'Today is ' + random.choice(weathers)
                
                # See if the input asks for introduction
                if i in intro_in:
                    out_msg = random.choice(intro_out)
                
                # See if the input asks for topics
                if i == 'topics':
                    out_msg = list_to_string(possible_topics, '\n')
                    
                    # See if the input asks for colleges
                if df_colleges(i):
                    out_msg = 'There are 7 colleges in UCSD'
                    print(colleges_df)
                
                    # See if the input asks for dining halls
                if df_dining(i):
                    out_msg = 'Check out where students eat!'
                    print(dining_df)
                    
                    # See if the input asks for housing
                if i in ['housing','dorms','dorm','on-campus']:
                    out_msg = housing
                    
                    # See if the input asks for library
                if i == 'library':
                    out_msg = library_spooky()
                    
                    # See if the input asks for Price Center
                if i == 'price':
                    out_msg = pc()
                
                    # See if the input asks for activities
                if i == 'activities':
                    out_msg = 'There are activities thourout the upcoming week! Which day you want to choose?'
                    # Give information of a specific day
                if i in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                        out_msg = activity_dic[i].print_info()
                
                # Echo the input when input does not ask for anything
                if i in echo_list:
                    out_msg = i + ' ' + i
                
                # If the input asks for things else than what we have in the collection
                    

        # if the input does not match with any of the keywords stored.
        if not out_msg:
            out_msg = "Hmm, I don't think I understand what you mean. Ask me something else! Or check your spelling!"
            
        print('OUTPUT:', out_msg)

        
# Talk to the chatbot
have_a_chat()