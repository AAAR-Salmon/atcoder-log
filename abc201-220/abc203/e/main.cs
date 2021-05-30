using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
	static void Main(string[] args)
	{
		var NM = Console.ReadLine().Split().Select(int.Parse).ToArray();
		var N = NM[0];
		var M = NM[1];
		var BlackPawns = new Dictionary<int, HashSet<int>>();
		for (int i = 0; i < M; i++)
		{
			var XY = Console.ReadLine().Split().Select(int.Parse).ToArray();
			var X = XY[0];
			var Y = XY[1];
			if (!BlackPawns.ContainsKey(X))
			{
				BlackPawns.Add(X, new HashSet<int>());
			}
			BlackPawns[X].Add(Y);
		}

		var dp = new HashSet<int>();
		dp.Add(N);
		foreach (var (_, bk) in BlackPawns.OrderBy(x => x.Key))
		{
			var dpAdd = new List<int>();
			var dpRem = new List<int>();
			foreach (var j in bk)
			{
				if (!dp.Contains(j) && (dp.Contains(j - 1) || dp.Contains(j + 1)))
				{
					dpAdd.Add(j);
				}
				if (dp.Contains(j) && (!dp.Contains(j - 1) && !dp.Contains(j + 1)))
				{
					dpRem.Add(j);
				}
			}
			foreach (var j in dpAdd) dp.Add(j);
			foreach (var j in dpRem) dp.Remove(j);
		}

		Console.WriteLine(dp.Count);
	}
}
