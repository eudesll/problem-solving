/* 
   URI
   Problem Id : 1036
   Problem Name: Fórmula de Bhaskara
*/

#include "stdio.h"
#include "math.h"
  
int main()
{
    double a, b, c, delta, r1, r2;

    scanf("%lf %lf %lf", &a, &b, &c);
  
    delta = (b * b) - (4 * a * c);
  
    if(a == 0 || delta < 0){
        printf("Impossivel calcular\n");
        return 0;
    }
  
    r1 = ((b *-1) + sqrt(delta)) / (2 * a);
    r2 = ((b *-1) - sqrt(delta)) / (2 * a);
  
    printf("R1 = %.5lf\n", r1);
    printf("R2 = %.5lf\n", r2);

    return 0;
}