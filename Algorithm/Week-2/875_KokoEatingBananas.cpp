class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int piles_size = piles.size();
        int k_min = 1;
        int k_max = *max_element(piles.begin(), piles.end());

        while(k_min < k_max){
            int k = k_min + (k_max - k_min) / 2;
            long long h_sum = 0;

            for(int j = 0; j < piles_size; j++){
                h_sum += (piles[j] + k - 1) / k;
            }

            if(h_sum <= h){
                k_max = k;
            }
            else{
                k_min = k + 1;
            }
        }

        return k_min;
    }
};


// 시간 초과 발생
// class Solution {
// public:
//     int minEatingSpeed(vector<int>& piles, int h) {
//         sort(piles.begin(), piles.end());
//         int piles_size = piles.size();
//         int k_max = piles[piles_size - 1];
//         int k_min = k_max;

//         if(piles_size == 1){
//             if(piles[0] % h == 0) return piles[0] / h;
//             else return piles[0] / h + 1;
//         }

//         for(int k = 1; k <= k_max; k++){
//             long long h_sum = 0;

//             for(int j = 0; j < piles_size; j++){
//                 int division = piles[j] / k;
//                 int reminder = piles[j] % k;

//                 if(reminder == 0) h_sum = h_sum + division;
//                 else h_sum = h_sum + division + 1;
//             }

//             if(h_sum <= h){
//                 k_min = k;
//                 break;
//             }
//         }

//         return k_min;
//     }
// };