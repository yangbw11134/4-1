class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        if(k % (m*n) == 0) return grid;
        vector<vector<int>> shift_grid(m, vector<int>(n));
        for(int r=0; r<k; r++){
            for(int i=0; i<m; i++){
                for(int j=0; j<n; j++){
                    if(i==m-1 && j==n-1) shift_grid[0][0] = grid[i][j];
                    else if(j==n-1) shift_grid[i+1][0] = grid[i][n-1];
                    else shift_grid[i][j+1] = grid[i][j];

                }
            }
            grid = shift_grid;
        }
        return shift_grid;

    }
};