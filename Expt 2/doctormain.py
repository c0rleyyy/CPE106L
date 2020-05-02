from doctor import Doctor

"""
main method for view purpose
it is the interactive from user 
and display messages
"""


def main():
    d = Doctor()
    print(d.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(d.farewell())
            break
        print(d.reply(sentence))


# The entry point for program execution
if __name__ == "__main__":
    main()