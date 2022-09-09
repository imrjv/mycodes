void selectionSort(vector<int>& arr, int n)
{   
    for (int i = 0; i<n; i++){
        int miniIndex = i;
        for (int j=i+1; j<n; j++){
            if (arr[j] < arr[miniIndex]){
                miniIndex = j; 
            }
        }
        swap(arr[i], arr[miniIndex]);
    }
   
}
