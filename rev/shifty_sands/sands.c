#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_flag()
{
    FILE *f = fopen("flag.txt", "r");
    char flag[64];
    fgets(flag, 64, f);
    printf("%s\n", flag);
    fclose(f);
}

char map[10][10] = {".###.....#",
                    "..#S.##..#",
                    "#.S#.#SS.#",
                    "#..#.#..##",
                    ".S.#.#.SS.",
                    ".###.#.S..",
                    "...#.#...S",
                    "##.#.####.",
                    ".S.S.#..S.",
                    "..S..#LS.."};
int timer = 0;

// void debug(int x, int y)
// {
//     printf("timer: %d\n", timer);
//     printf("x: %d, y: %d\n", x, y);
//     for (int i = 0; i < 10; i++)
//     {
//         for (int j = 0; j < 10; ++j)
//         {
//             if (i == x && j == y)
//             {
//                 printf("P");
//             }
//             else
//             {
//                 printf("%c", map[i][j]);
//             }
//         }
//         printf("\n");
//     }
// }

void shiftsands()
{
    // purposefully expand so compiler doesn't optimize out
    int dx = 0, dy = 0;
    int x = 0, y = 0;
    switch (timer % 4)
    {
        case 0:
            dx = 1;
            dy = 0;
            for (x = 9; x >= 0; x--)
            {
                for (y = 0; y < 10; y++)
                {
                    if (map[x][y] == 'S')
                    {
                        if (x + dx < 0 || x + dx >= 10 || y + dy < 0 || y + dy >= 10)
                        {
                            continue;
                        }
                        if (map[x + dx][y + dy] != '.')
                        {
                            continue;
                        }
                        map[x][y] = '.';
                        map[x + dx][y + dy] = 'S';
                    }
                }
            }
            break;
        case 1:
            dx = 0;
            dy = -1;
            for (y = 0; y < 10; y++)
            {
                for (x = 0; x < 10; x++)
                {
                    if (map[x][y] == 'S')
                    {
                        if (x + dx < 0 || x + dx >= 10 || y + dy < 0 || y + dy >= 10)
                        {
                            continue;
                        }
                        if (map[x + dx][y + dy] != '.')
                        {
                            continue;
                        }
                        map[x][y] = '.';
                        map[x + dx][y + dy] = 'S';
                    }
                }
            }
            break;
        case 2:
            dx = -1;
            dy = 0;
            for (x = 0; x < 10; x++)
            {
                for (y = 0; y < 10; y++)
                {
                    if (map[x][y] == 'S')
                    {
                        if (x + dx < 0 || x + dx >= 10 || y + dy < 0 || y + dy >= 10)
                        {
                            continue;
                        }
                        if (map[x + dx][y + dy] != '.')
                        {
                            continue;
                        }
                        map[x][y] = '.';
                        map[x + dx][y + dy] = 'S';
                    }
                }
            }
            break;
        case 3:
            dx = 0;
            dy = 1;
            for (y = 9; y >= 0; y--)
            {
                for (x = 0; x < 10; x++)
                {
                    if (map[x][y] == 'S')
                    {
                        if (x + dx < 0 || x + dx >= 10 || y + dy < 0 || y + dy >= 10)
                        {
                            continue;
                        }
                        if (map[x + dx][y + dy] != '.')
                        {
                            continue;
                        }
                        map[x][y] = '.';
                        map[x + dx][y + dy] = 'S';
                    }
                }
            }
            break;
    }
}

void move(char c, int *x, int *y)
{
    if (c == 'w'){
        if (*x == 0) {
            return;
        }
        if (map[*x - 1][*y] == '#' || map[*x - 1][*y] == 'S') {
            return;
        }
        *x -= 1;
    }
    if (c == 'a'){
        if (*y == 0) {
            return;
        }
        if (map[*x][*y - 1] == '#' || map[*x][*y - 1] == 'S') {
            return;
        }
        *y -= 1;
    }
    if (c == 's'){
        if (*x == 9) {
            return;
        }
        if (map[*x + 1][*y] == '#' || map[*x + 1][*y] == 'S') {
            return;
        }
        *x += 1;
    }
    if (c == 'd'){
        if (*y == 9) {
            return;
        }
        if (map[*x][*y + 1] == '#' || map[*x][*y + 1] == 'S') {
            return;
        }
        *y += 1;
    }
}

int main()
{
    int x = 0, y = 0;
    char c;
    // char *moves = malloc(50);
    while (1)
    {
        c = getchar();
        if (c == '\n')
        {
            continue;
        }   
        // moves[timer] = c;
        shiftsands();
        timer++;
        move(c, &x, &y);
        // debug(x, y);
        if (timer >= 50 || map[x][y] == 'S'){
            printf("ssssssssss\n");
            break;
        }
        if (map[x][y] == 'L')
        {
            read_flag();
            // printf("%s\n", moves);q
            return 0;
        }
    }
    return 1;
}