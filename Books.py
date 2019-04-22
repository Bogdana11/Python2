   
def show_help():
  print("what should we pick up at the stoore?")
  print("""
Enter 'DONE' to stop adding items .
Enter 'HELP' to get help.
Enter 'SHOW' to get the list
  """)
Books_List = []
def add_to_list(item):
     Books_List.append(item)
     print("Added there are {}books".format(len(Books_List)))
def show_list():
     print("here is your list")
     for item in Books_List:
         print(item)
  
show_help()
  
while True: 
            new_item = input(">")
            if new_item == 'DONE':
                 break
            elif  new_item == 'HELP':
                 show_help()
                 continue
            elif new_item == 'SHOW':
                 show_list()
                 continue
            add_to_list(new_item)