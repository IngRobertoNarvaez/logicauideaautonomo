

#ifndef PONG_H
#define PONG_H

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>

// ============================
//  CONSTANTES DEL JUEGO
// ============================
#define WIDTH 60
#define HEIGHT 20

#define PADDLE_SIZE 4
#define BALL_SPEED 1
#define PADDLE_SPEED 1

// ============================
//  ESTRUCTURAS
// ============================

// Pelota
typedef struct {
    int x, y;       // posición
    int dx, dy;     // dirección
} Ball;

// Paleta
typedef struct {
    int x, y;       // posición superior de la paleta
} Paddle;

// Estado general del juego
typedef struct {
    Ball ball;
    Paddle leftPaddle;
    Paddle rightPaddle;
    int scoreLeft;
    int scoreRight;
} GameState;

// ============================
//  PROTOTIPOS
// ============================

// Inicialización
void InitGame(GameState *game);

// Renderizado
void DrawBorders();
void DrawPaddles(const GameState *game);
void DrawBall(const GameState *game);
void RenderGame(const GameState *game);

// Actualización
void UpdateBall(GameState *game);
void UpdatePaddles(GameState *game);

// Colisiones
void CheckCollision(GameState *game);

// Entrada de usuario
void HandleInput(GameState *game);

// Ciclo principal
void PlayPong();

// Utilidades
void GoToXY(int x, int y);
void ClearScreen();

#endif
