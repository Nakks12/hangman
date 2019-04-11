#coding:utf-8

def hangman(word):
    wrong = 0
    stages = ["",
              "     |     ",
              "     o     ",
              "    /|\    ",
              "    / \    ",
              "___________"]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")

    while wrong < len(stages) - 1:
        print("\n")
        char = input("文字を入力してね: ")

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1

        print(" ".join(board))
        print("\n".join(stages[0: wrong+1]))
        if "_" not in board:
            print("あなたの勝ち！")
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong+1]))
        print("あなたの負け！")

hangman("cat")
            
