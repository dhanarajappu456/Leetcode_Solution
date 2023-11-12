import java.util.*;

class Graph {

    private Map<Integer, List<int[]>> adj;
    private int n;
    private int[] dist;

    public Graph(int n, int[][] edges) {
        this.adj = new HashMap<>();
        this.n = n;

        for (int[] edge : edges) {
            int s = edge[0];
            int d = edge[1];
            int w = edge[2];

            adj.computeIfAbsent(s, k -> new ArrayList<>()).add(new int[]{d, w});
        }
    }

    public void addEdge(int[] edge) {
        int s = edge[0];
        int d = edge[1];
        int w = edge[2];

        adj.computeIfAbsent(s, k -> new ArrayList<>()).add(new int[]{d, w});
    }

    public int shortestPath(int node1, int node2) {
        //PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        //or
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a->a[1]));
        pq.offer(new int[]{node1, 0});

        dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[node1] = 0;

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int node = current[0];
            int nodeWt = current[1];

            for (int[] neighbor : adj.getOrDefault(node, Collections.emptyList())) {
                int neib = neighbor[0];
                int neibWt = neighbor[1];

                if (nodeWt + neibWt < dist[neib]) {
                    dist[neib] = nodeWt + neibWt;
                    pq.offer(new int[]{neib, dist[neib]});
                }
            }
        }

        return dist[node2] == Integer.MAX_VALUE ? -1 : dist[node2];
    }
}

// Example usage:
// Graph obj = new Graph(4, new int[][]{{0, 1, 1}, {0, 2, 3}, {1, 2, 1}, {2, 3, 1}});
// obj.addEdge(new int[]{1, 3, 2});
// int result = obj.shortestPath(0, 3);
// System.out.println(result);
