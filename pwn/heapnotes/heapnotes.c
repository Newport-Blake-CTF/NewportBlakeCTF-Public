#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* notes[0x10];
int note_idx;

void win() {
    system("/bin/sh");
}

void menu() {
    printf("1. Create Note\n");
    printf("2. Read Note\n");
    printf("3. Update Note\n");
    printf("4. Delete Note\n");
    printf("5. Exit\n");
}

void create_note() {
    void* chunk;

    if (note_idx >= 0x10) {
        printf("Max amount of notes created!\n");
        return;
    }

    chunk = malloc(0x40);

    while ( getchar() != '\n' );
    printf("Input note data: ");

    fgets(chunk, 0x40, stdin);
    
    notes[note_idx++] = chunk;

    printf("Note successfully added.\n");
};

void read_note() {
    int idx;

    if (note_idx <= 0) {
        printf("Create at least 1 note before you can read.\n");
        return;
    }
        
    printf("Note index (0-%d): ", note_idx-1);
    scanf("%d", &idx);
    if (idx < 0 || idx > note_idx-1) {
        printf("Invalid note index.\n");
        return;
    }
    
    puts(notes[idx]);
};

void update_note() {
    int idx;

    if (note_idx <= 0) {
        printf("Create at least 1 note before you can update.\n");
        return;
    }
        
    printf("Note index (0-%d): ", note_idx-1);
    scanf("%d", &idx);
    if (idx < 0 || idx > note_idx-1) {
        printf("Invalid note index.\n");
        return;
    }

    while ( getchar() != '\n' );
    printf("Input note data: ");

    fgets(notes[idx], 0x40, stdin);

    printf("Note successfully updated.\n");
};

void delete_note() {
    int idx;

    if (note_idx <= 0) {
        printf("Create at least 1 note before you can update!\n");
        return;
    }
        
    printf("Note index (0-%d): ", note_idx-1);
    scanf("%d", &idx);
    if (idx < 0 || idx > note_idx-1) {
        printf("Invalid note index.\n");
        return;
    }

    free(notes[idx]);

    printf("Note successfully deleted.\n");
};

int main() {
    int choice;

    printf("First heap chall? That's ok!\n");
    printf("Try taking some notes using my brand new app, heapnotes!\n");

    while (1) {
        menu();
        printf("> ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                create_note();
                break;
            case 2:
                read_note();
                break;
            case 3:
                update_note();
                break;
            case 4:
                delete_note();
                break;
            case 5:
                printf("Bye!\n");
                exit(0);
                break;
            default:
                printf("Invalid choice.\n");
        }
    }

    return 0;
}

__attribute__((constructor)) void init() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    return;
}
