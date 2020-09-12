# -*- coding: utf-8 -*-
"""
Eniola Osineye
800148708
osineye_finalp.py 11/16/19

"""
def createCursor():
      import tweepy
    
      #variables to be used to create cursor object
      twitterAccount = 'realdonaldtrump'
      size = 200
      
      #twitter developer account keys
      consumer_key = 'CONSUMER_KEY'
      consumer_secret = 'CONSUMER_SCRET'
      access_token = 'ACCESS_TOKEN'
      access_token_secret = 'ACCESS_TOKEN_SECRET'
      
      #tweepy authentication
      auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
      auth.set_access_token(access_token, access_token_secret)
      api = tweepy.API(auth)

      #list to store dictionary with details on followers
      followers = []
                  
      #creating cursor object
      cursor = tweepy.Cursor(api.followers, screen_name=twitterAccount, count=size)
      
      #creating a dictionary of follower's details and storing dictionary in a list
      for person in cursor.items(size):
          if(not person.verified):
              followers.append({'screen_name': person.screen_name,                'friends': person.friends_count,              
                            'number_of_tweets': person.statuses_count,        'bio': person.description,                    
                            'default_image': person.default_profile_image,    'verified': person.verified,                  
                            'followers': person.followers_count,              'url': 'twitter.com/'+person.screen_name,     
                            'created': person.created_at,                     'score': 0 })
              
      return followers
    
  
def main():
    from operator import itemgetter
   
    #menu driven program
    while True:

        #main menu 
        mainMenu()
 
        try:
            #enter choice
            choice = int(input('\n>>>>   ').strip())
            
            #exit program
            if(choice == 0):
                endDetails()
                break
            
            #examine followers to find follow-bots
            elif(choice == 1):
                print('\nFollow-bots being examined...')
                
                #list to store dictionary of details on followers
                followers = createCursor()
                
                #calling function to examine follower for follow-bots
                followBots = examineFollowBots(followers)
                
                #calling function to create a list of follow-bots
                followBotList = printBots(followBots)
               
                while True:
                    #displaying follow-bot examination menu
                    botExaminationMenu()
                    
                    try:
                        #enter choice
                        choice = int(input('\n>>>>   ').strip())
                        
                        #exit follow-bot menu
                        if(choice == 0):
                            print('\nExiting follow-bot options!')
                            break
                        
                        #showing list of follow-bots
                        elif(choice == 1):
                            print('\nFirst option being executed!\n\nShowing list of follow-bots')
                            
                            print('\n---------------------------------------------------\n')
                            for person in followBotList:
                                print(person['screen_name'])
                                
                            print('\n---------------------------------------------------\n')
                
                        #showing probability of follower being a follow-bot menu   
                        elif(choice == 2):
                            print('\nSecond option being executed!')
                            print('\nShowing probability of follow-bots')
                           
                            while True:
                                #displaying probability menu
                                probabilityMenu()
                               
                                try:
                                    choice = int(input('\n>>>>   ').strip())
                                   
                                    #exit probaility menu
                                    if(choice == 0):
                                        print('\nExiting probability options')
                                        break

                                    #print probability of follow-bots in ascending order    
                                    elif(choice == 1):
                                        print('\nPrbability in asccending order')

                                        #calling method to calculate and print probability
                                        printList = probFollowBots(followBotList)
                                        print('\n---------------------------------------------------\n')
                                        for person in sorted(printList, key=itemgetter('probability', 'screen_name')):
                                            print('Screen name: ', person['screen_name'])
                                            print('Probability: ', person['probability'],'\n')
                                        
                                        print('\n---------------------------------------------------\n')
                                        
                                    #print probability of follow-bots in descending order    
                                    elif(choice == 2 ):
                                        print('\nPrbability in decending order')

                                        #calling function to calculate and print probability
                                        printList = probFollowBots(followBotList)
                                        
                                        print('\n---------------------------------------------------\n')
                                        for person in sorted(printList, key=itemgetter('probability', 'screen_name'), reverse=True):
                                            print('Screen name: ', person['screen_name'])
                                            print('Probability: ', person['probability'],'\n')
                                        print('\n---------------------------------------------------\n')
                                        
                                    
                                    elif(choice ==  3):
                                        #display help details for probability menu
                                        probabilityHelp()
                                    
                                    #choice out not an option
                                    else:
                                        print('\nPlease enter a valid menu option!')

                                #choice not an integer
                                except:
                                    print('\nPlease type a valid menu option as an integer!')
                                                          
                        #displaying menu for a short report
                        elif(choice == 3):
                            print('\nThird option being executed!')
                           
                            while True:
                                #displaing short report menu
                                shortReportMenu()
                               
                                try:
                                    choice = int(input('\n>>>>   ').strip())
                                    
                                    #exiting short report menu
                                    if(choice == 0):
                                        print('\nExiting short report options')
                                        break

                                    elif(choice == 1):
                                        print('\nShort report for one-to-many specific accounts')
                                       
                                        while True:
                                            # number of elemetns as input
                                            try:
                                                #creating a list of screen names to search
                                                createSearchList(followBotList,'short')
                                                break

                                            except:
                                                print('\nMust enter an integer!')
                                            
                                    #percentage option selected
                                    elif(choice == 2 ):
                                        print('\nShort report for percentage of accounts')
                                        
                                        while True:
                                            # number of elemetns as input
                                            try:
                                                perct = float(input("\nEnter percentage of accounts: ").strip())
                                                
                                                #calling function to display report of percentage of follow-bots
                                                detailPercentage(perct,  followBotList, 'short')
                                                break
                                            except:
                                                print('\nMust enter an integer!')
                                    
                                    #displaying help details for short report menu
                                    elif(choice == 3):
                                        #displaying short report help
                                        shortReportHelp()
                                    else:
                                        print('\nPlease enter a valid menu option!')
                                except:
                                    print('\nPlease type a valid menu option as an integer!')    
                                       
                        elif(choice == 4):
                            print('\nFourth option being executed!')
                           
                            while True:
                                #displaying long report menu
                                longReportMenu()
                               
                                try:
                                    choice = int(input('\n>>>>   ').strip())
                                   
                                    if(choice == 0):
                                        print('\nExiting long report options')
                                        break

                                    elif(choice == 1):
                                        print('\nLong report for one-to-many specific accounts')
                                        while True:
                           
                                            # number of elemetns as input
                                            try:
                                                #creating a list of screen names to search
                                                createSearchList(followBotList,'long')
                                                break
                                                
                                            except:
                                                print('\nMust enter an integer!')
                                   
                                    elif(choice == 2 ):
                                        print('\nLong report for percentage of accounts')
                                        while True:
                                            # number of elemetns as input
                                            try:
                                                perct = float(input("\nEnter percentage of accounts: ").strip())
                                               
                                                #calling method to display report of percentage of follow-bots
                                                detailPercentage(perct, followBotList, 'long')
                                                break

                                            except:
                                                print('\nMust enter an integer!')
                                    
                                    
                                    elif(choice == 3):
                                        #displaying help details for long report menu
                                        longReportHelp()
                                    else:
                                        print('\nPlease enter a valid menu option!')
                                except:
                                    print('\nPlease type a valid menu option as an integer!')   
                        
                        
                        elif(choice == 5):
                            #displaying help details for follow-bot examination menu
                            botExaminationHelp()
                                       
                        else:
                            print('\nPlease enter a valid menu option!')
                    except:
                        print('\nPlease type a valid menu option as an integer!')            
            else:
                print('\nPlease enter a valid menu option!')
        except:
            print('\nPlease type a valid menu option as an integer!') 
          
        
   
        

        
                                               
 #function to examine follower accounts and identify follow-bots   
def examineFollowBots(followers):
        
    for person in followers:       
        #check if account has default image
        if(person['default_image']):
            person['score'] += 1
                
        #check if 'bot' in screen_name
        if('bot' in person['screen_name']):
            person['score'] += 1
                
        #check if screen_name contains numbers
        if(any(i.isdigit() for i in person['screen_name'])):
            person['score'] += 1
            
        #check account has a bio
        if(person['bio'] == ''):
            person['score'] += 1
                
        #check if account is relatively new (made in 2019)
        if(person['created'].year >= 2019):
            person['score'] += 1
                
        #check if the account has low followers (below 100)
        if(person['followers'] < 10):
            person['score'] += 1
                    
        #check if the account has low friends (below 100)
        if(person['friends'] < 20):
            person['score'] += 1
                 
            
        if(person['number_of_tweets'] == 0):
            person['score'] += 1
            
    return followers

#function to print each followers screen name and if it is suspected to be a follow-bot, print so
def printBots(followers):
    
    #empty list to store screen names
    followBotList = []
    ctr = 0;
    print('\n---------------------------------------------------\n')
    
    #iterating list of followers
    for person in followers:
        print('Examining @{}...'.format(person['screen_name']))
        
        if(person['score'] >= 6):
            ctr += 1
            print('Found follow-bot #{}: twitter.com/{}'.format(ctr, person['screen_name']))
            followBotList.append(person)
    print('\n---------------------------------------------------')
    
    return followBotList
    
#function to create a list of screen names to print report of
def createSearchList(followBotList,size):
    # creating an empty list
    lst = []
                                                
    n = int(input("\nEnter number of accounts: ").strip())
    ctr = 1
                                                
    if(n  > 0):
        # iterating till the range
        for i in range(n):
            account = input(('\nEnter screen name #{}:  ').format(ctr)).rstrip()
            lst.append(account) 
            ctr += 1
                                                         
        print('\nShowing report of specific accounts')

        #calling report function
        detailSpecific(lst,  followBotList, size)
                                                
    else:
        print('\nNumber of accounts must be greater than zero')

#function to print a report on a percentage of the follow-bot accounts                  
def detailPercentage(perct, dataList, length):
    
    if((1/len(dataList))* 100 < perct ):
        x = (perct/100) * len(dataList)
        output = '\n\n\nPrinting report of  {}% of follow-bot accounts'.format(perct)
            
    else:
        x = 1
        output =  '\n\n\nPrinting report of 10% of follow-bot accounts as\nprinting {}% is too small of a percentage of the data'.format(perct) 
        
    print(output)
    print('\n\n\n---------------------------------------------------')

    if(length == 'short'):
        for n in range(int(x)):
            account = dataList[n]
            print('\nScreen_name:             ',account['screen_name'])
            print('Followers count:           ',account['followers'])
            print('Friends count:             ',account['friends'])
            print('Score:                     ',account['score'],'/ `9')
            print('\n---------------------------------------------------')
          
    else:
        for n in range(int(x)):
            account = dataList[n]
            print('\nScreen_name:             ',account['screen_name'])
            print('Followers count:           ',account['followers'])
            print('Friends count:             ',account['friends'])
            print('Bio:                       ',account['bio'])
            print('\nCreated:                   ',account['created'])
            print('Number Tweets:             ',account['number_of_tweets'])
            print('URL:                       ',account['url'])
            print('Default profile image?:    ',account['default_image'])
            print('Score:                     ',account['score'], '/ 9')
            print('\n---------------------------------------------------')
    print('\n\n\n')
   
#function to print a report on a specific follow-bot accounts 
def detailSpecific(searchList, dataList, length):
    ctr = 1
    
    if(length == 'short'):
        print('\n\n\n---------------------------------------------------')
        for account in dataList:
            for name in searchList:
                if(account['screen_name'].lower() == name.lower()):
                    print('\nShort report #',ctr)
                    print('Screen_name:               ',account['screen_name'])
                    print('Followers count:           ',account['followers'])
                    print('Friends count:             ',account['friends'])
                    print('Score:                     ',account['score'])
                    ctr += 1        
                    print('\n---------------------------------------------------')   
        print('\n\n\n')
                      
    else:
        print('\n\n\n---------------------------------------------------')
        for account in dataList:
            for name in searchList:
                if(account['screen_name'].lower() == name.lower()):
                    print('\n---------------------------------------------------')
                    print('\nLong report #',ctr)
                    print('Screen_name:               ',account['screen_name'])
                    print('Followers count:           ',account['followers'])
                    print('Friends count:             ',account['friends'])
                    print('Bio:                       ',account['bio'])
                    print('Created:                   ',account['created'])
                    print('Number Tweets:             ',account['number_of_tweets'])
                    print('URL:                       ',account['url'])
                    print('Default profile image?:    ',account['default_image'])
                    print('Score:                     ',account['score'])   
                    ctr += 1        
                    print('\n---------------------------------------------------')
        print('\n\n\n')

#function to calculate the probability of the suspected follow-bot 
def probFollowBots(followBotList):
  lst = []

  for account in followBotList:
    #probability = (score/ max possible score)%
    prob = str(round(((account['score']/8) * 100),2)) + '%'
    lst.append({'screen_name': account['screen_name'], 'probability': prob})

  return lst

#Menus
#start Menu
def endDetails():
  print('\nProgram is ending!')
  print('\nAuthor: Eniola Adebayo Osineye')
  print('All rights reserved © Copyright 2019 FindFoloBoto')

#program main menu
def mainMenu():
    print('\n[1] Examine Follow-bots.')
    print('[0] Exit program.')

#follow-bot examination menu
def botExaminationMenu():
    print('\nFollow-bot examination options')
    print('[1] Option 1 - Print a list of suspected follow-bots')
    print('[2] Option 2 - Print the probability of account being a follow-bot')
    print('[3] Option 3 - Print a short report of follow-bot(s)')
    print('[4] Option 4 - Print a long report of follow-bot(s)')
    print('[5] Option 5 - Help me!!! ')
    print('[0] Exit bot-examination options')


#follow-bot probability menu
def probabilityMenu():
 print('\nShowing probability of follow-bots options')
 print('[1] Option 1 - Print in ascending order')
 print('[2] Option 2 - Print in descending order')
 print('[3] Option 3 - Help me!!! ')
 print('[0] Exit probability options')

#short report menu
def shortReportMenu():
 print('\nShort report options')
 print('[1] Option 1 - Short report for one-to-many specific accounts')
 print('[2] Option 2 - Short report for specific percentage of follow-bots')
 print('[3] Option 3 - Help me!!! ')
 print('[0] Exit short report options!')

#long report menu
def longReportMenu():
 print('\nLong report options')
 print('[1] Option 1 - Long report for one-to-many specific accounts')
 print('[2] Option 2 - Long report for specific percentage of follow-bots')
 print('[3] Option 3 - Help me!!! ')
 print('[0] Exit long report options!')

#Help
#long report help
def longReportHelp():
 print('\n---------------------------------------------------\n')
 print('Long report options help')
 print('\nThese options allows the user to print a long') 
 print('report on each suspected follow-bot. You have the ')
 print('option get one or more specific users ') 
 print('from the list of follow-bots or 0 to 100 percent ')
 print('of the follow-bots.')
 print('\nWhen entering the screen names of twitter')
 print('accounts to get a report on, the screen names can')
 print('be entered in any capitalization schemes desired.')
 print('And if a screen name entered is wrong, it does not')
 print('affect the search of the other screen names entered') 
 print('correctly.')
 print ('\n---------------------------------------------------\n')

#follow-bot examination help
def botExaminationHelp():
 print('\n---------------------------------------------------\n')
 print('Follow-bot examination options help')
 print('\nThese options allow the user to print a list of ') 
 print('the screen names of suspected follow-bots and ')
 print('allows the user to enter into follow-bot probability ')
 print('options, short and long description report options. ') 
 print ('\n---------------------------------------------------\n')

#short report help
def shortReportHelp():
 print('\n---------------------------------------------------\n')
 print('Short report options help')
 print('\nThese options allows the user to print a short ') 
 print('report on each suspected follow-bot. You have the ')
 print('option get one or more specific users ') 
 print('from the list of follow-bots or 0 to 100 percent ')
 print('of the follow-bots.')

 print('\nWhen entering the screen names of twitter')
 print('accounts to get a report on, the screen names can')
 print('be entered in any capitalization schemes desired.')
 print('And if a screen name entered is wrong, it does not')
 print('affect the search of the other screen names entered') 
 print('correctly.')
 print ('\n---------------------------------------------------\n')

#follow-bot probability help
def probabilityHelp():
 print ('\n---------------------------------------------------\n')
 print('Probability options help')
 print('\nThese options allow the user to print the list ')
 print('of suspected follow-bots. You have the option to ')
 print('print in ascending or desceneding order.')
 print('\n---------------------------------------------------\n')

#program intro 
def intro():
 print("\n\n\nWelcome to FindFoloBoto 1.0.0")

if __name__ == '__main__':
 intro()
 main()
 

