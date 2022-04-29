#
# Name:
#

from Proj2_tree import printTree

#
# The following two trees are useful for testing.
#
smallTree = \
    ("Is it bigger than a breadbox?",
        ("an elephant", None, None),
        ("a mouse", None, None))
mediumTree = \
    ("Is it bigger than a breadbox?",
        ("Is it gray?",
            ("an elephant", None, None),
            ("a tiger", None, None)),
        ("a mouse", None, None))

yes_prompts = ["yes", "yep", "sure", "yup", "y", "yas"]

def main():
    """DOCSTRING!"""
    # Write the "main" function for 20 Questions here.  Although
    # main() is traditionally placed at the top of a file, it is the
    # last function you will write.

    print("Welcome to 20 Questions Game!")
    tree = smallTree
    while True:
        tree = play(tree)
        userinput = input("Would you like to play again?")
        if not yes(userinput):
            userinput2 = input("Would you like to save this tree for later?")
            if userinput2.lower() == 'yes':
                userinput3 = input("Please enter a file name: ")
                document = open(userinput3, "w")
                saveTree(tree, document)
                document.close()
            else:
                pass
            print("Thank you for playing!")
            break


def simplePlay(tree):
    """DOCSTRING!"""
    # print("ygyb", tree, "blahblah", type(tree), "\n")
    answer, yes_res, no = tree

    if isLeaf(tree):
        ans = playAnswer(answer)
        if yes(ans):
            return True, None
        else:
            return False, tree[0]
    else:
        x_1 = input(f"{tree[0]} \n")
        if yes(x_1):
            return simplePlay(yes_res)

        else:
            return simplePlay(no)


def isLeaf(tree):
    answer, yes, no = tree
    if yes == None  and no == None:
        return True
    else:
        return False

def playAnswer(answer):
    x = input(f"is your object {answer}? \n")
    return x


def play(tree):
    """DOCSTRING!"""
    x, old_ans = simplePlay(tree)
    if x == False:
        ans = input("What was it?")
        que = input(f"What's a question that distinguishes between {ans} and {old_ans}?")
        ques2 = input (f"What's the answer for {ans}?")
        if yes(ques2):
            tup = (que, (ans, None, None), (old_ans, None, None))
        else:
            tup = (que, (old_ans, None, None), (ans, None, None))
        old_tup = (old_ans, None, None)
        return replace(tree, old_tup, tup)
    else:
        print("I gotcha!")
        return tree

def replace(tree, old_tup, new_tup):
    flag = False
    if isLeaf(tree):
        if old_tup == tree:
            return new_tup
        else:
            return tree
    else:
        return (tree[0], replace(tree[1], old_tup, new_tup), replace(tree[2], old_tup, new_tup))



    # Keep copying the tree to new tree and when it reaches tiger, update Tiger
def saveTree(tree, treeFile):
    # print("Spish is spiced fish.", file = document)
    if isLeaf(tree):
        print("Leaf ", file=treeFile)
        print(tree[0], file=treeFile)
    else:
        print("Internal Node ", file=treeFile)
        print(tree[0], file=treeFile)
        saveTree(tree[1], treeFile)
        saveTree(tree[2], treeFile)

def yes(prompt):
    if prompt.lower() in yes_prompts:
        return True
    return False


# def loadtree(treeFile):
#     while True:
#         line = treeFile.readline()
#         if line=="":
#             break
#         line = line.strip()
#         if line=="Leaf":
#             pass
#         if line=="Internal Node":
#             pass

# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()
