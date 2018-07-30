#this is just a messaround for testing out python stuff
game = "the name game"
print(game.upper())
name = input("What is your name: ")
nickname=name[:4]
print("Your nickname is " + nickname)
endMessage = "%s is now over. Thanks for playing" % game
gameOver = input(endMessage)
