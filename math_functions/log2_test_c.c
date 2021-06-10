/* This should be compiled on GCC */

#include <sys/time.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <time.h>

#define COUNT 1<<17
#define LEN 4
int num = 9999;

/* Bit shifting until the correct answer */
/* O(log n) time, where n is the input number */
int32_t log2_a(uint32_t num){
    int32_t int_log = -1;
    uint32_t x = num;
    while(x != 0){
        int_log++;
        x = x >> 1;
    }
    return int_log;
}

/* GCC builtin Leading Zero Count */
int32_t log2_b(uint32_t num){
    return 32 - __builtin_clz(num) - 1;
}

const int tab32[32] = {
     0,  9,  1, 10, 13, 21,  2, 29,
    11, 14, 16, 18, 22, 25,  3, 30,
     8, 12, 20, 28, 15, 17, 24,  7,
    19, 27, 23,  6, 26,  5,  4, 31
};

/* Binary search and lookup table*/
/* O(log(log n)) time */
int32_t log2_c (uint32_t value)
{
    value |= value >> 1;
    value |= value >> 2;
    value |= value >> 4;
    value |= value >> 8;
    value |= value >> 16;
    return tab32[(uint32_t)(value*0x07C4ACDD) >> 27];
}

/* Binary search */
/* O(log(log n)) time */
int32_t log2_d(uint32_t num){
   int32_t result = 0;
   if(num & 0xFFFF0000){ /* if bits higher than 2^16 are set */
       num >>= 16;
       result |= 16;
   }
   if(num & 0xFF00){ /* if bits higher than 2^8 are set */
       num >>= 8;
       result |= 8;
   }
   if(num & 0xF0){ /* if bits higher than 2^4 are set */
       num >>= 4;
       result |= 4;
   }
   if(num & 0xC){ /* if bits higher than 2^2 are set */
       num >>= 2;
       result |= 2;
   }
   if(num & 0x2){ /* if bits higher than 2^1 are set */
       num >>= 1;
       result |= 1;
   }
   return result;
}

/* Sort the results for analysis */
int sort(const void *a, const void *b){
   int x = *(int*)a;
   int y = *(int*)b;
   if(x < y)
       return 1;
   if(x > y)
       return -1;
   return 0;
}

/* Tests */
int main(){
    int i, sum;
    int arr[LEN]; /* Array of times */
    char *name[100]; /* Hash table where key=time, value=name of function */
    printf("Number to find log2 of: %d\n",num);
    printf("Number of iterations: %d\n\n", COUNT);

    printf("%d\n",log2_a(num));
    sum = 0;
    for(i=0;i<COUNT;i++){
        double ms = clock();
        log2_a(num);
        double c = clock();
        sum += c-ms;
    }
    printf("log2_a (bit-shifting) sum time: %d\n\n",sum);
    arr[0] = sum;
    name[sum % 100] = "log2_a (bit-shifting)";

    printf("%d\n",log2_b(num));
    sum = 0;
    for(i=0;i<COUNT;i++){
        double ms = clock();
        log2_b(num);
        double c = clock();
        sum += c-ms;
    }
    printf("log2_b (builtin clz) sum time: %d\n\n",sum);
    arr[1] = sum;
    name[sum % 100] = "log2_b (builtin clz)";

    printf("%d\n",log2_c(num));
    sum = 0;
    for(i=0;i<COUNT;i++){
    	double ms = clock();
    	log2_c(num);
    	double c = clock();
    	sum += c-ms;
    }
    printf("log2_c (binary search + lookup table) sum time: %d\n\n",sum);
    arr[2] = sum;
    name[sum % 100] = "log2_c (binary search + lookup table)";

    printf("%d\n",log2_d(num));
    sum = 0;
    for(i=0;i<COUNT;i++){
    	double ms = clock();
    	log2_d(num);
    	double c = clock();
    	sum += c-ms;
    }
    printf("log2_d (binary search) sum time: %d\n\n",sum);
    arr[3] = sum;
    name[sum % 100] = "log2_d (binary search)";

    qsort(arr, LEN, sizeof(int), sort);
    for(i = LEN-1; i > 0; i--){
      printf("%d. %s, ", LEN-i, name[arr[i] % 100]);
      printf("%d, %.2f percent faster\n",arr[i], -100 * (1 - (float)arr[i-1]/(float)arr[i]));
    }
    printf("%d. %s, ", LEN, name[arr[i] % 100]);
    printf("%d\n",arr[i]);
}
