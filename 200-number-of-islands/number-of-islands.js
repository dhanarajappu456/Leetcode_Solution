/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let island = 0;
    let visited = new Set();

    function bfs(i, j, visited) {
        const queue = [];
        queue.push([i, j]);
        visited.add(`${i}-${j}`);

        while (queue.length) {
            const [r, c] = queue.shift();
            const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

            for (const [dr, dc] of directions) {
                const x = r + dr;
                const y = c + dc;

                if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && !visited.has(`${x}-${y}`) && grid[x][y] === "1") {
                    queue.push([x, y]);
                    visited.add(`${x}-${y}`);
                }
            }
        }
    }

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === "1" && !visited.has(`${i}-${j}`)) {
                island++;
                bfs(i, j, visited);
            }
        }
    }

    return island;
};
