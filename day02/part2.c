#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    char *direction;
    int units = 0;
    int horizontal = 0, depth = 0, aim = 0;

    if (2 != argc) {
        printf("usage: %s FILE_NAME\n", argv[0]);
    }

    fp = fopen(argv[1], "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    while ((read = getline(&line, &len, fp)) != -1) {
        if ('\n' == line[read - 1]) {
            line[read - 1] = '\0';
        }
        direction = strtok(line, " ");
        units = atoi(strtok(NULL, " "));
        if (!strcmp(direction, "forward")) {
            horizontal += units;
            depth += aim * units;
        } else if (!strcmp(direction, "up")) {
            aim -= units;
        } else if (!strcmp(direction, "down")) {
            aim += units;
        }
    }

    printf("horizontal: %d, depth: %d, product: %d\n", horizontal, depth, horizontal * depth);
    
    return 0;
}
