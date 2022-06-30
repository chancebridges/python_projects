# when you pass a list to a function, the function can modify the list.
 
# # any changes made to the list inside the function's body are permanent, 
# allowing you to work efficiently even when you're dealing with large amounts of data.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design. 
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
# we set up a list of unprinted designs and an empty list that will hold the ocmpleted models. 
# All we have to do is call the functions and pass them the right arguments.
# This example demonstrates the idea that every function should have one specific job. 
