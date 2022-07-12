# sometimes you'll want to prevent a function from modifying a list.
# if you want to keep an original list but still use it in a function, then you
# can address this issue by passing the function a copy of the list, not the original. 

# you can send a copy of a list to a function like this (look below)
# function_name(list_name[:])
# the slice notation [:] makes a copy of the list to send to the function

# refer to modifying_a_list_in_a_function.py
# if we did not want to empty the list of unprinted designs, we could call 
# print_models() like this: print_models(unprinted_designs[:], completed_models)
#  **This is done when calling the function, not in the function itself***