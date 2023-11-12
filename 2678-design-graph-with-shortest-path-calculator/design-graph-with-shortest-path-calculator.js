/**
 * @param {number} n
 * @param {number[][]} edges
 */
var Graph = function(n, edges) {
    this.adj = new Map();
        this.n = n;
        
        for (const [s, d, w] of edges) {
            if (!this.adj.has(s)) {
                this.adj.set(s, []);
            }
            this.adj.get(s).push([d, w]);
        }
};

/** 
 * @param {number[]} edge
 * @return {void}
 */
Graph.prototype.addEdge = function(edge) {
     const [s, d, w] = edge;
        if (!this.adj.has(s)) {
            this.adj.set(s, []);
        }
        this.adj.get(s).push([d, w]);
};

/** 
 * @param {number} node1 
 * @param {number} node2
 * @return {number}
 */
Graph.prototype.shortestPath = function(node1, node2) {
     const pq = [[node1, 0]];
        this.dist = new Array(this.n).fill(Number.POSITIVE_INFINITY);
        this.dist[node1] = 0;

        while (pq.length > 0) {
            pq.sort((a, b) => a[1] - b[1]);
            const [node, nodeWt] = pq.shift();

            for (const [neib, neibWt] of this.adj.get(node) || []) {
                if (nodeWt + neibWt < this.dist[neib]) {
                    this.dist[neib] = nodeWt + neibWt;
                    pq.push([neib, nodeWt + neibWt]);
                }
            }
        }

        return this.dist[node2] === Number.POSITIVE_INFINITY ? -1 : this.dist[node2];
};

/** 
 * Your Graph object will be instantiated and called as such:
 * var obj = new Graph(n, edges)
 * obj.addEdge(edge)
 * var param_2 = obj.shortestPath(node1,node2)
 */