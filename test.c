#include <stdio.h>

int main(void)
{

    int count;
    int count2;

    for (count = 1; count < 10; count++)
        for (count2 = 1; count2 < 10; count2++)
            if ((count * count2) % 2 == 0)
            {
                printf("%d*%d = %d\n", count, count2, count * count2);
            }

    printf("for 문 종료 후 카운트 변수의 값 : %d\n", count);
    return 0;
}