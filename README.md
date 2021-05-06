# Quizman

Quizman is a quiz program but also can be used as a training tool which runs in the terminal.
It takes the quizdata from a json database.

### Using quizman

To start quizzing or learning simply run `python quiz.py`. For now,
there are 4 modes the program can run in. Those modes are:
| Mode | Details |
| ---- | ------- |
| 1 random question | Asks one question from a random category, then returns to the main menu. |
| Random questions | Asks multiple questions until the user stops it. |
| Learning/Zen mode | Shows only the question and correct answers to it. |
| Learning/Zen mode (press for answer) | Same as above but doesn't reveal the answer immediately. |

### Structure of the database

The database format is structured to support categories like so:

```json
{
  "Category 1 - Colors": [
    {
      "Question": "Which of those is a color?",
      "Correct Answers": [1],
      "Answers": ["Red", "Yes", "No", "Demo answer"]
    },
    {
      "Question": "Select yes and no (multiple choice)?",
      "Correct Answers": [2, 3],
      "Answers": ["Red", "Yes", "No", "Demo answer"]
    }
  ],
  "Category 2 - Demo 2": [
    {
      "Question": "Select the demo answer",
      "Correct Answers": [4],
      "Answers": ["Red", "Yes", "No", "Demo answer"]
    }
  ]
}
```
