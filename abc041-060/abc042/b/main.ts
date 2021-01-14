import * as fs from 'fs'

function main(input: string[][]): void {
    const S = input.slice(1).map(row => row[0]);

    S.sort();

    console.log(S.join(''));
}

main(fs.readFileSync('/dev/stdin', 'utf-8')
       .split('\n')
       .map((s: string) => s.split(' ')));
