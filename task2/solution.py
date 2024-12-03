import requests
from bs4 import BeautifulSoup
import csv

def main():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    animals_count = {}
    groups = soup.find_all('div', class_='mw-category-group')

    for group in groups:
        letter_first = group.find('h3').text.strip()   
        animal_links = group.find_all('a')   
        animals_count[letter_first] = len(animal_links)   

    # Wtiting to csv 
    with open('beasts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for letter_first, count in animals_count.items():
            writer.writerow([letter, count])   

    if os.path.exists(filename):
        print("File saves as beasts.csv")
    else:
        print("ERROR! Saving wasnt successful")


if __name__ == "__main__":
    main()