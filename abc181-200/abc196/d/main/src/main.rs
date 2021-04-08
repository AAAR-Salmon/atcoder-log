fn main() {
	proconio::input! {
		h: usize,
		w: usize,
		a: usize,
		b: usize
	}
	let filled: u32 = 0;
	println!("{}", dfs(0, 0, 0, 0, h, w, a, b, filled));
}

fn dfs(i: usize, j: usize, a: usize, b: usize, _h: usize, _w: usize, _a: usize, _b: usize, filled: u32) -> usize {
	if a > _a || b > _b {
		return 0;
	} else if i == _h {
		return 1;
	} else if j == _w {
		return dfs(i + 1, 0, a, b, _h, _w, _a, _b, filled);
	} else if filled >> (i * _w + j) & 1 != 0 {
		return dfs(i, j + 1, a, b, _h, _w, _a, _b, filled);
	}

	let mut tate: usize = 0;
	let mut yoko: usize = 0;
	let square: usize = dfs(i, j + 1, a, b + 1, _h, _w, _a, _b, filled);

	if i + 1 < _h {
		tate = dfs(i, j + 1, a + 1, b, _h, _w, _a, _b, filled | 1 << ((i + 1) * _w + j));
	}
	if j + 1 < _w {
		yoko = dfs(i, j + 2, a + 1, b, _h, _w, _a, _b, filled);
	}

	return tate + yoko + square;
}
