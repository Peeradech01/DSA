"""Sorting"""


def insertionSort(list, last):
    counter = 0

    for i in range(1, last + 1):
        current = list[i]
        j = i - 1
        
        while j >= 0 and list[j] > current:
            list[j + 1] = list[j]
            j -= 1
            counter += 1

        list[j + 1] = current
        print(list)

    if counter == 0:
        counter = last
    else:
        counter = counter + last - 1

    print("Comparison times:", counter)
    print()

insertionSort([23, 78, 45, 8, 32, 56], 5)




def selectionSort(list, last):
    """Selection"""

    counter = 0

    for i in range(last):
        smallest = i
        walker = i+1

        while walker <= last:
            counter += 1
            if list[walker] < list[smallest]:
                smallest = walker
            walker += 1
        
        list[smallest], list[i] = list[i], list[smallest]

        print(list)

    print("Comparison times:", counter)
    print()
    
    
selectionSort([23, 78, 45, 8, 32, 56], 5)




def bubbleSort(lst, last):
    """BubbleSort"""

    current = 0
    sorted = False
    counter = 0
    
    while current <= last and not sorted:
        walker = last
        sorted = True
        
        while walker > current:
            counter += 1
            
            if lst[walker] < lst[walker-1]:
                sorted = False
                lst[walker], lst[walker-1] = lst[walker-1], lst[walker]
            
            walker -= 1
        
        current += 1
    
        print(lst)
    print("Comparison times:", counter)
    print()
    

bubbleSort([23, 78, 45, 8, 32, 56], 5)





"""CardSort"""

def insertionCardSort(cards, last):
    counter = 0
    for i in range(1, last + 1):
        current = cards[i]
        j = i - 1
        while j >= 0 and cardValue(cards[j]) > cardValue(current):
            counter += 1
            cards[j + 1] = cards[j]
            j -= 1
        cards[j + 1] = current
        print(cards)
    if counter == 0:
        counter = last
    else:
        counter = counter + last - 1
    print("Comparison times:", counter)
    print()
    


def selectionCardSort(cards, last):
    counter = 0
    for i in range(last):
        min_index = i
        for j in range(i+1, last+1):
            counter += 1
            if cardValue(cards[j]) < cardValue(cards[min_index]):
                min_index = j
        cards[i], cards[min_index] = cards[min_index], cards[i]
        print(cards)
    print("Comparison times:", counter)
    print()



def bubbleCardSort(cards, last):
    counter = 0
    for i in range(last):
        for j in range(last-i):
            counter += 1
            if cardValue(cards[j]) > cardValue(cards[j+1]):
                cards[j], cards[j+1] = cards[j+1], cards[j]
        if counter == 0:
            break
        print(cards)
    print("Comparison times:", counter)
    print()
    


def cardValue(card):
    faceValues = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
    suitValues = {"♣": 0, "♦": 1, "♥": 2, "♠": 3}
    return (faceValues[card[:-1]], suitValues[card[-1]])
    


def main():
    print("Insettion")
    insertionCardSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
    print("Selection")
    selectionCardSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
    print("Bubble")
    bubbleCardSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
    
main()


     