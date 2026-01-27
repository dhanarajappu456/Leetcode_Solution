import java.util.*;

class Pair {
    int dist;
    int node;

    Pair(int dist, int node) {
        this.dist = dist;
        this.node = node;
    }
}

class Edge {
    int to;
    int wt;

    Edge(int to, int wt) {
        this.to = to;
        this.wt = wt;
    }
}

class Solution {
    public int minCost(int n, int[][] edges) {

        Map<Integer, List<Edge>> adj = new HashMap<>();
        Map<Integer, List<Edge>> indegree = new HashMap<>();

        // Build graph
        for (int[] e : edges) {
            int a = e[0], b = e[1], w = e[2];

            adj.computeIfAbsent(a, k -> new ArrayList<>())
               .add(new Edge(b, w));

            indegree.computeIfAbsent(b, k -> new ArrayList<>())
                    .add(new Edge(a, 2 * w));
        }

        int[] d = new int[n];
        Arrays.fill(d, Integer.MAX_VALUE);
        d[0] = 0;

        PriorityQueue<Pair> pq =
                new PriorityQueue<>((x, y) -> x.dist - y.dist);

        pq.add(new Pair(0, 0));

        while (!pq.isEmpty()) {
            Pair cur = pq.poll();
            int node = cur.node;
            int nodeWt = cur.dist;

            if (node == n - 1)
                return d[node];

       

            // normal outgoing edges
            if (adj.containsKey(node)) {
                for (Edge e : adj.get(node)) {
                    if (nodeWt + e.wt < d[e.to]) {
                        d[e.to] = nodeWt + e.wt;
                        pq.add(new Pair(d[e.to], e.to));
                    }
                }
            }

            // reversed incoming edges
            if (indegree.containsKey(node)) {
                for (Edge e : indegree.get(node)) {
                    if (nodeWt + e.wt < d[e.to]) {
                        d[e.to] = nodeWt + e.wt;
                        pq.add(new Pair(d[e.to], e.to));
                    }
                }
            }
        }

        return -1;
    }
}
