#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include<math.h>
#define PI 3.141592653589
double complex* fft(double complex* x, int n){
    if(n==1){
        return x;
        
    }
    double complex* even = malloc((n/2)*sizeof(double complex));
    double complex* odd = malloc((n/2)*sizeof(double complex));
    int i;
    for(i=0;i<n/2;i++){
        even[i] = x[2*i];
        odd[i] = x[(2*i)+1];
        
    }
    double complex* y_even =fft(even,n/2);
    double complex* y_odd = fft(odd,n/2);
    double complex* y = malloc((n)*sizeof(double complex));
    for(i=0;i<n/2;i++){
        double w_imag = sin(2*PI*i/n);
		double w_real  = cos(2*PI*i/n);
		y[i] = y_even[i] + (w_real+I*w_imag)*y_odd[i];
		y[i + n/2] = y_even[i] - (w_real+I*w_imag)*y_odd[i];
    }
    free(y_even);
    free(y_odd);
    return y;
    
    
    
}
double complex* ifft(double complex* y, int n){
    if(n==1){
        return y;
        
    }
    double complex* even = malloc((n/2)*sizeof(double complex));
    double complex* odd = malloc((n/2)*sizeof(double complex));
    int i;
    for(i=0;i<n/2;i++){
        even[i] = y[2*i];
        odd[i] = y[(2*i)+1];
        
    }
    double complex* y_even =ifft(even,n/2);
    double complex* y_odd = ifft(odd,n/2);
    double complex* x1 = malloc((n)*sizeof(double complex));
    for(i=0;i<n/2;i++){
        double w_imag = sin(-2*PI*i/n);
		double w_real  = cos(-2*PI*i/n);
		x1[i] = y_even[i] + (w_real+I*w_imag)*y_odd[i];
		x1[i + n/2] = y_even[i] - (w_real+I*w_imag)*y_odd[i];
    }
    free(y_even);
    free(y_odd);
    return x1;
    
    
    
}

int main() {
    int n=8;
	double complex  x[8] = {1,2,3,4,5,5,6,0};  
	double complex* y = fft(x,n);
	double complex* y1 = ifft(y,n); 
	printf("%s\n","fft" );
	for(int i=0;i<n;i++)
	{
		  printf( "%f %f\n", creal(y[i]), cimag(y[i]));

	}
	printf("%s\n","ifft" );
	for(int i=0;i<n;i++)
	{
		  printf( "%f %f\n", creal(y1[i])/n, cimag(y1[i])/n);

	}
    
    
    return 0;
}

