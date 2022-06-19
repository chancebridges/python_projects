favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

poll_takers = ['chance' , 'nick', 'jen', 'sarah', 'edward', 'phil']
for poll_taker in poll_takers:
    if poll_taker in favorite_languages.keys():
        print("Thank you " + poll_taker.title() + 
        " for responding.")
    if poll_taker not in favorite_languages.keys():
        print(poll_taker.title() + " please respone to the poll.")