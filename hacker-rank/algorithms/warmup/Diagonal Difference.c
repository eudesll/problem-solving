/* 
   HackerRank
   Problem Name: diagonal-difference
*/

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){

    int n, f = 0, b = 0; 

    scanf("%d",&n);

    int a[n][n];
    for(int a_i = 0; a_i < n; a_i++){

       for(int a_j = 0; a_j < n; a_j++){            
          scanf("%d",&a[a_i][a_j]);

          if(a_i == a_j){
              f += a[a_i][a_j];
          }
          if(a_j == (n - 1) - a_i){
              b += a[a_i][a_j];
          }
       }
    }

    printf("%d", abs(f - b));
    
    return 0;
}