import user
import hangmangame as HM

def main():
    word = HM.get_word()
    HM.play(word)
    while input("Want To Play Again? (Y/N) ").upper() == "Y":
        word = HM.get_word()
        HM.play(word)
        
if __name__ == "__main__":
    user.register_user()
    main()
