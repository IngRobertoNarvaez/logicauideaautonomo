#include "pong.h"

int main() {
    srand((unsigned int)time(NULL));

    while (TRUE) {
        printf("Press 1 to play Pong."
               "\nPress Esc to exit.");

        char option = getch();

        if (option == '1') {
            PlayPong();   // Llama al juego Pong
        } 
        else if (option == ESCAPE_KEY) {
            return 0;     // Salir
        }

        system("cls");
    }

    return 0;
}
