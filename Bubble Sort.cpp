void bubbleSort(vector<int>& arr, int n)
{   
    
    // Write your code here.
    for (int i=1; i<n; i++){
        int count = 0;
        for (int j=0; j<n-i; j++){
            if (arr[j]>arr[j+1]){
                swap(arr[j], arr[j+1]);
                count = 1;
            }
        }
        if (count == 0){
            break;
        }
    }
}
