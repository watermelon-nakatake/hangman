def hangman():
    import random
    ans = "y"
    words = ["cat","dog","bat","elephant","rion","bird","monkey","bug"]
    print("ハングマンへようこそ！")
    while ans == "y" :
        w_num = random.randint(0,len(words)-1)
        word = words[w_num]
        wrong = 0

        stages = ["",
                  "_________           ",
                  "|                   ",
                  "|         |         ",
                  "|         0         ",
                  "|        /|\        ",
                  "|        / \        ",
                  "|                   ",
                  ]
        rletters = list(word)
        board = ["_"] * len(word)
        win = False
        while wrong < len(stages) - 1:
            print("\n")
            msg = "１文字を予想してね: "
            char = input(msg)
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = "$"
            else:
                wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))
            if "_" not in board:
                print("あなたの勝ち！")
                print(" ".join(board))
                win = True
                break
        if not win:
            print("\n".join(stages[0:wrong+1]))
            print("貴方の負け！正解は {}.".format(word))
        ans = input("ゲームを続けますか？(y/n): ")
        if ans == "n":
            break
        
hangman()
            
