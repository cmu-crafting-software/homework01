$ git clone https://github.com/cmu-crafting-software/Homework01.git E:/Desktop/17950_CraftingSoftware/Homework01
$ cd E:/Desktop/17950_CraftingSoftware/Homework01
$ git branch yinchenq
$ git add ClassRoster.md
$ git commit -m "Added name: Yincheng Qiu"
$ git push origin yinchenq

$ git commit -m "Added Year & College"
$ git branch new_yinchenq
$ git checkout new_yinchenq
$ git commit -m "Added fun fact"
$ git chekout yinchenq
$ git commit -m "Added programming language"
$ git merge new_yinchenq
$ git add E:/Desktop/17950_CraftingSoftware/Homework01/student_facts.txt
$ git commit -m "Merged fun fact"

