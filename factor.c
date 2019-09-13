#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define ui64 unsigned long long

void factor(ui64 x){
  int prime = 1;
  ui64 n = x;
  if(n == 2){
    printf("%d\n",2);
    return;
  }
  /* Find is n is even and if so, factor n/2 */
  else if(n % 2 == 0){
    printf("%d\n",2);
    n /= 2;
    factor(n);
    return;
  }
  ui64 lim = n/2;
  lim = (lim + n/lim)/2;
  lim += 10;
  /* Factor out odd integers and print any factors found */
  for(ui64 i=3;i<lim;i+=2){
    if(n % i == 0){
      printf("%llu\n",i);
      n /= i;
      prime = 0;
      break;
    }
  }
  /* If a factor was found, factor (n/found factor)*/
  if(!prime){
    factor(n);
  }
  /* Else, n is prime and we stop */
  else{
    printf("%llu\n",n);
    return;
  }
}

int main(void){
  factor(2090862748777986991);
}