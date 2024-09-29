import colorama.ansi
from faker import Faker
from colorama import Fore


fake = Faker()
colorama.init(autoreset=True)

banner = '''
   ___                             ___ __        ___  _                 __       
  / _ \___ _______ ___  ___  ___ _/ (_) /___ __/ _ \(_)__ ___  _______/ /__ ____
 / ___/ -_) __(_-</ _ \/ _ \/ _ `/ / / __/ // / // / (_-</ _ \/ __/ _  / -_) __/
/_/   \__/_/ /___/\___/_//_/\_,_/_/_/\__/\_, /____/_/___/\___/_/  \_,_/\__/_/   
                                        /___/                            V 1.1                                                                                                                                     
                                                                         Created By Mr. Bilred
                                                                            
This tool generates random, fake personal details like name, email, address, and other key attributes. 
It can be used for testing, filling dummy data, or experimenting with data processing.

Note: This is not a critical project; it’s primarily for fun and educational purposes.
(maybe I was trying to fill my boredom, or maybe I got an idea to make such tool)

GitHub: https://github.com/BilalAhmadKhanKhattak
'''
print(Fore.LIGHTMAGENTA_EX + banner)


def generate_extended_fake_data(num_entries_range):
    for _ in range(num_entries_range):
        fake_data = {
            "Name:": fake.name(),
            "Email: ": fake.email(),
            "Address:": fake.address(),
            "Date Of Birth:": fake.date_of_birth(),
            "Phone Number:": fake.phone_number(),
            "Job: ": fake.job(),
            "Company: ": fake.company(),
            "Website: ": fake.url(),
            #  "Image: ": fake.image_url()
        }
        print_fake_data(fake_data)  # I forgot the indentation here, which also waste alot of my time xd


def fake_profile():
    profile = fake.profile()
    for key, value in profile.items():
        print(Fore.LIGHTMAGENTA_EX + f"{key}: {value}")


def print_fake_data(fake_data):
    for key, value in fake_data.items():
        print(Fore.LIGHTCYAN_EX + f" {key}: {value}")
    print(Fore.LIGHTCYAN_EX + "-" * 40)


if __name__ == "__main__":
    try:
        num_entries_input = input(Fore.LIGHTCYAN_EX + "Enter the number of personalities you wanna generate("
                                                         "Leaving it "
                                                         "Blank makes 5): ")  # Specify number of entries
        if num_entries_input.strip() == "":
            num_entries = 5
        else:
            num_entries = int(num_entries_input)

        if num_entries == 1:
            print(Fore.LIGHTMAGENTA_EX + "NEW PERSONALITY WITH RANDOM DETAILS CREATED:")

        else:
            print(Fore.LIGHTMAGENTA_EX + "NEW PERSONALITIES WITH RANDOM DETAILS CREATED:")  # I also kept an eye on
            # grammar :)

        generate_extended_fake_data(num_entries)

        print(Fore.LIGHTCYAN_EX + "Extra Profile Created: ")
        fake_profile()

    except ValueError:
        print(Fore.LIGHTRED_EX + "Just Enter any INTEGER, Man")
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error Occurred: {e}")

    print(Fore.LIGHTYELLOW_EX + "\nTake A Look at the information, use your mind too, this is fake data, so keep an eye"
                                "on everything above")