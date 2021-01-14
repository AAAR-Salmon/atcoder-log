function main(input) {
	const N = parseInt(input, 10);
	let ans = 0;
	for (let j = 1; j <= N; j++) {
		ans += j * Math.floor(N / j) * (Math.floor(N / j) + 1) / 2;
	}
	console.log(ans);
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
