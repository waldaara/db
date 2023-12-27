from auth import *

from db import connect_to_mysql

# config = {
#     "host": "aws.connect.psdb.cloud",
#     "user": "oiz6rvc7lfcomf85u0rf",
#     "password": "pscale_pw_f4s4xJpZ9LsZUgFrSldM6LpWTIUbxDy7VLJxlHSUo4i",
#     "database": "netflix",
#     "raise_on_warnings": True,
# }
#
# cnx = connect_to_mysql(config, attempts=3)
#
# if cnx and cnx.is_connected():
#     with cnx.cursor() as cursor:
#         result = cursor.execute("SELECT * FROM serie")
#         rows = cursor.fetchall()
#
#         for rows in rows:
#             print(rows)
#
#     cnx.close()
# else:
#     print("Could not connect")


def optionMovies():
  print("\n_____MOVIES______\n")
  print("-----Algebra Relacional-----")
  print("π titulo, duracion (Pelicula)")
  print("----------\n")

  with open("movies.txt", "r") as moviesFile:
    moviesFile.readline()

    for movie in moviesFile:
      movie = movie.strip()
      movieProps = movie.split(",")
      movieTitle = movieProps[0]
      movieDuration = movieProps[1]

      print(f"\n Title: {movieTitle} \n Duration: {movieDuration} \n")



def optionSeries():
  print("\n______SERIES______\n")
  print("-----Algebra Relacional-----")
  print("π titulo, número (Serie ⨝ Temporada )")
  print("----------\n")

  with open("series.txt", "r") as seriesFile:
    seriesFile.readline()

    for serie in seriesFile:
      serie = serie.strip()
      serieProps = serie.split(",")
      serieTitle = serieProps[0]
      serieSeasons = serieProps[1]

      print(f"\n Title: {serieTitle} \n Seasons: {serieSeasons} \n")


#shows the movies and series of the platform
def optionHome():
  print("\n________HOME_________\n")

  optionMovies()

  optionSeries()


#Shows the profile's list
def optionMyList(idProfile):
  print("\n________YOUR LIST_________\n")
  print("-----Algebra Relacional-----")
  print("σ id_pelicula != null (π id_pelicula (σ esFavorito = true (Perfil ⨝ Visualización))) ∪ σ id_serie != null (π id_serie (σ esFavorito = true (Perfil ⨝ Visualización)))")
  print("----------\n")

  with open("lists.txt", "r") as listsFile:
    listsFile.readline()

    for listsItem in listsFile:
      listsItem = listsItem.strip()

      listsItemProps = listsItem.split(",")
      id = listsItemProps[0]
      myList = listsItemProps[1]

      if id == idProfile:
        myList = myList.split("-")
        for item in myList:
          print(item)




def optionSearch():
  print("\n________SEARCH_________\n")

  option = 0

  while option not in [1,2]:
    print("1. Movies")
    print("2. Series")
    print("3. Exit")

    option = int(input("Choice: "))

    match option:
      case 1:

        movieAsked = input("Write the movie's name: ")
        print("-----Algebra Relacional-----")
        print("π titulo,duración (σ titulo = '*nombre seleccionado*' (Pelicula))")
        print("----------\n")
        with open("movies.txt", "r") as movies:
          movies.readline()

          for movie in movies:
            movie = movie.strip()
            pelicula, duracion = movie.split(",")

            if pelicula == movieAsked:
              print(f"Movie found!: \n {pelicula} - {duracion}")

      case 2:

        print("----------\n")
        serieAsked = input("Write the serie's name: ")
        print("-----Algebra Relacional-----")
        print("π titulo, número ( σ titulo = '*nombre seleccionado*' (Serie) ⨝ Temporada)")
        with open("series.txt", "r") as series:
          series.readline()

          for serie in series:
            serie,temporadas = serie.split(",")
            if serie == serieAsked:
              print(f"Serie found!: \n {serie} has:")
              contador = 1
              while contador <= int(temporadas):
                print(f"Season: {contador}")
                contador += 1





def mainMenu(idprofile):
  print("\n___________NETFLIX__________\n")

  opcion = 0

  while opcion != 6:
    print("\n1. Home")
    print("2. Movies")
    print("3. Series")
    print("4. My List")
    print("5. Search")
    print("6. Exit\n")

    opcion = int(input("Select an option: "))

    match opcion:
      case 1:
        optionHome()
      case 2:
        optionMovies()
      case 3:
        optionSeries()
      case 4:
        optionMyList(idprofile)
      case 5:
        optionSearch()
      case _:
        print("Validn't option")


