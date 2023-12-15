choice = input("Change A or B?\n")
text_to_sorted = input(str("Please enter a text: "))
alphabets = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
alphabets1 = 'abcdefghijklmnopqrstuvwxyz'
class Dictionary():
    def choice(self, text):
        if choice == 'A' or choice == 'a':
            self.choice_A(text)
        elif choice == 'B' or choice == 'b':
            self.choice_B(text)
        else:
            print('Unsupported')

    def choice_A(self, text):
        list_txt_A = text.split(' ')
        list_txt_A.sort()
        list_txt_A = ', '.join(list_txt_A)
        print(list_txt_A)

    def choice_B(self, text):
        for i in alphabets1:
            count = text.count(i) + text.count(i.upper())
            if count == 0:
                continue
            print(("{} - {}".format(i.upper(), count)))

object1 = Dictionary()
object1.choice(text_to_sorted())