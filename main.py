

import register

def main():
    language = input(f"""
                CHOOSE THE LANGUAGE
        1. O`zbek tili
        2. Pусский язык
        3. English language>>> """)
    if language == "1":
        return register.register()
    else:
        return main()


if __name__ == "__main__":
    main()
