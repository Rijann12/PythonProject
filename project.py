import random

class Game:
    def __init__(self):
        self.levels = [Level(1), Level(2), Level(3)]
        self.current_level = 0
        self.player = Player()
        self.question_bank = QuestionBank()
    
    def start(self):
        print("Welcome to the Quiz Game!")
        print("Categories: Country, Animal, Car, Phone, Colors")
        while self.current_level < len(self.levels):
            level = self.levels[self.current_level]
            self.play_round(level)
            self.current_level += 1
        print(f"Congratulations, {self.player.name}! You've completed all levels with a score of {self.player.score}.")

    def play_round(self, level):
        display = Display(level)
        input_handler = InputHandler()
        print(f"\nStarting Level {level.difficulty}")
        
        for i in range(3):
            category = random.choice(list(self.question_bank.questions.keys()))
            question = self.question_bank.get_question(category, level)
            display.show_question(question)
            answer = input_handler.get_answer()
            if question.check_answer(answer):
                print("Correct!")
                self.player.increment_score()
            else:
                print(f"Wrong! The correct answer was: {question.answer}")
        print(f"Your score: {self.player.score}")

class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.score = 0

    def increment_score(self):
        self.score += 1

class QuestionBank:
    def __init__(self):
        self.questions = {
            'country': [
                Question('What is the capital of France?', 'Paris', 1),
                Question('Which country has the largest population?', 'China', 2),
                Question('What is the smallest country in the world?', 'Vatican City', 3),
            ],
            'animal': [
                Question('What is the fastest land animal?', 'Cheetah', 1),
                Question('Which mammal is known to have the most powerful bite?', 'Hippopotamus', 2),
                Question('What is the largest mammal?', 'Blue Whale', 3),
            ],
            'car': [
                Question('Which company manufactures the Mustang?', 'Ford', 1),
                Question('What is the best-selling electric car in the world?', 'Tesla Model 3', 2),
                Question('Which car company has a logo featuring four rings?', 'Audi', 3),
            ],
            'phone': [
                Question('What company makes the iPhone?', 'Apple', 1),
                Question('Which company developed the Android operating system?', 'Google', 2),
                Question('What was the first smartphone?', 'IBM Simon', 3),
            ],
            'colors': [
                Question('What color is a sapphire?', 'Blue', 1),
                Question('What color is created by mixing red and blue?', 'Purple', 2),
                Question('What color do you get when you mix all primary colors?', 'Brown', 3),
            ]
        }

    def get_question(self, category, level):
        suitable_questions = [q for q in self.questions[category] if q.difficulty == level.difficulty]
        return random.choice(suitable_questions)

class Question:
    def __init__(self, text, answer, difficulty):
        self.text = text
        self.answer = answer
        self.difficulty = difficulty

    def check_answer(self, answer):
        return answer.strip().lower() == self.answer.strip().lower()

class Display:
    def __init__(self, level):
        self.level = level

    def show_question(self, question):
        print(f"Question: {question.text}")

class Level:
    def __init__(self, difficulty):
        self.difficulty = difficulty

class InputHandler:
    def get_answer(self):
        return input("Your answer: ")

class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

if __name__ == "__main__":
    game = Game()
    game.start()
