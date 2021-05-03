import sys

def trivia():

    choice = input('Ready to take a Trivia Quiz? yes/no: ')

    score = 0
    total = 10

    if choice == 'yes':
        question = input('1. who is the founder of Microsoft?: ')
        if question.lower() == 'bill gates':
            score +=1
            print('correct!')
        else:
            print('wrong')
    
        question = input('2. _____ is developed by guido van rossum: ')
        if question.lower() == 'python':
            score +=1
            print('correct!')
        else:
            print('wrong')

        question = input('3. HTML is a programming language? (yes/no): ')
        if question.lower() == 'no':
            score +=1
            print('correct!')
        else:
            print('wrong')
    
        question = input('4. Java and Javascript is the same  (true/false): ')
        if question.lower() == 'false':
            score +=1
            print('correct!')
        else:
            print('wrong')
        
        question = input('5. who is the first computer programmer  ?: ')
        if question.lower() == 'ada lovelace':
            score +=1
            print('correct!')
        else:
            print('wrong')
        
        question = input('6. data structure that contains group of elements ')
        if question.lower() == 'array':
            score +=1
            print('correct!')
        else:
            print('wrong')

        question = input('7. father of computer science and artificial intelligence: ')
        if question.lower() == 'alan turing':
            score +=1
            print('correct!')
        else:
            print('wrong')
        
        question = input('8. founder of apple: ')
        if question.lower() == 'steve jobs':
            score +=1
            print('correct!')
        else:
            print('wrong')
        
        question = input('9. Javascript is a programming language (true/false): ')
        if question.lower() == 'true':
            score +=1
            print('correct!')
        else:
            print('wrong')
        
        question = input('10. if ("2" == "02") {  echo "true";} else {echo "false";}: ')
        if question.lower() == 'true':
            score +=1
            print('correct!')
        else:
            print('wrong')


        print('well played! you got',score ,'correct answer!')
        grade = (score/total)*100
        print('your grade is', str(grade), '% thank you for playin!')

        again = str(input('Want another try? (yes/no)'))
        if again == 'yes':
            trivia()
        else:
            print('Thank you for playin! have a great day ahead')
            sys.exit(0)

    print('ok some other time..')

trivia()