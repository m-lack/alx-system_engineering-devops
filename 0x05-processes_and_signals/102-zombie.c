#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - Runs an infinite loop to keep the parent alive.
 * 
 * Return: 0 on success.
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid == 0)  // Child process
        {
            // Child exits immediately
            return 0;
        }
        else if (pid > 0)  // Parent process
        {
            printf("Zombie process created, PID: %d\n", pid);
        }
        else
        {
            // Fork failed
            perror("Fork failed");
            return 1;
        }
    }
    infinite_while();
    return (0);
}

