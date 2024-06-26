# WordGuesser

WordGuesser is a Python project designed to help you find words based on specific criteria such as the number of letters, starting letters, and ending letters. This project reads from a file containing a list of words and filters them based on user input.

## Features

- Filter words by the number of letters.
- Filter words by the starting letters.
- Filter words by the ending letters.
- Combine multiple criteria to find specific words.

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python installed on your machine.

## Usage

1. Download the polish data file `slowa.txt` from [this link](https://drive.google.com/file/d/1VGpozR2hwmsoKxGEc4LXqSz9LFnhZMkm/view?usp=sharing).
2. Place the `slowa.txt` file in the same directory as `main.py`.
3. Run the script using the following command:
   ```bash
   python main.py
   ```

## Example

Upon running the script, you will be prompted to specify your criteria:

- Whether you want to filter by the number of letters.
- Whether you want to filter by the starting letters.
- Whether you want to filter by the ending letters.

For each criterion, you will be asked to input the specific details. For example, if you choose to filter by the number of letters, you will be prompted to enter the desired number of letters.

Example interaction:
```
Jesli TAK to T, jesli NIE to N
Czy chcesz podac ilosc liter?
T
Czy chcesz podac na jaka/jakie zaczyna sie wyraz?
N
Czy chcesz podac na jaka/jakie konczy sie wyraz?
N
Podaj liczbe liter wyrazu jaki chcesz dostac:
5

Twoje kryteria to:
Liczba liter: 5

['kotka', 'domku', 'zegar']
```

## Code Overview

The main logic of the script is as follows:

1. Open and read the `slowa.txt` file.
2. Prompt the user for filtering criteria.
3. Filter the words based on the specified criteria.
4. Print the list of words that match the criteria.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to reach out if you have any questions or need further assistance. Enjoy using WordGuesser!
