#include <iostream>
using namespace std;

int sqrtInteger(int n){
  int s = 0;
  int e = n;
  long long int mid = s + (e-s)/2;
   int ans = -1;
  while (s<=e){
    long long int sq = mid*mid;
    if (sq == n){
      ans = mid;
      return mid;
    }
    else if (sq > n){
      e = mid - 1;
    }
    else{
      ans = mid;
      s = mid + 1;
    }
    mid = s + (e-s)/2;
  }
  return ans;
}

double sqrtDecimal(int ans, int decimals, int n){
  double factor = 1;
  double result = ans;
  for(int i = 0; i< decimals ; i++){
    factor = factor/10;
    for (double j = ans; j*j<n; j+=factor){
      result = j;
    }
  }
  return result;
}


int main() {
    int n;
  cout << "Enter the value of n: ";
  cin >> n;
  int ans = sqrtInteger(n);
  cout << sqrtDecimal(ans, 3, n);
  
}

