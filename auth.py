import uuid
from home import *

def signUp():
  print("\n_____CREATE AN ACCOUNT______\n")

  with open("auth.txt", "a") as authFile:
    email = input("Email: ")
    phoneNumber = input("Phone number: ")
    password = input("Password: ")
    profileId = str(uuid.uuid4()).replace("-", "")
    profileName = input("Profile Name: ")

    subscriptions = ["basic", "standar", "premium"]
    subscription = 0
    while subscription not in [1,2,3]:
      print("\nSubscription type: \n 1. Basic \n 2. Standar \n 3. Premium \n")
      subscription = int(input("Select an option: "))

    authFile.write(f"{email},{phoneNumber},{password},{profileId}|{profileName}-,{subscriptions[subscription-1]}\n")

    print("\nSigned up!")
    return True


def signIn():
  print("\n_____SIGN INTO YOUR ACCOUNT______\n")

  while True:
    emailOrPhoneNumber = input("Email or Phone Number: ")
    password = input("Password: ")

    with open("auth.txt", "r") as authFile:
      authFile.readline()

      for userLine in authFile:
        userLine = userLine.strip()
        userProps = userLine.split(",")
        email = userProps[0]
        phoneNumber = userProps[1]
        passwordDB = userProps[2]
        profiles = userProps[3].split("-")[:-1]

        if ((emailOrPhoneNumber in (email, phoneNumber)) and passwordDB == password):
          print("\nSigned in!\n")

          print("Profiles: \n")
          print("-----Algebra Relacional-----")
          print("π nombre(σ correo_cuenta = '*Cuenta Seleccionada*' (Cuenta) ⨝ Perfil)")
          print("----------\n")

          for i, profile in enumerate(profiles):
            profileProps = profile.split("|")

            profileName = profileProps[1]

            print(f"{i+1}. {profileName}")

          choice = 0

          while choice not in range(1, len(profiles)+1):
            choice = int(input("\nSelect a profile: "))

          return profiles[choice - 1].split("|")[0]

        else:
          print("\nIncorrect email/phoneNumber or password.")

          print("\n1. Try again \n 2. Exit\n")

          choice = input("Choice: ")

          match choice:
            case "1":
              break
            case "2":
              return None


def auth():
  print("\n________AUTH_________\n")

  choice = 0

  while choice not in [1,2,3]:
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Exit\n")

    choice = int(input("Choice: "))

  match choice:
    case 1:
      signUp()
    case 2:
      profileId = signIn()

      if profileId is not None:
        mainMenu(profileId)
    case 3:
      exit()
