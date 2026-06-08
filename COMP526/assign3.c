#include <stdio.h>
#include <math.h>


// global variables
// allows for array to be used in multiple functions
float xj[100];

// function tested and works
double choosetest(int t)                //fuction to check t is a valid test
{                                      //returns what test was chosen
    switch(t) {
        case 1: 
            printf("You chose 1. Natural Logrithm\n\n");
            break;

        case 2:
            printf("You chose 2. Tangent\n\n");
            break;

        case 3:
            printf("You chose 3. Arcsine\n\n");
            break;

        case 4:
            printf("You chose 4. Hyperbolic cosine\n\n");
            break;

        case 5:
            printf("You chose 5. Hyperbolic Arctangent\n\n");
            break;

        default:
            printf("\nYou did not select a test.\n\n");
    }
}

// function tested and works
double checkint (int t, float a, float b)      //check whether the interval is in range of function
{
    int k;

    switch (t){
        case 1:
            if ((a == 0 || b == 0) || (a < 0 && b > 0)){        //ln(x) is undefined when x < 0; D/Dx ln(x) is undefined a x=0
                k = 0;                                         // integral of ln(x) is undefined at x = 0
            }
            else{
                k = 1;
            }
            break;
        case 2:
            if ((a == (M_PI/2) || b == (M_PI/2)) || (a < (M_PI/2) && b > (M_PI/2))){  //tan(x) is undefined when x = pi/2 + 2x
                k = 0;
            }
            else{
                k = 1;
            }
            break;
        case 3:
            if (a < 1 || b < 1){    // Arcsine is undefined when x < 1
                k = 0;
            }
            else{
                k = 1;
            }
            break;
        case 4:                     //hyperbolic cosine has no domain error
            k = 1;
            break;
        case 5:
            if (a == 1 || b == 1 || a == (-1) || b == (-1)){   // Hyperbolic Arctangent has a domain error at x = +/- 1
                k = 0;
            }
            else{
                k = 1;
            }
            break;
            }
    
    return k;
}

// function tested and works
int checkn(int n)               // function to verify n is an integer 
{                               // that is <= 100
    int k;

    if (n > 0 && n <= 100){
        k == 0;
    }
    else {
        k == 1;
    }
    return k;
}

// function tested and works
double subintervals(int n, double a, double b)        // function to determine the subintervals for the
{                                                   // approximations of derivative and integral
    double sub = (b-a)/ (float)n;
    int i = 0; 
    double j = a + sub;

    for (i = 0; i < n - 1 ; i = i + 1)
            xj[i] = j + (i * sub);
    
    printf("Subinterval Values: ");
    for (i = 0; i < n - 1; i++)
        printf("%lf ", xj[i]);
    printf("\n");

}

double derivative(int t, int n)
{
    int i = 0;
    double epsi = pow(10, -16);
    double fx_fdpx[100];
    double dh[100];
    double fx_plus_dh[100];
    double fx_minus_dh[100];
    double approx_fpx[100];
    double exact_fpx[100];
    double difference[100];

    switch (t){
        case 1:         //log(x)
            for (i = 0; i < n - 1 ; i = i + 1)
                exact_fpx[i] = (1 / xj[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_fdpx[i]= fabs((log(xj[i])) * (-1) * pow(xj[i],2));

            for (i = 0; i < n - 1 ; i = i + 1)
                dh[i]= 2 * sqrt(fx_fdpx[i] * epsi);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_plus_dh[i]= log(xj[i] + dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_minus_dh[i]= log(xj[i] - dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                approx_fpx[i]= (fx_plus_dh[i] - fx_minus_dh[i]) / (2 * dh[i]);


            break;

        case 2:         //tan(x)
            for (i = 0; i < n - 1 ; i = i + 1)
                exact_fpx[i] = (1/ pow(cos(xj[i]),2));

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_fdpx[i]= fabs(0.5 * cos(xj[i]) * cos(xj[i]));

            for (i = 0; i < n - 1 ; i = i + 1)
                dh[i]= 2 * sqrt(fx_fdpx[i] * epsi);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_plus_dh[i]= tan(xj[i] + dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_minus_dh[i]= tan(xj[i] - dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                approx_fpx[i]= (fx_plus_dh[i] - fx_minus_dh[i]) / (2 * dh[i]);

            break;

        case 3:         //asin(x)
            for (i = 0; i < n - 1 ; i = i + 1)
                exact_fpx[i] = (1 / sqrt(1 - pow(xj[i], 2)));

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_fdpx[i]= fabs(asin(xj[i]) * pow(1 - pow(xj[i],2), 1.5) / xj[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                dh[i]= 2 * sqrt(fx_fdpx[i] * epsi);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_plus_dh[i]= asin(xj[i] + dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_minus_dh[i]= asin(xj[i] - dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                approx_fpx[i]= (fx_plus_dh[i] - fx_minus_dh[i]) / (2 * dh[i]);


            break;
        case 4:         //cosh(x)
            for (i = 0; i < n - 1 ; i = i + 1)
                exact_fpx[i] = sinh(xj[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_fdpx[i]= fabs(cosh(xj[i]) / cosh(xj[i]));

            for (i = 0; i < n - 1 ; i = i + 1)
                dh[i]= 2 * sqrt(fx_fdpx[i] * epsi);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_plus_dh[i]= cosh(xj[i] + dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_minus_dh[i]= cosh(xj[i] - dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                approx_fpx[i]= (fx_plus_dh[i] - fx_minus_dh[i]) / (2 * dh[i]);


            break;
        case 5:         //atanh(x)
            for (i = 0; i < n - 1 ; i = i + 1)
                exact_fpx[i] = (1/ (1 - pow(xj[i],2)));

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_fdpx[i]= fabs(atanh(xj[i]) * pow(1 - pow(xj[i], 2), 2) / (2 * xj[i]));

            for (i = 0; i < n - 1 ; i = i + 1)
                dh[i]= 2 * sqrt(fx_fdpx[i] * epsi);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_plus_dh[i]= atanh(xj[i] + dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                fx_minus_dh[i]= atanh(xj[i] - dh[i]);

            for (i = 0; i < n - 1 ; i = i + 1)
                approx_fpx[i]= (fx_plus_dh[i] - fx_minus_dh[i]) / (2 * dh[i]);

            break;
    }
    for (i = 0; i < n - 1 ; i = i + 1)
        difference[i]= fabs(exact_fpx[i] - approx_fpx[i]);


    printf("point    exact derivative     approximated derivative   absolute value of their difference\n");
    printf("=============================================================================================\n\n");
    for (i = 0; i < n - 1; i++)
        printf("%lf      %lf               %lf                 %lf\n", xj[i], exact_fpx[i], approx_fpx[i], difference[i]);
}

// function tested and works
double integrals(int t, int n, double a, double b)
{
    double fa, fb, Fa, Fb, Fx;
    double ompow_a = 1 - pow(a, 2);
    double ompow_b = 1 - pow(b, 2);
    double exact_Fx;
    double approx_Fx;

    double summa_fx = 0;
    double sub = (b-a)/ (float)n;
    double func_sum[100];
    int i = 0;
    
    switch (t){
        case 1:                                 //log(x)
            fa = log(a);
            fb = log(b);
            Fa = a * log(a) - a;
            Fb = b * log(b) - b;

            for (i = 0; i < n - 1 ; i = i + 1)
                func_sum[i] = log(xj[i]);

            break;
        case 2:                                 //tan(x)
            fa = tan(a);
            fb = tan(b);
            Fa = log(1 / cos(a));
            Fb = log(1 / cos(b));

            for (i = 0; i < n - 1 ; i = i + 1)
                func_sum[i] = tan(xj[i]);

            break;
        case 3:                                 //asin(x)
            fa = asin(a);
            fb = asin(b);
            Fa = a * asin(a) + sqrt(ompow_a);
            Fb = b * asin(b) + sqrt(ompow_b);

            for (i = 0; i < n - 1 ; i = i + 1)
                func_sum[i] = asin(xj[i]);

            break;
        case 4:                                 //cosh(x)
            fa = cosh(a);
            fb = cosh(b);
            Fa = sinh(a);
            Fb = sinh(b);

            for (i = 0; i < n - 1 ; i = i + 1)
                func_sum[i] = cosh(xj[i]);

            break;
        case 5:                                 //atanh(x)
            fa = atanh(a);
            fb = atanh(b);
            Fa = 0.5 * log(ompow_a) + a * atanh(a);
            Fb = 0.5 * log(ompow_b) + b * atanh(b);

            for (i = 0; i < n - 1 ; i = i + 1)
                func_sum[i] = atanh(xj[i]);

            break;
    }


    for (i = 0; i < n - 1 ; i = i + 1)          //summation part in trapezoidal rule
        summa_fx = summa_fx + func_sum[i];

    approx_Fx = sub * ((fa * 0.5) + summa_fx + (fb * 0.5));     //trapezoidal rule
    exact_Fx = Fb - Fa;

    printf("\nExact integral: %lf,   Approx integral: %lf,    Error: %lf\n", exact_Fx, approx_Fx, fabs(exact_Fx - approx_Fx));


}

// main funtion to input values and run functions
double main(void)
{ 
    int test;
    double a, b;
    int n;
    int k = 0;
   
    do {printf("1. Natural Logrithm\n2. Tangent\n3. Arcsine\n4. Hyperbolic cosine\n5. Hyperbolic Arctangent\nPlease enter a number to select a test: ");
        scanf("%d", &test);
        choosetest(test);
    }
    while (test <= 0, test > 5);

    do{ printf("Enter an interval [a,b] where a < b.\n\nEnter a: ");
        scanf("%lf", &a);
        printf("\nEnter b: ");
        scanf("%lf", &b);

        k = checkint(test, a, b);
    } while (k == 0 || b < a);

    printf("The interval is [%f,%f]\n", a, b);

    while(k == 1)
    {   printf("Enter a positive integer n <= 100:  ");
        scanf("%d", &n);
        k = checkn(n);
    }
    printf("Interval will be divided in %d subunits\n", n);

    subintervals(n, a, b);
    derivative(test, n);
    integrals(test, n, a, b);

    
    return 0;
}