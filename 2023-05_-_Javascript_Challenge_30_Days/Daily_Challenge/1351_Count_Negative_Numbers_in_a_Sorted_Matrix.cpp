class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int counter = 0;
        int height = grid.size();
        int width = grid[0].size();
        int x = width - 1;
        int y = 0; 

        while (x >= 0 && y < height) {
            if (grid[y][x] < 0){
                counter += (height - y);
                x -= 1;
            }
            else {
                y += 1;
            }
        }
        return counter;
    }
};
