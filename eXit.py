#just for fun

chances = 1

while chances == 1:
    print('''
    ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|

    ''')
    print("Welcome to eXit.")
    print("Your mission is to win the game\n")
    choice1 = input(
        "\nYou're trapped in a dungeon with your freind. You see a barrel.\nWhat do you do? (move the barrel/stay) "
    )
    if choice1 == "move the barrel":
        choice2 = input(
            "\nThe barrel rolls aside and you find a secret tunnel.\nWhat do you do? (enter the tunnel/stay) "
        )
        if choice2 == "enter the tunnel":
            choice3 = input(
                "\nYou start to escape but your friend is too week to go with you. They hand you a note.\nWhat do you do? (read the note/leave freind) "
            )
            if choice3 == "read the note":
                choice4 = input(
                    "\nIt is too dark to read the note.\nWhat do you do? (leave/light a match) "
                )
                if choice4 == "leave":
                    choice5 = input("\nYou crawl through the tunnel and the tunnel leads you to a beach.\nWhat do you do? (look/go back) ")
                    if choice5 == "look":
                        choice6 = input("\nIn the water you see a boat.\nWhat do you do? (get on the boat/stay)")
                        if choice6 == "get on the boat":
                            tryAgain = input("\nCongrats! You've successfully messed up!\n\nDo you want to try again? (yes/no)")
                            if (tryAgain == "yes"):
                              chances = 1
                            else:
                              print("Game Over!")
                              chances = 0
                              
                        else:
                          print("Game Over!")
                          chances = 0
                          
                    else:
                      print("Game Over!")
                      chances = 0
                      
                else:
                  print("Game Oover!")
            else:
              choice8 = input("\nThe note says, 'Do not leave me here.'\nDo you leave your friend or stay? (leave/stay) ")
              if choice8=='stay':
                print("\n\nYou found the eXit!")
                exit()
              else:
                print("Game Over!")  
                chances=0
            
        else:
          choice7 = input("\nYou friend hands you note.\nWhat do you do?(light a match/nothing)")
          if (choice7 == 'light a match'):
            choice8 = input("\nThe note says, Don not leave me here.\nDo you leave your friend or stay? (leave/stay) ")
            if choice8=='stay':
              print("\n\nYou found the eXit!")
              exit()
            else:
              print("Game Over!")  
              chances=0
          else:
            print("Game Over!")
            chances=0

    else:
      choice7 = input("\nYou friend hands you note.\nWhat do you do?(light a match/nothing)")
      if (choice7 == 'light a match'):
        choice8 = input("\nThe note says, 'Do not leave me here.'\nDo you leave your friend or stay? (leave/stay) ")
        if choice8=='stay':
          print("\n\nYou found the eXit!")
          exit()
        else:
          print("Game Over!")  
          chances=0
      else:
        print("Game Over!")
        chances=0


        
                   
                            
                            
                              



