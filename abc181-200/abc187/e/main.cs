using System;
using System.Collections.Generic;
using System.Linq;

class Program {
		static void Main() {
		int N = int.Parse(Console.ReadLine());
		int[] a = new int[N];
		int[] b = new int[N];
		List<int>[] children = new List<int>[N + 1];
		int[] parent = new int[N + 1];

		for (int i = 0; i <= N; i++) {
			children[i] = new List<int>();
		}

		for (int i = 1; i < N; i++) {
			int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
			a[i] = input[0];
			b[i] = input[1];
			children[a[i]].Add(b[i]);
			children[b[i]].Add(a[i]);
		}

		children[1].Add(0);
		Queue<(int, int)> q1 = new Queue<(int, int)>();
		q1.Enqueue((1, 0));
		while (q1.Count > 0) {
			(var n, var p) = q1.Dequeue();
			parent[n] = p;
			children[n].Remove(p);
			foreach (var c in children[n]) {
				q1.Enqueue((c, n));
			}
		}

		long[] ans = new long[N + 1];

		int Q = int.Parse(Console.ReadLine());
		for (int i = 0; i < Q; i++) {
			string[] input = Console.ReadLine().Split();
			int t = int.Parse(input[0]);
			int e = int.Parse(input[1]);
			long x = long.Parse(input[2]);
			int A, B;
			if (t == 1) {
				A = a[e];
				B = b[e];
			} else {
				A = b[e];
				B = a[e];
			}
			if (parent[A] == B) {
				ans[A] += x;
			} else {
				ans[1] += x;
				ans[B] -= x;
			}
		}

		Queue<int> q2 = new Queue<int>();
		q2.Enqueue(1);
		while (q2.Count > 0) {
			int n = q2.Dequeue();
			ans[n] += ans[parent[n]];
			foreach (var c in children[n]) {
				q2.Enqueue(c);
			}
		}

		for (int i = 1; i <= N; i++) {
			Console.WriteLine(ans[i]);
		}
	}
}
