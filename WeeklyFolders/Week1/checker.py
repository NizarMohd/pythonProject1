
import WeeklyFolders.Week1.solutions as solutions
import WeeklyFolders.Week1.loader as loader
import os

def load():
    loader.load_file()
def unload():
    os.remove('temp.py')


def check(model, ans, marks, i):
    if model == ans:
        print("Test" + str(i) + ": " + "passed!")
        marks = marks + 1
    else:
        print("Test" + str(i) + ": " + "failed (TRY AGAIN :D)")
    i = i + 1
    return marks, i
def read_file(filename):
    # change based on input
    file = open(filename, "r")
    lines = file.readlines()
    return lines

# change fn name  with each qn
def check_question_name(lines):
    index = 1  #change with qn name
    i = 0
    marks = 0
    for line in lines:
        # change depending on input file
        arr = line.strip().split(" ")

        Questions = questions.Questions()
        Solutions = solutions.Solution()
        # model is our answer, ans is student's soln, suffix number is the questions number, change behavour name acc
        model1 = Questions.sum(x=int(arr[0]),y=int(arr[1]))
        ans1 = Solutions.sum(int(arr[0]),int(arr[1]))
        marks, i = check(model1, ans1, marks, i)
    print("Score for qn" + str(index) + ": " + str(marks * 100 / i) + "%")
if __name__ == '__main__':
    load()
    from WeeklyFolders.Week1 import temp as questions
    input1 = read_file("input1.txt")
    check_question_name(input1)
    unload()



