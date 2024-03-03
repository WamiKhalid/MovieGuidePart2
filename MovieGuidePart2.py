# Function to display the menu choices for the user
def display_menu():
    print("\nCOMMAND MENU")
    print("list  -  List all movies")
    print("add   -  Add a movie")
    print("del   -  Delete a movie")
    print("exit  -  Exit program")

# Function to open the file and populate the list with movie titles
def read_file_into_list(filename):
    movie_list = []
    with open(filename, 'r') as file:
        for line in file:
            movie_list.append(line.strip())
    return movie_list

# Function to display all movie titles
def display_movies(movie_list):
    print("\nMovies:")
    for index, movie in enumerate(movie_list, start=1):
        print(f"{index}. {movie}")

# Function to add a movie to the list and write the updated list to the file
def add_movie(movie_list, movie, filename):
    movie_list.append(movie)
    with open(filename, 'w') as file:
        for movie_title in movie_list:
            file.write(movie_title + "\n")
    print(f"\n{movie} was added.")

# Function to delete a movie from the list and write the updated list to the file
def delete_movie(movie_list, movie_number, filename):
    if movie_number < 1 or movie_number > len(movie_list):
        print("\nInvalid Movie number.")
    else:
        deleted_movie = movie_list.pop(movie_number - 1)
        with open(filename, 'w') as file:
            for movie_title in movie_list:
                file.write(movie_title + "\n")
        print(f"\n{deleted_movie} was deleted.")

# Main function
def main():
    filename = "movies.txt"
    movie_list = read_file_into_list(filename)
   
    display_menu()
   
    while True:
        command = input("\nCommand: ").lower()
       
        if command == "list":
            display_movies(movie_list)
        elif command == "add":
            movie = input("Movie: ")
            add_movie(movie_list, movie, filename)
            display_movies(movie_list)
        elif command == "del":
            movie_number = int(input("Number: "))
            delete_movie(movie_list, movie_number, filename)
            display_movies(movie_list)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()
