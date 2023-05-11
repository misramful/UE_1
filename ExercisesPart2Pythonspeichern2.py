#for loops fixed number of times
#while loop, execute something while some condition remains true


def count_a_number(numbers, number):
    numbers = [2, 3, 2, 4, 2, 5, 6, 2, 2]
    counter = 0
    for number in numbers:
        if (number == 2):
            counter += 1
    return int(counter) #Achtung zu integer machen




def play_with_lists(numbers, number):
    numbers = [2, 5, 6, 9, 3]
    number = 5
    #print(numbers)
    copy = numbers.copy() #copy methode
    #print(copy)

    copy.reverse()
    print(copy)

    index = numbers.index(number) #AUSBESSERN!!! #index-methode spricht bestimmte stelle an
    numbers[index] = 1
    print(numbers)
    #sorted version of list with number 1
    sort_numbers = sorted(numbers)
    #print(sort_numbers) #sortierte nachdem "5" zu eins getauscht wurde
    #sorted verwendet weil hier eine neue Liste erstellt wird, die Originalliste bleibt gleich
    sort_numbers.reverse()
    print(sort_numbers)




def compare_lists (list1, list2):
    list1 = ["banana", "apples", "oranges"]
    list2 = ["apples", "cherries", "strawberries"]
    print(set(list1).intersection(list2)) #Achtung, zuerst zum set machen

def remove_dubplicates(items):
    items = ["My", "favourite", "colour", "is", "blue", "His", "favourite", "colour", "is", "yellow"]
    items = (set(items)) #Achtung nur wenn Anordnung egal ist
    print(items)


def remove_duplicate_my_way(items):
    items = ["Hanna", "Marc", "Jojo", "Lukas", "Lukas", "Katha", "Kaleef", "Julia", "Allen", "Julia"]

    no_duplicates = []
    for element in items:
        if element not in no_duplicates:
            no_duplicates.append(element) #append -> immer ein element wird hinzugefügt
    print(no_duplicates)

def describe_computer(computer):
    computer = {"Type": "Notebook", "Brand": "Dell ", "Price": 2000}
    computer_type = computer.get("Type", "unknown type")
    computer_brand = computer.get("Brand", "unknown brand")
    computer_price = computer.get("Price", "unknown price")

    computer["OS"] = "Linux"
    print(computer)


    print(f"You have a {computer_type} from {computer_brand} that costs {computer_price}€.")








print(count_a_number(3, 4))
play_with_lists(6, 7)
compare_lists("eins", "zwei")
remove_dubplicates("colours")
remove_duplicate_my_way("names")
describe_computer("typing machine")